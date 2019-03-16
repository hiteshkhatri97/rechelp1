from company.models import CompanyLoginForm, CompanyCreationForm
from student.models import StudentLoginForm, StudentCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


def loginForm(request, user_type):

    form = StudentLoginForm() if user_type == 'student' else CompanyLoginForm()

    if request.method == 'POST':
        form = StudentLoginForm(
            data=request.POST) if user_type == 'student' else CompanyLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user and user.userType == user_type:
                # TODO: SEND A NICE MESSAGE IF SOMEONE TRIES TO LOGIN WITH CREDENTIALS OF DIFFERENT USER TYPE
                login(request, user)
        return redirect(user_type + ':home')
    return render(request, user_type + '/login.html', {'form': form})


def signupForm(request, user_type):

    form = StudentCreationForm() if user_type == 'student' else CompanyCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(
            request.POST) if user_type == 'student' else CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_type + ':profile')
    return render(request, user_type + '/signup.html', {'form': form})