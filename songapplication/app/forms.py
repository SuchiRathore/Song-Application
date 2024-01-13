from django import forms
from .models import *

class AudioForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = "__all__"