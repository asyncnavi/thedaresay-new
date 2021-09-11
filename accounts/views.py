from django.shortcuts import render

# Create your views here.
def login_view(request):

    return render(request,'accounts/login.html')

def signup_view(request):

    return render(request, 'accounts/signup.html')


def forgot_password_view(request):

    return render(request, 'accounts/forgot.html')