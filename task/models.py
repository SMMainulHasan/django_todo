from django.db import models


class TaskStoreModel(models.Model):
    task = models.CharField(max_length=50)
    detail = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
