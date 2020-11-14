from django import forms


from .models import Rastreador


class RastreadorForm(forms.ModelForm):

    class Meta:
        model = Rastreador
        fields = '__all__'
