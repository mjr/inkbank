from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, resolve_url as r

from .models import Account
from .forms import NewAccountForm, SearchAccountForm


def new(request):
    if request.method == "POST":
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, "accounts/account_form.html", {"form": NewAccountForm()})


def create(request):
    form = NewAccountForm(request.POST)

    if not form.is_valid():
        return render(request, "accounts/account_form.html", {"form": form})

    form.save()
    messages.success(request, ("Conta cadastrada com sucesso!"))
    return redirect(r("index"))


def detail(request):
    if request.method == "POST":
        return get_account(request)

    return search_form(request)


def search_form(request):
    return render(request, "accounts/account_search.html", {"form": SearchAccountForm()})


def get_account(request):
    account = get_object_or_404(Account, number=request.POST.get("number"))
    return render(request, "accounts/account_detail.html", {"account": account})
