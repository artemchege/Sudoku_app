from django.db import models
from django.utils import timezone


class Matrix(models.Model):
    array = models.JSONField()
    user = models.TextField(max_length=50, default=None)
    if_solved = models.BooleanField(default=None, null=True)
    result = models.JSONField(null=True)
    date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f'Matrix with id{self.id}'


