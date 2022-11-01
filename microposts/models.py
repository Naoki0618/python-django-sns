from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    # Postのオーナーを設定する
    owner = models.ForeignKey(
        'accounts.User', verbose_name='オーナー', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'


class Message(models.Model):
    id = models.BigAutoField(primary_key=True,)
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT,)
    comment = models.TextField(verbose_name='コメント')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post_id)


class Favorite(models.Model):
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT,)
    created_at = models.DateTimeField(auto_now_add=True)