from django.urls import path
from .views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view(), name="team-list"),
    path("teams/<int:pk>/", TeamView.as_view(), name="team-detail"),
]
