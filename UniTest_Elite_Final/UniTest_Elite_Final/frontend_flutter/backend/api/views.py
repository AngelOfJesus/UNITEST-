from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Student, ExamResult

from .serializers import (
    StudentSerializer,
    ExamResultSerializer,
)


@api_view(['POST'])
def register_student(request):

    try:

        email = request.data.get('email')

        national_id = request.data.get(
            'national_id'
        )

        # VALIDAR EXISTENTE
        if Student.objects.filter(
            email=email
        ).exists():

            return Response({

                'success': False,

                'message':
                'El correo ya existe',
            })

        if Student.objects.filter(
            national_id=national_id
        ).exists():

            return Response({

                'success': False,

                'message':
                'La cédula ya existe',
            })

        serializer = StudentSerializer(
            data=request.data,
        )

        if serializer.is_valid():

            serializer.save()

            return Response({

                'success': True,

                'message':
                'Usuario registrado correctamente',
            })

        return Response({

            'success': False,

            'errors': serializer.errors,
        })

    except Exception as e:

        return Response({

            'success': False,

            'message': str(e),
        })


@api_view(['POST'])
def login_student(request):

    try:

        email = request.data.get('email')

        password = request.data.get(
            'password'
        )

        student = Student.objects.get(

            email=email,

            password=password,
        )

        return Response({

            'success': True,

            'student_id': student.id,

            'full_name':
            student.full_name,

            'career':
            student.career,

            'exam_completed':
            student.exam_completed,
        })

    except Student.DoesNotExist:

        return Response({

            'success': False,

            'message':
            'Credenciales incorrectas',
        })

    except Exception as e:

        return Response({

            'success': False,

            'message': str(e),
        })


@api_view(['POST'])
def save_result(request):

    try:

        student_id = request.data.get(
            'student_id',
        )

        score = int(
            request.data.get('score')
        )

        total_questions = int(
            request.data.get(
                'total_questions'
            )
        )

        percentage = (
            score / total_questions
        ) * 100

        passed = percentage >= 70

        student = Student.objects.get(
            id=student_id,
        )

        if student.exam_completed:

            return Response({

                'success': False,

                'message':
                'El examen ya fue realizado',
            })

        ExamResult.objects.create(

            student=student,

            score=score,

            total_questions=
            total_questions,

            percentage=percentage,

            passed=passed,
        )

        student.exam_completed = True

        student.save()

        return Response({

            'success': True,

            'percentage': percentage,

            'passed': passed,
        })

    except Exception as e:

        return Response({

            'success': False,

            'message': str(e),
        })