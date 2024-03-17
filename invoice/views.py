from django.shortcuts import render
from .models import InvoiceDetail, Invoice
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.


class InvoiceUsersView(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class InvoiceUserDetailView(APIView):

    def get(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
            serializer = InvoiceSerializer(invoice, many=False)
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return Response(
                {"message": "No Invoices Found!"}, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
            serializer = InvoiceSerializer(invoice, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)

        except Invoice.DoesNotExist:
            return Response(
                {"message": "No Invoices Found!"}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
            if invoice:
                invoice.delete()
                return Response(
                    {"message": "Deleted Successfully"},
                    status=status.HTTP_204_NO_CONTENT,
                )
        except:
            return Response(
                {"message": "No Invoices Found!"}, status=status.HTTP_400_BAD_REQUEST
            )


class InvoiceDetailsView(APIView):

    def get(self, request):

        user = request.GET.get("name", "")
        userid = request.GET.get("id", "")

        detailed_invoices = InvoiceDetail.objects.all()

        if user:
            detailed_invoices = detailed_invoices.filter(
                Q(CustomerName__icontains=user)
            )

        if userid:
            detailed_invoices = detailed_invoices.filter(invoice=userid)

        serializer = InvoiceDetailSerializer(detailed_invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Added Successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Error", "Error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SingleInvoiceDetailView(APIView):

    def get(self, request, pk):
        try:
            invoice = InvoiceDetail.objects.get(pk=pk)
            serializer = InvoiceDetailSerializer(invoice, many=False)
            return Response(serializer.data)
        except InvoiceDetail.DoesNotExist as e:
            return Response({"message": "Does not exist!"})

    def put(self, request, pk):

        invoice = InvoiceDetail.objects.get(pk=pk)
        serializer = InvoiceDetailSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            invoice = InvoiceDetail.objects.get(pk=pk)
            if invoice:
                invoice.delete()
                return Response(
                    {"message": "Deleted Successfully"},
                    status=status.HTTP_204_NO_CONTENT,
                )
        except:
            return Response(
                {"message": "No Invoices Found!"}, status=status.HTTP_400_BAD_REQUEST
            )
