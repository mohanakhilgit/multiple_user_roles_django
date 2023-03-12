from django.shortcuts import redirect, render
from django.contrib import messages


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.admin:
            return render(request, 'admin.html')
        else:
            messages.error(request, "Unauthorized Access! Kindly Login From an Admin Account to Access.")
            return redirect('website:home')
    return wrapper_func


def student_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.student:
            return render(request, 'student.html')
        else:
            messages.error(request, "Unauthorized Access! Kindly Login From a Student Account to Access.")
            return redirect('website:home')
    return wrapper_func


def staff_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.staff:
            return render(request, 'staff.html')
        else:
            messages.error(request, "Unauthorized Access! Kindly Login From a Staff Account to Access.")
            return redirect('website:home')
    return wrapper_func


def editor_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.editor:
            return render(request, 'editor.html')
        else:
            messages.error(request, "Unauthorized Access! Kindly Login From an Editor Account to Access.")
            return redirect('website:home')
    return wrapper_func
