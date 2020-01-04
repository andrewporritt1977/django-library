from django import forms

class LibraryLoginForm(forms.Form):
    """ Library user login form """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
