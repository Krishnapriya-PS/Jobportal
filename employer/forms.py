from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"
        widgets={
            'job_title':forms.TextInput(attrs={'class':'form-control','size':10}),
            'company_name': forms.TextInput(attrs={'class': 'form-control','size':10}),
            'location': forms.TextInput(attrs={'class': 'form-control','size':10}),
            'salary': forms.NumberInput(attrs={'class': 'form-control','size':10}),
            'experience': forms.NumberInput(attrs={'class': 'form-control','size':10})

        }

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())





