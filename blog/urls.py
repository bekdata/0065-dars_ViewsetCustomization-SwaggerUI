from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookWiewSet, BookViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]