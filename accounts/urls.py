
from django.urls import path
from .views import UserSighupView

urlpatterns = [
    path('signup/', UserSighupView.as_view(), name='signup'),
]
