from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    total_score = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = '__all__'
