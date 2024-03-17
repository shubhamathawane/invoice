from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):

    customer_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = InvoiceDetail
        fields = ['id', 'invoice', 'description', 'quantity', 'unit_price', 'price', 'customer_name']
    
    def get_customer_name(self, obj):
        invoices = obj.invoice
        customer_name = invoices.CustomerName
        print("invoices", invoices)
        return customer_name


class InvoiceSerializer(serializers.ModelSerializer):

    invoice_details = InvoiceDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Invoice
        fields = ['id', 'Date', 'CustomerName', 'invoice_details']
