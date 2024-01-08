from django.shortcuts import render
from django.db.models import Q
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def patch(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        product.is_favorite = not product.is_favorite
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

#class ToggleFavoriteBookView(APIView):
    def patch(self, request, product_id):
        try:
            book = Product.objects.get(pk=product_id)
            book.is_favorite = not book.is_favorite
            book.save()
            serializer = ProductSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Книга не найдена'}, status=status.HTTP_404_NOT_FOUND)
#class FavoriteProductsList(APIView):
    def get(self, request):
        favorite_products = Product.objects.filter(is_favorite=True)
        serializer = ProductSerializer(favorite_products, many=True)
        return Response(serializer.data)
