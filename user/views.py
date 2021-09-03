from .forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class SignUp(View):
    def get(self, request):
        logger.info('Handling things over here please move')
        return render(request, 'user/signup.html', {'form': RegisterForm})

    def post(self, request):
        form = RegisterForm(request.POST)
        logger.info('Handling things over here please move')
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            return render(request, 'user/success.html')
        else:
            logger.info(form.error_messages)
            return render(
                request, 'user/signup.html', {'form': RegisterForm, 'sign_up_errors': form.error_messages})
