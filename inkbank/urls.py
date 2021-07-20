from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from inkbank.core.views import index


urlpatterns = [
    path("", index, name="index"),
    path("restricted/", admin.site.urls),
    path("admin/", RedirectView.as_view(url="https://www.djangoproject.com")),
]
