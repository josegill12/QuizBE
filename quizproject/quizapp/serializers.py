from rest_framework import serializers
from .models import Quiz, Question, Option, SavedQuestion


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'questions']

class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Quiz
        fields = ['id', 'user', 'questions', 'selected_option']
        read_only_fields = ('user',)

class SavedQuestionSerializer(serializers.ModelSerializer):
    # If you want to include details of the saved options, you can define a nested serializer
    saved_options = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text'  # Or any other field of the Option model you want to display
    )

    class Meta:
        model = SavedQuestion
        fields = ['id', 'user', 'question', 'saved_options', 'timestamp']
        read_only_fields = ('user', 'timestamp')