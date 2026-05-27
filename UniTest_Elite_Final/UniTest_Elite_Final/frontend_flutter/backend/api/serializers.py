from rest_framework import serializers

from .models import Student, ExamResult


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = '__all__'


class ExamResultSerializer(serializers.ModelSerializer):

    class Meta:

        model = ExamResult

        fields = '__all__'