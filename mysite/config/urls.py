from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path(r'^$', TemplateView.as_view(tempalte_name='index.html'), name='index'),
    path(r'^$', RedirectView.as_view(url='accounts/login/'), name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)