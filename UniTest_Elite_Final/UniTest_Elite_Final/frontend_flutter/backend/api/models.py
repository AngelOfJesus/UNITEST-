from django.db import models


class Student(models.Model):

    full_name = models.CharField(max_length=255)

    national_id = models.CharField(
        max_length=50,
        unique=True,
    )

    email = models.EmailField(unique=True)

    career = models.CharField(max_length=255)

    password = models.CharField(max_length=255)

    exam_completed = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.full_name


class ExamResult(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )

    score = models.IntegerField()

    total_questions = models.IntegerField()

    percentage = models.FloatField()

    passed = models.BooleanField()

    completed_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.student.full_name} - {self.percentage}%'