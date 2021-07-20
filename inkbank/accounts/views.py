from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, resolve_url as r

from .models import Account
from .forms import NewAccountForm, SearchAccountForm, SimpleOperationAccountForm


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


def credit(request):
    if request.method == "POST":
        return add_credit(request)

    return credit_form(request)


def credit_form(request):
    return render(
        request, "accounts/account_credit.html", {"form": SimpleOperationAccountForm()}
    )


def add_credit(request):
    form = SimpleOperationAccountForm(request.POST)

    if not form.is_valid():
        return render(request, "accounts/account_credit.html", {"form": form})

    account = get_object_or_404(Account, number=form.cleaned_data["number"])
    account.balance += form.cleaned_data["value"]
    account.save()
    messages.success(request, (f"Crédito adicionado à conta #{account.number}!"))
    return redirect(r("index"))


def debit(request):
    if request.method == "POST":
        return add_debit(request)

    return debit_form(request)


def debit_form(request):
    return render(
        request, "accounts/account_debit.html", {"form": SimpleOperationAccountForm()}
    )


def add_debit(request):
    form = SimpleOperationAccountForm(request.POST)

    if not form.is_valid():
        return render(request, "accounts/account_debit.html", {"form": form})

    account = get_object_or_404(Account, number=form.cleaned_data["number"])
    account.balance -= form.cleaned_data["value"]
    account.save()
    messages.success(request, (f"Valor debitado da conta #{account.number}!"))
    return redirect(r("index"))
