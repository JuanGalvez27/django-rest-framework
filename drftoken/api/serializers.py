from rest_framework import serializers
from rest_framework.authtoken.models import Token
from polls.models import Question, Choice
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = Choice
        fields = "__all__"
