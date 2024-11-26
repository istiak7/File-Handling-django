from django import forms
from .models import Doccument
class DoccumentForm(forms.ModelForm):
    class Meta:
        model = Doccument
        fields = '__all__'