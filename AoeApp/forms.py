from django.forms import ModelForm
from .models import Sign_up, Free_Quotation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Sign_up_form(ModelForm):
    class Meta:
        model = Sign_up
        fields = '__all__'
    
class Free_Quotation_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Free_Quotation_form, self).__init__(*args, **kwargs)
        
        self.fields['Name'].widget.attrs.update(
            {'placeholder': 'Name',})
        self.fields['Address'].widget.attrs.update(
            {'placeholder': 'Address',})
        self.fields['Email'].widget.attrs.update(
            {'placeholder': 'Email',})
        self.fields['Contact'].widget.attrs.update(
            {'placeholder': '09*****',})
        self.fields['Date'].widget.attrs.update(
            {'placeholder': 'DD-MM-YY',})
        self.fields['Details'].widget.attrs.update(
            {'placeholder': 'Details.....',})

    class Meta:
        model = Free_Quotation
        fields = ['Name', 'Address', 'Email', 'Contact', 'Date', 'Details', 'Quantity', 'File' ] 
        
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class StatusForm(ModelForm):
	class Meta:
		model = Free_Quotation
		fields = ['status']


