from django.db import models

class Question(models.Model):
    slug = models.SlugField()
    content = models.CharField(max_length= 1024)
    def __str__(self):
        return self.content

class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    def __str__(self):
        return "{} - {}".format(self.question.content[:50], self.content)

# Create your models here.
