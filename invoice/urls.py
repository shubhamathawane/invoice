from django.urls import path
from .views import InvoiceUserDetailView, InvoiceUsersView, InvoiceDetailsView, SingleInvoiceDetailView

urlpatterns = [
    path("invoices/", InvoiceUsersView.as_view(), name="invoice"),
    path("invoices/<int:pk>/", InvoiceUserDetailView.as_view(), name="invoice_detail"),
    path('invoice/details/', InvoiceDetailsView.as_view(), name='invoice_user' ),
    path('invoice/details/<int:pk>/', SingleInvoiceDetailView.as_view(), name='invoice_user')
]
