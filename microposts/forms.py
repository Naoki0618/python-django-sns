from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Message


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 5, 'cols': 30,
                       'placeholder': 'ここに入力してください'}
            ),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 5, 'cols': 30}
            ),
        }


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'comment',
        )
        widgets = {
            'comment': forms.Textarea(
                attrs={'rows': 1, 'cols': 30,
                       'placeholder': 'ここに入力してください'}
            ),
        }
