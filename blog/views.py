from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet
                  ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer