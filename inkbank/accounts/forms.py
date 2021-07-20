from django import forms

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
