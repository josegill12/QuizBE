from django.urls import path
from .views import QuizListCreate, QuizDetailUpdateDelete, CreateQuestion, QuizAnswerCreateView


urlpatterns = [
    path('', QuizListCreate.as_view(), name='quiz-list'),
    path('quizzes/', QuizListCreate.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizDetailUpdateDelete.as_view(), name='quiz-detail-update-delete'),
    path('quizzes/<int:pk>/questions/', CreateQuestion.as_view(), name='create-question'),
    path('submit-answer/', QuizAnswerCreateView.as_view(), name='submit-answer'),
    # path('saved-questions/', save_question(), name='saved-question-list'),
]
