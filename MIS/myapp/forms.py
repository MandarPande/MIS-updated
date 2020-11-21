from django import forms
from .models import Image,Student

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':'Upload','Ename':'Event Name','Edate':'Event Date','s_usn':'USN'}
