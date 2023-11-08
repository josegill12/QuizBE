from rest_framework import generics
from rest_framework.response import Response
from .models import Quiz, Question, Option
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer
from django.shortcuts import render



class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CreateQuestion(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request):
        quiz_id = request.data.get('quiz')
        question_text = request.data.get('text')
        options_data = request.data.get('options', [])

        question = Question.objects.create(quiz_id=quiz_id, text=question_text)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)

        return Response({'status': 'success', 'question_id': question.id})
    
class OptionListCreate(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer




