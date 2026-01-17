
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ConversationSerializer, ChatSerializer
from rest_framework import status
from .models import Chat, Conversation

class CreateConversationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ConversationSerializer(
            data=request.data,
            context = {"request": request}

        )

        if serializer.is_valid():
            conversation = serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListConversation(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            conversations = Conversation.objects.all()
            serializer = ConversationSerializer(conversations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Error fetching conversations"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get_queryset(self):
        return Conversation.objects.all()

class DeleteConversation(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            conversation = Conversation.objects.get(pk = pk)
            conversation.delete()
            return Response({"message":  "Conversation Deleted"}, status=status.HTTP_200_OK)
        except Conversation.DoesNotExist:
            return Response({"message": "Conversation Not Found"}, status=status.HTTP_404_NOT_FOUND)
        


class CreateMessage(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        conversation_id = request.data.get("conversation_id")
        conversation = Conversation.objects.get(id=conversation_id)
        serializer = ChatSerializer(
            data = request.data,
            context = {
                "request": request,
                "conversation": conversation,
            }
        )

        if serializer.is_valid():
            chat = serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetConversationMessages(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            conversation = Conversation.objects.get(pk=pk)
            messages = Chat.objects.filter(conversation=conversation)
            serializer = ChatSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Conversation.DoesNotExist:
            return Response({"message": "Conversation Not Found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error fetching messages"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
