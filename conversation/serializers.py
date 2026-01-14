
from rest_framework import serializers
from conversation.models import Conversation, Chat

class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = ["title", "created_at", "updated_at", "id"]
        read_only_fields = ["created_at", "updated_at", "id"]

    def create(self, validated_data):
        profile = self.context['request'].user.profile
        conversation = Conversation.objects.create(
            user = profile,
            **validated_data
        )
        return conversation
    
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["message", "created_at"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        profile = self.context["request"].user.profile
        conversation = self.context["conversation"]
        chat = Chat.objects.create(
            user = profile,
            conversation = conversation,
            **validated_data
        )
        return chat
