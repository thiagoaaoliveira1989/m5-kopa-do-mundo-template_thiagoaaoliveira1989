from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


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

            return Response(model_to_dict(team), 201)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"Error ": str(err)}, status=400)

    def get(self, request):
        teams = Team.objects.all()

        teams_dic = []

        for team in teams:
            t = model_to_dict(team)
            teams_dic.append(t)

        return Response(teams_dic)
