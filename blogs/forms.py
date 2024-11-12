from django import forms
from .models import BlogSpot

class BlogFrom(forms.ModelForm):
    class Meta:
        model = BlogSpot
        fields = {'title','text'}
        labels = {'title':'Title', 'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}