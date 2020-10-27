from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

from .models import Pathology

class newPatho(forms.ModelForm):

	class Meta:
		model = Pathology
		fields = ('name', 'associated_gene_OMIM',)