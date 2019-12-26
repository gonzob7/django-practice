from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.Charfield(max_length=200)
    pub_date = models.DateTimeField('date published')
