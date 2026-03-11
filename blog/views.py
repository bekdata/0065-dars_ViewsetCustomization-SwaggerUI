# from django.shortcuts import render
# from rest_framework import viewsets, mixins
# from .models import Book
# from .serializers import BookSerializer
#
# # Create your views here.
#
# class BookViewSet(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   viewsets.GenericViewSet
#                   ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination


# 67-dars: Pagination sozlamasi
class SmallResultsPagination(PageNumberPagination):
    page_size = 5  # Har bir sahifada 5 tadan kitob chiqadi


class BookViewSet(mixins.ListModelMixin,  # Ko'rish
                  mixins.CreateModelMixin,  # Qo'shish
                  mixins.RetrieveModelMixin,  # Bitta elementni ko'rish
                  viewsets.GenericViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    pagination_class = SmallResultsPagination  # Pagination qo'shildi

    # 67-dars: Filter va Search qo'shish
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']  # Muallif bo'yicha filter
    search_fields = ['title', 'description']  # Nomi va tavsifi bo'yicha qidiruv
    ordering_fields = ['price', 'created_at']