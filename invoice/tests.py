from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail


class TestInvoiceViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'CustomerName': "shubham stanes3"
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)
    
    def test_get_invoices(self):
        res = self.client.get(reverse('invoice'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        new_payload = {
            'CustomerName': "Something Gaikwad"
        }
        res = self.client.post(reverse('invoice'), new_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Invoice.objects.filter(CustomerName='Something Gaikwad').exists())

    def test_get_invoice_detail(self):
        res = self.client.get(reverse('invoice_detail', kwargs={'pk': self.invoice.id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_update_invoice(self):
        updated_payload = {
            'CustomerName':"Shubham M. Athawane"
        }
        res = self.client.put(reverse('invoice_detail', kwargs={'pk': self.invoice.id}), updated_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.CustomerName, 'Shubham M. Athawane')
    
    def test_delete(self):
        res = self.client.delete(reverse('invoice_detail', kwargs={'pk': self.invoice.id}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice.objects.filter(pk=self.invoice.id).exists())


class TestInvoiceDetailViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(CustomerName='Test Customer')
        self.invoice_detail_data = {
            'invoice': self.invoice, 
            'description': 'Testing the description using python test',
            'quantity': 1, 
            'unit_price': 10, 
            'price': 10
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)
    
    def test_get_invoice_detail(self):
        res = self.client.get(reverse('invoice_user'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_invoice_detail(self):

        new_invoice_details_data = {
            'invoice': self.invoice.id, 
            'description': 'Testing the description using python test',
            'quantity': 1, 
            'unit_price': 10, 
            'price': 10
        }

        res = self.client.post(reverse('invoice_user'), new_invoice_details_data, formate='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.CustomerName, "Test Customer")


class TestSingleInvoiceDetailView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(CustomerName='Test Customer')
        self.invoice_detail_data = {
            'invoice': self.invoice, 
            'description': 'Testing the description using python test',
            'quantity': 1, 
            'unit_price': 10, 
            'price': 10
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)
    

    def test_get_single_invoice_detail(self):
        res = self.client.get(reverse('invoice_user', kwargs={'pk': self.invoice_detail.id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_update_single_invoice_detail(self):
        updated_invoice_detail_data = {
            'description': 'Testing the description using python test',
        }
        response = self.client.put(reverse('invoice_user', kwargs={'pk': self.invoice_detail.id}), updated_invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice_detail.description, 'Testing the description using python test')

    def test_delete_single_invoices_details(self):
        res = self.client.delete(reverse('invoice_user', kwargs={'pk': self.invoice_detail.id}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(InvoiceDetail.objects.filter(pk=self.invoice_detail.id).exists())
