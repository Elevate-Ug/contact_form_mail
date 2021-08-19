from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class SignupPageView(SuccessMessageMixin, generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'
    success_message = "Account was created successfully"
