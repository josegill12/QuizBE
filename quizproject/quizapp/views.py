from rest_framework import generics, status
from rest_framework.response import Response
from .models import Quiz, Question, Option, QuizAnswer, SavedQuestion
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer, SavedQuestionSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser

class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CreateQuestion(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        quiz_id = request.data.get('quiz')
        question_text = request.data.get('text')
        options_data = request.data.get('options', [])

        question = Question.objects.create(quiz_id=quiz_id, text=question_text)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)

        return Response({'status': 'success', 'question_id': question.pk}, status=status.HTTP_201_CREATED)
    
class OptionListCreate(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class QuizAnswerCreateView(generics.CreateAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = AnswerSerializer
    parser_classes = [JSONParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SaveQuestionAPIView(generics.CreateAPIView):
    queryset = SavedQuestion.objects.all()
    serializer_class = SavedQuestionSerializer

    def post(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        options_ids = request.data.get('options_ids', [])
        question = get_object_or_404(Question, pk=question_id)
        options = Option.objects.filter(id__in=options_ids)

        saved_question, created = SavedQuestion.objects.get_or_create(
            user=request.user,
            question=question
        )

        if created:
            saved_question.saved_options.set(options)
            saved_question.save()

        serializer = SavedQuestionSerializer(saved_question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)