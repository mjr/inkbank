from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from inkbank.accounts.views import new, detail, credit, debit, transfer, earn_interest
from inkbank.core.views import index


urlpatterns = [
    path("", index, name="index"),
    path("new/", new, name="new"),
    path("detail/", detail, name="detail"),
    path("credit/", credit, name="credit"),
    path("debit/", debit, name="debit"),
    path("transfer/", transfer, name="transfer"),
    path("earn-interest/", earn_interest, name="earn-interest"),
    path("restricted/", admin.site.urls),
    path("admin/", RedirectView.as_view(url="https://www.djangoproject.com")),
]
