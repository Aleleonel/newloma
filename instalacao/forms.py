from django import forms

from .models import Instalacao


class InstalacaoForm(forms.ModelForm):

    class Meta:
        model = Instalacao
        fields = '__all__'

