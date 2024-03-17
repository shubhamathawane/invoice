from django.db import models


# Create your models here.
class Invoice(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    CustomerName = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.CustomerName


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice"
    )
    description = models.CharField(max_length=512)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f' {self.pk} of {self.invoice}'