from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from polls.models import Question, Choice
from .serializers import (
    ChoiceSerializer,
    QuestionSerializer,
)


class QuestionsAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    authentication_class = (TokenAuthentication,)


class ChoicesAPIView(generics.ListAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)


class QuestionAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ChoiceAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class CreateQuestionAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = QuestionSerializer


class CreateChoiceAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = ChoiceSerializer


class UpdateQuestionAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = QuestionSerializer


class UpdateChoiceAPIView(generics.UpdateAPIView):
    queryset = Choice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = ChoiceSerializer


class DeleteQuestionAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = QuestionSerializer


class DeleteChoiceAPIView(generics.DestroyAPIView):
    queryset = Choice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication,)
    serializer_class = ChoiceSerializer
