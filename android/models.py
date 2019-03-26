from django.db import models

# Create your models here.
class AndroidUser(models.Model):

    name = models.CharField(max_length=50, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name