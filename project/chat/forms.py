from django import forms
from .models import *

class typing(forms.ModelForm):
    class Meta:
        model = chat_mesg
        fields = ['message']
    
# message = forms.CharField(max_length=300)