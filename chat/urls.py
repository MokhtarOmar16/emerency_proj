from .views import ChatListView , ChatMessagesDetailView

from django.urls import path

urlpatterns = [
    path('', ChatListView.as_view(), name='chat-list'),
    path('messages/', ChatMessagesDetailView.as_view(), name='messages-list'),
    
]