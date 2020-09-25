from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee 

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'

class EmployeeFormLogin(forms.Form):    
    username = forms.CharField(
        label='Enter Your User Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your User Name'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Password'
            }
        )
    )

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
