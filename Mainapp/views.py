from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import (
    View,
    ListView,
    CreateView,
    TemplateView,
    FormView
)

#Imports Locals
from .forms import (
    RegisterForm, 
    LoginForm, 
    UpdatePasswordsForm)



# -----------------------------------------------------------


class Index (TemplateView):
    template_name = 'mainapp/index.html'
    


# -----------------------------------------------------------


class Register_User (CreateView):
    model = User
    template_name = 'Mainapp/user/register.html'
    form_class = RegisterForm
    success_url = '/inicio'


# -----------------------------------------------------------


class LoginUser(FormView):
    template_name = 'mainapp/user/login.html'
    form_class = LoginForm
    success_url = '/blog'

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


# -----------------------------------------------------------


class UpdatePasswordsView(LoginRequiredMixin, FormView):
    template_name = 'mainapp/user/update_password.html'
    form_class = UpdatePasswordsForm
    success_url = '/login'
    login_url = 'Login'
    

    def form_valid(self, form):

        user = self.request.user
        user = authenticate(
            username=user.username,
            password=form.cleaned_data['password1']
            )

        if user:
            new_password = form.cleaned_data['password2']
            user.set_password(new_password)
            user.save()

        logout(self.request)
        
        return super(UpdatePasswordsView, self).form_valid(form)


# -----------------------------------------------------------


class LogoutUser(LoginRequiredMixin, View):
    login_url = 'Login'

    def get(self,request, *args,**kwargs):
        messages.success(self.request, 'Adios!!')

        logout(request)
        return redirect('/inicio')
