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

class QuizAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz_answers', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='quiz_answers', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


class SavedQuestion(models.Model):
    user = models.ForeignKey('users.User', related_name='saved_questions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='saved_questions', on_delete=models.CASCADE)
    saved_options = models.ManyToManyField(Option, related_name='included_in_saved_questions')
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ['user', 'question']