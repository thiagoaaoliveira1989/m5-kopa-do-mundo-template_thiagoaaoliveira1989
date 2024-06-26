from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(null=True, default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(unique=True, max_length=3)
    first_cup = models.DateField(null=True)

    def __repr__(self):
        return f"<[{self.pk}] {self.name} - {self.fifa_code}>"
