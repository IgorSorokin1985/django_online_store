from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserForm, LoginForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import redirect
import random

# Create your views here.


class LoginView(BaseLoginView):
    #form_class = LoginForm
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Congratulations',
            message='You registered',
            from_email=EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm


    def get_object(self, queryset=None):
        return self.request.user

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
            send_mail(
                subject='New password',
                message=f'Your new password {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            user.set_password(new_password)
            user.save()
            return redirect(reverse('users:login'))
        except Exception:
            message = 'We can not find user with this email'
            contex = {
                'message': message
            }
            return render(request, 'users/forgot_password.html', contex)
    else:
        return render(request, 'users/forgot_password.html')
