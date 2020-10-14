
from django.urls import path
from .views import UserSighupView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', UserSighupView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),   
    path('password_success/', views.passwordsChangeDoneView, name='password_success'),
    #path('password_success/', passwordsChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_success'),
]
