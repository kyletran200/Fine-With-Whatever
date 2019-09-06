from rest_framework import serializers
from .models import Question

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessesPage
        fields = ('id', 'question_text', 'description')
