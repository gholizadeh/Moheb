from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm

def home(request):
    return render(request, 'pages/home.html')

class CustomAdminLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'admin/login.html'  # Specify your custom login template