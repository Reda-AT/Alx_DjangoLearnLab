from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('', include('router.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
