from .views import ChatListView

from django.urls import path

urlpatterns = [
    path('', ChatListView.as_view(), name='chat-list'),
]