from django import forms


from .models import Veiculos


class VeiculosForm(forms.ModelForm):

    class Meta:
        model = Veiculos
        fields = '__all__'
