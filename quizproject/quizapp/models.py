from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)


