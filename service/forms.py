from django import forms
from .models import Identification

class IdentificationForm(forms.ModelForm):

	class Meta:
		model = Identification
		fields = ('id_card_img','selfie_img')