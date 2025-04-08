from rest_framework import generics, permissions
from .models import Question, Answer, Like
from .serializers import QuestionSerializer, AnswerSerializer, LikeSerializer

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all().order_by('-created_at')
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)