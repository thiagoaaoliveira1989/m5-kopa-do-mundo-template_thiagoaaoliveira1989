from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)
    titles = models.IntegerField(default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3)
    fifa_cup = models.DateField(null=True, blank=True)

    def __repr__(self):
        return f"<[{self.pk}] {self.name} - {self.fifa_code}>"
