from django import forms
from django.core.exceptions import ValidationError

from .models import Account


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["kind", "number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["kind"].widget.attrs.update(
            {
                "class": "mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            }
        )
        self.fields["number"].widget.attrs.update(
            {
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        )


class SearchAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["number"].widget.attrs.update(
            {
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        )


class SimpleOperationAccountForm(forms.Form):
    number = forms.IntegerField(
        label="Número",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )
    value = forms.DecimalField(
        label="Valor",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )

    def clean_number(self):
        number = self.cleaned_data["number"]
        if not Account.objects.filter(number=number).exists():
            raise ValidationError("Não existe nenhuma conta com este número.")

        return number

    def clean_value(self):
        value = self.cleaned_data["value"]
        if value <= 0:
            raise ValidationError("O valor tem que ser maior que 0.")

        return value


class TransferAccountForm(forms.Form):
    number_sender = forms.IntegerField(
        label="Número da conta remetente",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )
    number_receiver = forms.IntegerField(
        label="Número da conta destinatária",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )
    value = forms.DecimalField(
        label="Valor",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )

    def clean_number_sender(self):
        number = self.cleaned_data["number_sender"]
        if not Account.objects.filter(number=number).exists():
            raise ValidationError("Não existe nenhuma conta com este número.")

        return number

    def clean_number_receiver(self):
        number = self.cleaned_data["number_receiver"]
        if not Account.objects.filter(number=number).exists():
            raise ValidationError("Não existe nenhuma conta com este número.")

        return number

    def clean_value(self):
        value = self.cleaned_data["value"]
        if value <= 0:
            raise ValidationError("O valor tem que ser maior que 0.")

        sender = Account.objects.get(number=self.cleaned_data["number_sender"])
        if sender.balance < value:
            raise ValidationError(
                f"O remetente não tem esse valor para transferir. Saldo do remetente: R$ {sender.balance}"
            )

        return value


class EarnInterestAccountForm(forms.Form):
    number = forms.IntegerField(
        label="Número",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )
    interest = forms.DecimalField(
        label="Taxa de juros",
        widget=forms.TextInput(
            attrs={
                "class": "focus:ring-indigo-500 focus:border-indigo-500 flex-1 block w-full rounded-md sm:text-sm border-gray-300"
            }
        ),
    )

    def clean_number(self):
        number = self.cleaned_data["number"]
        if not Account.objects.filter(number=number).exists():
            raise ValidationError("Não existe nenhuma conta com este número.")

        account = Account.objects.get(number=number)
        if account.kind != Account.SAVINGS:
            raise ValidationError(
                f"Operação permitida apenas para contas poupança. Está é uma {account.get_kind_display().lower()}."
            )

        return number

    def clean_interest(self):
        interest = self.cleaned_data["interest"]
        if interest <= 0:
            raise ValidationError("Os juros tem que ser maior que 0.")

        return interest
