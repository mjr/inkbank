from django.contrib import messages
from django.shortcuts import render, redirect, resolve_url as r

from .forms import NewAccountForm


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
