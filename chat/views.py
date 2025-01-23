from rest_framework.generics import ListAPIView 
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthenticatedAndNotAdmin
from .models import Chat, Message
from .serializers import ChatSerializer , MessageSerializer
class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAdminUser]


class ChatMessagesDetailView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedAndNotAdmin]
    def get_queryset(self):
        return super().get_queryset().filter(sender=self.request.user)
    