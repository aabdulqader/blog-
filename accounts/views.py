from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm



class UserSighupView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_success')




def passwordsChangeDoneView(request):
    return render(request, 'registration/success_password.html')

'''   
class passwordsChangeDoneView(PasswordChangeDoneView):
    success_url = reverse_lazy('password_success')
'''
