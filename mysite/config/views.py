from django.contrib.auth.models import User
from django.views.generic import TemplateView, RedirectView

class IndexView(TemplateView):
    template_name = 'index.html'
    url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user_count'] = User.objects.all().count()
        return context


index = IndexView.as_view()