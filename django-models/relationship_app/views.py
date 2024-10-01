from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Function-Based View (FBV) pour lister tous les livres
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-Based View (CBV) pour afficher les détails d'une bibliothèque
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('list_books')  # Redirect to any view after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
