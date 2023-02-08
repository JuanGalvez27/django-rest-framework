from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("questions/", views.QuestionsAPIView.as_view(), name="questions"),
    path("choices/", views.ChoicesAPIView.as_view(), name="choices"),
    path("<int:pk>/", views.QuestionAPIView.as_view(), name="question"),
    path("<int:pk>/", views.ChoiceAPIView.as_view(), name="choice"),
    path(
        "create-question/",
        views.CreateQuestionAPIView.as_view(),
        name="create-questions",
    ),
    path("create-choice/", views.CreateChoiceAPIView.as_view(), name="create-choice"),
    path(
        "<int:pk>/update-question/",
        views.UpdateQuestionAPIView.as_view(),
        name="update-question",
    ),
    path(
        "<int:pk>/update-choice/",
        views.UpdateChoiceAPIView.as_view(),
        name="update-choice",
    ),
    path(
        "<int:pk>/delete-question/",
        views.DeleteQuestionAPIView.as_view(),
        name="delete-question",
    ),
    path(
        "<int:pk>/delete-choice/",
        views.DeleteChoiceAPIView.as_view(),
        name="delete-choice",
    ),
]
