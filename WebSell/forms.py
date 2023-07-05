from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:

        model = Account
        fields = '__all__'
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'User name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password'})
        } 



class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Tiêu đề'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'content': forms.Textarea(attrs={'placeholder':'Nội dung'})
        }