from django.urls import path
from .apis import *



urlpatterns = [
    path("auth/o/<str:provider>/",CustomProviderAuthView.as_view(),name="provider-auth",),
    path('users/me/', UserMeViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete':'destroy'}), name="users-me"),
    path('users/', UserRegisterView.as_view(), name='user'), 
    path('users/changepassword/', ChangePasswordView.as_view(), name='user-changepassword'), 
    path('users/request-reset-password/', RequestPasswordResetCodeView.as_view(), name='user-resetpassword'), 
    path('users/confirm-reset-password/', PasswordResetCodeView.as_view(), name='user-resetpasswordconfirm' ),
    path('google/', GoogleAuthView.as_view()),
    path('google/url/', CreateGoogleAuthLinkView.as_view()),
] 

