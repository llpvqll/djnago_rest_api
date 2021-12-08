from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100, blank=True)
    total_experience = models.IntegerField()
    start = models.DateField(null=True)
    end = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['total_experience']



