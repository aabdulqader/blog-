from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from home.models import Profile, Post

class CreateProfilePageView(CreateView):
    model = Profile
    fields_class = ProfilePageForm
    template_name = 'registration/create_user_profile_Page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)






class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user 
        return context



def MyAccountView(request, pk):
    posts = Post.objects.all()
    data = Profile.objects.all()
    context = {'posts':posts, 'data':data}
    return render(request,'registration/my_account.html', context )

class EditProfileView(generic.UpdateView):
    model = Profile
    fields = ['bio','profile_pic','website_url','facebook_url','linkedin_url','instagram_url','twitter_url']
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('my_account')



class UserSighupView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_success')




def passwordsChangeDoneView(request):
    return render(request, 'registration/success_password.html')
