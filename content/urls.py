from django.urls import path
from .views import projects_list_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", projects_list_view, name="projects_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)