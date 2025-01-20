# store/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# Include the router URLs in the store app's URLs
urlpatterns = [
    path('Products/', include(router.urls)),
]
