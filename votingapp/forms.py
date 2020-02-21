from .models import*
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # firstname = forms.CharField()
    # lastname = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class VotersForm(forms.ModelForm):   
    class Meta:
        model = Voters
        fields = '__all__'

class VoteForm(forms.ModelForm):   
    # voter_id = forms.CharField(label='voter_id', max_length=19)
    class Meta:
        model = Vote
        fields = '__all__'
        

        

