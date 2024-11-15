# #Fotima va Sabina , Amal
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email=None, phone_number=None, password=None, is_courier=False, gender=None, birth_date=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be provided")
        if not password:
            raise ValueError("Password is not provided")

        email = self.normalize_email(email) if email else None
        user = self.model(
            email=email,
            phone_number=phone_number,
            is_courier=is_courier,
            gender=gender,
            birth_date=birth_date,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, phone_number=None, password=None, is_courier=False, gender=None, birth_date=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, password, is_courier, gender, birth_date, **extra_fields)

    def create_superuser(self, email=None, phone_number=None, password=None, is_courier=False, gender=None, birth_date=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, is_courier, gender, birth_date, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True, max_length=254, blank=True, null=True)

    phone_number = models.CharField(max_length=15, unique=True)
    is_courier = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)  # Add null=True and blank=True
    birth_date = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'  
    REQUIRED_FIELDS = ['email']   

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self) -> str:
        return f'{self.phone_number}'

class Plastik(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiry_date = models.DateField()
    holder_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Card {self.card_number} - {self.holder_name}'

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.country}'
