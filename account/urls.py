from django.urls import path
from .views import Userregistration,LoginView,UserProfileView,Userchangepassword


urlpatterns = [
    path('register/',Userregistration.as_view(),name="register"),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',Userchangepassword.as_view(),name="changepassword")
]
