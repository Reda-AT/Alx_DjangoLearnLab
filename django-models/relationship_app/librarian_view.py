from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
  return user._is_autehnticated and user.userprofile.role == 'librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
  return render(request, 'relationship_app/librarian_view.html')
