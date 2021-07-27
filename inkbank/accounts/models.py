from django.core.validators import MinValueValidator
from django.db import models


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
