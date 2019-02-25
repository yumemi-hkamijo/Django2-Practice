from django import forms
from django.contrib.auth.forms import UsernameField

class LoginForm(form.Form):
    username = UsernameField(
        label="ユーザー名",
        max_length=255,
    )

    password = forms.CharField(
        label='パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True)
    )