from django.contrib.auth.models import User
#gives us access to generic user class
from django import forms
#now we can create new user form class so we can structure user setup how we want

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)#hides password being typed in

  class Meta:
    #provides info about your class (userform)
    model = User
    #whenever a user signs up put them in user table
    fields = ['username', 'email', 'password']
