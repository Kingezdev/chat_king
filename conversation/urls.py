
from django.urls import path
from .views import CreateConversationView, CreateMessage, DeleteConversation, ListConversation, GetConversationMessages


urlpatterns = [
    path("newconversation/", CreateConversationView.as_view()),
    path("listconversation/", ListConversation.as_view()),
    path("message/", CreateMessage.as_view()),
    path("conversation/<int:pk>/", GetConversationMessages.as_view()),
    path("deleteconversation/<int:pk>/", DeleteConversation.as_view())
]