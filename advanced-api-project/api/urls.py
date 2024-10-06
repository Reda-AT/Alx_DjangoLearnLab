from django.urls import path
from api import views


urlpatterns = [
    path('books/', views.ListView.as_view(), name='list-books'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='detail-books'),
    path('books/update/<int:pk>', views.UpdateView.as_view(), name='update-books'),
    path('books/create/', views.CreateView.as_view(), name='create-book'),
    path('books/delete/<int:pk>', views.DeleteView.as_view(), name='delete-book'),
]
