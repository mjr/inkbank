from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models, transaction


class Account(models.Model):
    SIMPLE = "SI"

    KINDS = ((SIMPLE, "Conta simples"),)

    number = models.PositiveIntegerField(
        "número", unique=True, validators=[MinValueValidator(10000)]
    )
    balance = models.DecimalField("saldo", max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField("criada em", auto_now_add=True)
    kind = models.CharField("tipo", max_length=2, choices=KINDS, default=SIMPLE)

    class Meta:
        verbose_name_plural = "contas"
        verbose_name = "conta"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.number}"

    def clean(self):
        if self.kind == Account.SIMPLE:
            pass

        else:
            assert False, f'Unknown account type "{self.kind}"'

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def deposit(self, value):
        if value <= 0:
            raise ValidationError("O valor tem que ser maior que 0.")

        self.balance += value
        self.save()

    def withdraw(self, value):
        if value <= 0:
            raise ValidationError("O valor tem que ser maior que 0.")

        self.balance -= value
        self.save()

    def transfer(self, receiver, value):
        if value <= 0:
            raise ValidationError("O valor tem que ser maior que 0.")

        if self.balance < value:
            raise ValidationError(
                f"O remetente não tem esse valor para transferir. Saldo do remetente: R$ {self.balance}"
            )

        with transaction.atomic():
            self.balance -= value
            receiver.balance += value

            self.save()
            receiver.save()
