from django import forms
from .models import ReturnMoney

class ReturnModelForm(forms.ModelForm):
    class Meta:
        model = ReturnMoney
        fields = ["title",
                  "amount",
                  "short_description"]

        widgets={
            'title': forms.TextInput(attrs={'class':'form-title'}),
            'amount': forms.NumberInput(attrs={'class':'form-amount'}),
            'short_description': forms.TextInput(attrs={'class':'form-description'})
        }