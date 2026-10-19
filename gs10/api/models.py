from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __Str__(self):
        return self.name

    # here we have developer one to many relationship where we can have multiple songs related to one singer 

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer , on_delete=models.CASCADE , related_name='sungby')
    duration = models.IntegerField()


    def __str__(self):
        return self.title
