from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from polls.models import Question, Choice


User = get_user_model()

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = Choice
        fields = "__all__"

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ("username",)