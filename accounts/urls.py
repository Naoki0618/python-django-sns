from django.urls import path
from .views import (
   RegistUserView,HomeView,
   UserLoginView, UserLogoutView,
   ProfileEditView,UserListView, # 追加
)
app_name = 'accounts'
urlpatterns = [
   path('home/', HomeView.as_view(), name='home'),
   path('regist/', RegistUserView.as_view(), name='regist'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('logout/', UserLogoutView.as_view(), name='logout'),
   path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'), # 追加
   path('userlist/', UserListView.as_view(), name='userlist'), # 追加
]