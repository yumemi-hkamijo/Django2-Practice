from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse
from django.views import View

from .forms import LoginForm

# Create your views here.
class LoginView(AuthLoginView):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        """GETリクエスト"""
        context = {
            'form': LoginForm(),
        }

        # ログイン画面のテンプレートに空のフォームをレンダリング
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト"""
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        user = form.get_user()

        auth_login(request, user)

        return redirect(reverse('shop:index'))

login = LoginView.as_view()