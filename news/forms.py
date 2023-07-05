from django import forms
from.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title','content', }

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(max_length=1000, widget= forms.Textarea)
    cc = forms.BooleanField(required=False)