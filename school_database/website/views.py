from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import RegisterForm, LoginForm
from .decorators import admin_only, student_only, staff_only, editor_only


def home(request):
    return render(request, 'index.html')


def register(request):
    form = RegisterForm()
    counter = 0
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            counter += form.cleaned_data.get('admin')
            counter += form.cleaned_data.get('student')
            counter += form.cleaned_data.get('staff')
            counter += form.cleaned_data.get('editor')
            if counter == 0:
                messages.error(request, "You must choose a role!")
                return redirect('website:register')
            elif counter > 1:
                messages.error(request, "You can choose only one role!")
                return redirect('website:register')
            else:
                form.save()
                messages.success(
                    request, "Your account has been successfully created.")
                return redirect('website:log_in')

    return render(request, 'register.html', {'form': form})


def log_in(request):
    form = LoginForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.get(email=email)
            print(email)
            print(password)

            if user.check_password(password):
                if user.admin:
                    login(request, user)
                    return redirect("website:admin")
                elif user.student:
                    login(request, user)
                    return redirect("website:student")
                if user.staff:
                    login(request, user)
                    return redirect("website:staff")
                if user.editor:
                    login(request, user)
                    return redirect("website:editor")

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('website:log_in')

    return render(request, 'login.html', {'form': form})


@login_required(login_url='website:log_in')
@admin_only
def admin(request):
    return render(request, 'admin.html')


@login_required(login_url='website:log_in')
@student_only
def student(request):
    return render(request, 'student.html')


@login_required(login_url='website:log_in')
@staff_only
def staff(request):
    return render(request, 'staff.html')


@login_required(login_url='website:log_in')
@editor_only
def editor(request):
    return render(request, 'editor.html')


def log_out(request):
    logout(request)
    return redirect('website:home')
