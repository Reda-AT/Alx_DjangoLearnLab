from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Route pour le logout (utilise la vue intégrée de Django)
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Route pour l'inscription
    path('register/', views.register, name='register'),
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
