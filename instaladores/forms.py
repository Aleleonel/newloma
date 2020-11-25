from django import forms


from .models import Instaladores


class InstaladoresForm(forms.ModelForm):

    class Meta:
        model = Instaladores
        fields = '__all__'
