from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserForm, AuthenticationForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from users.utils import send_email_for_verify
import random

# Create your views here.


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            print(user)
            print(token_generator.check_token(user, token))
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('product_list')
        print(user)
        print(token_generator.check_token(user, token))
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user



class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_email_for_verify(self.request, new_user)
        #send_mail(
        #    subject='Congratulations',
        #    message='You registered',
        #    from_email=EMAIL_HOST_USER,
        #    recipient_list=[new_user.email]
        #)
        return super().form_valid(form)

    #def post(self, request):
    #    form = UserCreationForm(request.POST)
#
    #    if form.is_valid():
    #        form.save()
    #        email = form.cleaned_data.get('email')
    #        password = form.cleaned_data.get('password1')
    #        user = authenticate(email=email, password=password)
    #        send_email_for_verify(request, user)
    #        return redirect('confirm_email')
    #    context = {
    #        'form': form
    #    }
    #    return render(request, self.template_name, context)


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
