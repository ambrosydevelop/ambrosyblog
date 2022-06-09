from attr import attr
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea(attrs={
        'style':'color:black;width:200px;height:15px;resize:none;','class':'form-control'
        }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'style':'color:black;width:200px;height:40px;resize:none;','class':'form-control','type':'password'
    }))

    class Meta:
        model = User
        fields = ['username','password']
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.Textarea(attrs={
        'style':'color:black;width:200px;height:15px;resize:none;','class':'form-control'
        }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'style':'color:black;width:200px;height:40px;resize:none;','class':'form-control','type':'password'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'style':'color:black;width:200px;height:40px;resize:none;','class':'form-control','type':'password'
    }))
    
    class Meta:
        model = User
        fields = ['username','password1','password2']