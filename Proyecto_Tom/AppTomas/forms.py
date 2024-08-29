from django import forms

class Client(forms.Form):
    user = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)