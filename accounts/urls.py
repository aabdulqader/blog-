
from django.urls import path
from .views import UserSighupView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfileView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', UserSighupView.as_view(), name='signup'),
    path('settings/', UserEditView.as_view(), name='settings'),
    #path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),   
    path('password_success/', views.passwordsChangeDoneView, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = 'show_profile' ),
    path('<int:pk>/edit_profile/', EditProfileView.as_view(), name = 'edit_profile' ),
    path('<int:pk>/my_account/', views.MyAccountView, name = 'my_account' ),
    path('create_profile_page/', CreateProfilePageView.as_view(), name = 'create_profile_page' ),




]
