from rest_framework import serializers
from .model import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fieldes = '__all__'