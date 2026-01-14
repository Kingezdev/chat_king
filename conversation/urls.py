
from django.urls import path
from .views import CreateConversationView, CreateMessage, DeleteConversation


urlpatterns = [
    path("newconversation/", CreateConversationView.as_view()),
    path("message/", CreateMessage.as_view()),
    path("deleteconversation/<int:pk>/", DeleteConversation.as_view())
]