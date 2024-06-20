from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    '''
    displays text for user to knwo the fields
    '''
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')