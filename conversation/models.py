from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


class Conversation(models.Model):
    user= models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="conversations"
    )

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else f"conversation #{self.id}"
    
class Chat(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="chat"
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="chats"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.message or f"chat {self.id}"


