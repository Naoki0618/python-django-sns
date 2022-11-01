from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Favorite, Post, Message
from .forms import PostCreateForm, PostUpdateForm, MessageCreateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'microposts/create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('microposts:create')

    def form_valid(self, form):
        # formに問題なければ、owner id に自分のUser idを割り当てる
        # request.userが一つのセットでAuthenticationMiddlewareでセットされている。
        form.instance.owner_id = self.request.user.id
        messages.success(self.request, '投稿が完了しました')
        return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('microposts:create')


class PostListView(LoginRequiredMixin, ListView):
    # テンプレートを指定
    template_name = 'microposts/postlist.html'
    # 利用するモデルを指定
    model = Post
    # ページネーションの表示件数
    paginate_by = 10
    # Postsテーブルの全データを取得するメソッド定義
    # テンプレートでは、object_listとしてreturnの値が渡される

    def get_queryset(self):
        return Post.objects.all()


class PostDetailView(LoginRequiredMixin, TemplateView):
    # テンプレートを指定
    template_name = 'microposts/postdetail.html'
    form_class = MessageCreateForm

    def get_context_data(self, **kwargs):

        try:
            comments = Message.objects.filter(post_id=self.kwargs['pk'])
        except:
            comments = []
        try:
            favorites = Favorite.objects.filter(post_id=self.kwargs['pk'])
        except:
            favorites = []
        try:
            favorites_owner = Favorite.objects.filter(post_id=self.kwargs['pk'], user_name = self.request.user)
        except:
            favorites_owner = []
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['owner'] = post.owner
        context['post'] = post
        context['form'] = self.form_class
        context['comments'] = comments
        context['favorites'] = favorites
        context['favorites_owner'] = False
        for fa in favorites_owner:
            if fa.user_name.username == self.request.user.username:
                context['favorites_owner'] = True
        context['authenticated'] = self.request.user.is_authenticated

        return context

    def post(self, request, pk):
        form = MessageCreateForm(request.POST or None)
        if "favorite" in request.POST:
            favorite_list = Favorite.objects.filter(post_id=self.kwargs['pk'], user_name_id=request.user.id )
            if not favorite_list :
                print("list is empty")
                Favorite.objects.create(
                    post_id_id=pk, user_name_id=request.user.id )
            else :
                print("list is not empty")            
                favorite_list.delete()
                
        else:
            Message.objects.create(
                post_id_id=pk, user_name_id=request.user.id, comment=form.data['comment'])

        return redirect('microposts:postdetail', pk)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'microposts/update.html'

    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')
        return super(PostUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('microposts:update', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return reverse_lazy('microposts:update', kwargs={'pk': self.object.id})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'microposts/delete.html'
    # deleteviewでは、SuccessMessageMixinが使われないので設定する必要あり
    success_url = reverse_lazy('microposts:create')
    success_message = "投稿は削除されました。"
    # 削除された際にメッセージが表示されるようにする。

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


class MyPostsView(LoginRequiredMixin, ListView):  # 追加
    # テンプレートを指定
    template_name = 'microposts/myposts.html'
    # 利用するモデルを指定
    model = Post
    # ページネーションの表示件数
    paginate_by = 10

    # Postsテーブルのowner_idが自分自身の全データを取得するメソッド定義
    def get_queryset(self):  # 自分の投稿オブジェクトを返す。
        return Post.objects.filter(owner_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Postsテーブルの自分の投稿数をmy_posts_countへ格納
        context['my_posts_count'] = Post.objects.filter(
            owner_id=self.request.user).count()
        return context
