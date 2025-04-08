from rest_framework import serializers
from .models import Question, Answer, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'author', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['id', 'body', 'author', 'question', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'answer']