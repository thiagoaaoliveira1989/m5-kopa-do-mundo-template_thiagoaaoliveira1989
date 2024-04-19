from django.urls import path
from .views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:pk>", TeamView.as_view()),
]
