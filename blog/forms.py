from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    comment model
    '''
    class Meta:
        model = Comment
        fields = ('body',)