from django.db import models

# Create your models here.
class Questions(models.Model):
      question=models.TextField()
      option1=models.CharField(max_length=100)
      option2=models.CharField(max_length=100)
      option3=models.CharField(max_length=100)
      option4=models.CharField(max_length=100)
      answer=models.CharField(max_length=100)
class MATQuestions(models.Model):
      question=models.TextField()
      option1=models.CharField(max_length=100)
      option2=models.CharField(max_length=100)
      option3=models.CharField(max_length=100)
      option4=models.CharField(max_length=100)
      answer=models.CharField(max_length=100)
class GKQuestions(models.Model):
      question=models.TextField()
      option1=models.CharField(max_length=100)
      option2=models.CharField(max_length=100)
      option3=models.CharField(max_length=100)
      option4=models.CharField(max_length=100)
      answer=models.CharField(max_length=100)

