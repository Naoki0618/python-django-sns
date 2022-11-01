from django import forms
from .models import User
# from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm  # 追加


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザーネーム')
    email = forms.EmailField(label='E-mail アドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=False):
        user = super().save(commit=False)
        # validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(AuthenticationForm):  # 追加
    username = forms.CharField(label='ユーザーネーム')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():  # bootstrapで使用するform-controlクラス
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')
        help_texts = {
            'username': None,
            'email': None,
        }
