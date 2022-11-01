from django.urls import path
from .views import (
    PostCreateView, PostListView,  # 追加
    PostUpdateView, PostDeleteView, PostDetailView,
    MyPostsView  # 追加
)
from . import views
app_name = 'microposts'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('postlist/', PostListView.as_view(), name='postlist'),  # 追加
    path('postlist/<int:pk>', PostDetailView.as_view(),
         name='postdetail'),  # 追加
    path('postlist/<int:pk>',
         PostDetailView.as_view(), name='createcomment'),  # 追加
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),  # 追加
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),  # 追加
    path('myposts/', MyPostsView.as_view(), name='myposts'),  # 追加

]
