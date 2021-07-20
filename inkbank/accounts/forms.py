from django import forms
from django.core.exceptions import ValidationError

from .models import Account


class NewAccountForm(forms.ModelForm):
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
