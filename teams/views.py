from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from django.http import Http404


class TeamView(APIView):
    def post(self, request):
        try:
            team_data = request.data
            data_processing(team_data)
            team = Team.objects.create(
                name=team_data["name"],
                titles=team_data["titles"],
                top_scorer=team_data["top_scorer"],
                fifa_code=team_data["fifa_code"],
                first_cup=team_data["first_cup"],
            )

            return Response(model_to_dict(team), status=201)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"Error": str(err)}, status=400)

    def get(self, request):
        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]
        return Response(teams_dict)

    def get(self, request, pk=None):
        if pk is not None:
            try:
                team = Team.objects.get(pk=pk)
                team_dict = model_to_dict(team)
                return Response(team_dict, status=200)
            except Team.DoesNotExist:
                raise Http404("Team does not exist")

        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]
        return Response(teams_dict)

    def patch(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            data = request.data

            for field, value in data.items():
                setattr(team, field, value)

            team.save()

            return Response(model_to_dict(team), status=200)
        except Team.DoesNotExist:
            raise Http404("Team does not exist")

    def delete(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            team.delete()
            return Response(status=204)
        except Team.DoesNotExist:
            raise Http404("Team does not exist")
