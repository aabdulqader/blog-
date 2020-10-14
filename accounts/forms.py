from django.contrib.auth.forms import UserCreationForm
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