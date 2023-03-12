from django.urls import path
from.views import home, register, log_in, admin, student, staff, editor, log_out


app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('log-in/', log_in, name='log_in'),
    path('admin-page/', admin, name='admin'),
    path('student-page/', student, name='student'),
    path('staff-page/', staff, name='staff'),
    path('editor-page/', editor, name='editor'),
    path('log-out/', log_out, name='log_out'),
]
