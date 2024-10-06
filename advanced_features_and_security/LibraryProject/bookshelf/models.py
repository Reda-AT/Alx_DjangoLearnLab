from django.db import models
from django.contrib.auth.models import AbstractUsers, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "can view book"),
            ("can_create", "can create book"),
            ("can_edit", "can edit book"),
            ("can_delete", "can delete book"),
        ]


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, profile_photo, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth, profile_photo, password=None):
        user = self.create_user(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pics/')

    objects = MyUserManager()
