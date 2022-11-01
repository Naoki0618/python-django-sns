from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView # 追加
from django.views.generic.base import TemplateView
from .forms import RegistForm, LoginForm , ProfileForm  # 追加
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView # 追加
from django.contrib.auth.mixins import LoginRequiredMixin # 追加
from .models import User # 追加



class HomeView(TemplateView):
   template_name = 'accounts/home.html'

class RegistUserView(CreateView):
   template_name = 'accounts/regist.html'
   form_class = RegistForm
   
class UserLoginView(LoginView):  # 追加
   template_name = 'accounts/login.html'
   authentication_form = LoginForm
       
class UserLogoutView(LogoutView): # 追加
   pass

   
class ProfileEditView(LoginRequiredMixin, UpdateView): # 追加
   template_name = 'accounts/edit_profile.html'
   model = User
   form_class = ProfileForm
   success_url = '/accounts/edit_profile/'
   def get_object(self):
       return self.request.user

class UserListView(LoginRequiredMixin, ListView): # 追加
   template_name = 'accounts/userlist.html'
   model = User
      
   def get_queryset(self):       
       return User.objects.all()
       