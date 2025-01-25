from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer,OpenApiExample
from rest_framework import serializers
from .serializers import MessageSerializer
from drf_spectacular_websocket.decorators import extend_ws_schema

Custom_admin_consumer = extend_ws_schema(
    description="This Endpoint is protected . \n you have to send a `jwt` as a `parameter` in the url",
    type='send',
    summary='sending message',
)

custom_chat_list_schema = extend_schema(
    description="This Endpoint is protected . \n you should be an `admin`",
)



custom_chat_messages_list_schema = extend_schema(
    description="This Endpoint is protected , <br> You should be A `user`",
    responses=MessageSerializer
)
