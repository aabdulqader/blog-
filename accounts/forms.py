from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Valid Email Address'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2' )


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['password1'].widget.attrs['placeholder']='**********'
        self.fields['password2'].widget.attrs['placeholder']='**********'


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active = forms.CharField(max_length=150, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-check'}))
    


    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password', 'last_login','is_active','date_joined' )


