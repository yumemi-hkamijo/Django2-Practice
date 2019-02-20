from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    #403エラー画面を表示する場合はコメントアウト消す
    #raise_exception = True
