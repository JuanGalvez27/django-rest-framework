from rest_framework import status, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from polls.models import Question, Choice
from .serializers import (
    ChoiceSerializer,
    QuestionSerializer,
    UserTokenSerializer,
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


class Login(ObtainAuthToken):

    def post(self, request, *args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            token,created = Token.objects.get_or_create(user = user)
            user_serializer = UserTokenSerializer(user)
            if created:
                return Response({
                    'token': token.key,
                    'user': user_serializer.data, #You must to serialize the user
                    'message': "Successful login "   
                    }, status= status.HTTP_201_CREATED)
            else:
                token.delete()
                token = Token.objects.create(user = user)
                return Response({
                    'token': token.key,
                    'user': user_serializer.data, #You must to serialize the user
                    'message': "Successful login "   
                    }, status= status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Username or passord non valid'},
                            status=status.HTTP_401_UNAUTHORIZED)