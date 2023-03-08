from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializers
from .models import Product


class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
