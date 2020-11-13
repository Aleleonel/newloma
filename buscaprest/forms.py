from django import forms


from .models import Prestador


class PrestadorForm(forms.ModelForm):

    class Meta:
        model = Prestador
        fields = '__all__'
