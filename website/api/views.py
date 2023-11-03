from django.contrib.auth import authenticate
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.api.serializers import MessageSerializer
from website.models import Message, Category, User


@api_view(['GET'])

def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)

@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)


@api_view(['POST'])
def create_message(request):
    if request.method == 'POST':
        newMessage = Message()
        newMessage.author = User.objects.get(id=1)

        message = MessageSerializer(instance=newMessage, data=request.data)

        if message.is_valid():
            message.save()
            return Response(message.data)
    return None

@api_view(['POST'])

def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return Response()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        return Response()

