from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=self.author)

    def test_create_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_permissions(self):
        # Test unauthenticated user trying to create a book
        url = reverse('book-list')
        data = {'title': 'Unauthorized Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
