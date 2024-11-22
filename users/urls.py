from django.urls import path
from .apis import UserMeViewSet,UserRegisterView, ChangePasswordView



urlpatterns = [
    
    path('users/me/', UserMeViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete':'destroy'}), name="users-me"),
    path('users/', UserRegisterView.as_view(), name='user'), 
    path('users/changepassword/', ChangePasswordView.as_view(), name='user-changepassword'), 

] 

