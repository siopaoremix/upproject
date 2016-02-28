'''
Created on Feb 21, 2016

@author: Pao
'''

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class' : 'form-control input-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control input-sm'}), required=True)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid login")
        
        return self.cleaned_data
    
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
    
class VoteForm(forms.Form):
    president = forms.ChoiceField()