from django.urls import path

from .views import (
    register_student,
    login_student,
    save_result,
)

urlpatterns = [

    path(
        'register/',
        register_student,
    ),

    path(
        'login/',
        login_student,
    ),

    path(
        'save-result/',
        save_result,
    ),
]