# #Fotima va Sabina , Amal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, username, is_courier, gender, birth_date, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_courier=is_courier,
            gender=gender,
            birth_date=birth_date,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username, is_courier=False, gender='', birth_date=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, username, is_courier, gender, birth_date, **extra_fields)

    def create_superuser(self, email, password, username, is_courier=False, gender='', birth_date=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, username, is_courier, gender, birth_date, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    username = models.CharField(max_length=150, unique=True)
    is_courier = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default='F')
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  
        blank=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
