from django.contrib.auth import authenticate
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_message(request):
    if request.method == 'POST':
        newMessage = Message()
        user = request.user.id
        newMessage.author = User.objects.get(id=user)
        message = MessageSerializer(instance=newMessage, data=request.data)

        if message.is_valid():
            message.save()
            return Response(message.data)
    return Response('error')

@permission_classes([IsAuthenticated])
@api_view(['PUT', 'PATCH'])
def update_Message(request, id):
    if request.method == 'PUT' or request.method == 'PATCH':
        message = Message.objects.get(id=id)
        user = request.user.id

        if message.author.id != user:
            return Response('Vous n\'êtes pas autorisé à mettre à jour ce message.')

        serializer = MessageSerializer(instance=message, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Erreur de validation des données')

    return Response('Méthode non autorisée')


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_Message(request,id):
    message = Message.objects.get(id=id)
    user = request.user.id

    if message and message.author.id == user:
        message.delete()
        return Response('message delete')

    return Response('Error')

