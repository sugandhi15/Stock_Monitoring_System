from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _


#  custom user model to make email as unique identifier
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        
        # normalise_email - converts email to its standard form like in small letters
        email = self.normalize_email(email)
        # creates a model for this user
        user = self.model(email=email, **extra_fields)
        # set_password - stores the password in the database in hashed form
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(email, password, **extra_fields)
    



class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now_add=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email




class Stock(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lastUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

