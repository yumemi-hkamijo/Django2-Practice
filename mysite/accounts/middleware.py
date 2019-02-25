from django.core.exceptions import PermissionDenied
from django.urls import reverse

class SitePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        has_site_permission = False
        if request.user.is_superuser or request.user.is_staff:
            has_site_permission = True

        admin_index = reverse('admin:index')
        if request.path.startswith(admin_index):
            if not has_site_permission:
                raise PermissionDenied

        request.user.has_site_permission = has_site_permission