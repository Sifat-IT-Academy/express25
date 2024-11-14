from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100)
    CATEGORY_TYPE = (('Store', 'Store'),('Restaurant','Restaurant'),)
    # name = models.CharField(_("Nomi"), max_length=255)
    description = models.TextField(_("Tavsif"), blank=True, null=True)
    address = models.ForeignKey(
        "common.Address", 
        on_delete=models.CASCADE, 
        related_name="categories",
        verbose_name=_("Manzil"),
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        _("Telefon raqam"),
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,12}$', 
                message=_("Telefon raqam formati '+999999999' bo'lishi va 12 ta raqamdan oshmasligi kerak.")
            )
        ]
    )
    rating = models.FloatField(
        _("Reyting"),
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text=_("Reyting 0 va 5 orasida bo'lishi kerak."),
        default=3
    )
    image = models.ImageField(_("Rasm"), upload_to='category_images/',)
    delivery_time = models.DurationField(_("Yetkazib berish vaqti"))
    working_time = models.TimeField(_("Ish vaqti"))
    category_type = models.CharField(_("Store turi"), max_length=255,choices=CATEGORY_TYPE)

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def clean(self):
        super().clean()
        # Validate rating range
        if self.rating < 0 or self.rating > 5:
            raise ValidationError(_("Reyting 0 va 5 orasida bo'lishi kerak."))

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(_("Nomi"), max_length=255)
    description = models.TextField(_("Tavsif"), blank=True, null=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name=_("Store")
    )
    image = models.ImageField(_("Rasm"), upload_to='subcategory_images/', blank=True, null=True)

    class Meta:
        verbose_name = _("SubStore")
        verbose_name_plural = _("SubStores")

    def clean(self):
        super().clean()
        if not self.category:
            raise ValidationError(_("SubStore Storega tegishli bo'lishi kerak."))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    description = models.TextField(_("Tavsif"), blank=True, null=True)
    price = models.DecimalField(
        _("Narxi"), 
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]
    )
    subcategory = models.ForeignKey(
        Subcategory, 
        on_delete=models.CASCADE, 
        verbose_name=_("SubStore")
    )
    image = models.ImageField(_("Rasm"), upload_to='product_images/', blank=True, null=True)
    stock = models.PositiveIntegerField(_("Soni"), default=0)

    class Meta:
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")

def clean(self):
    super().clean()
    
    
    if self.price is not None and self.price <= 0:
        raise ValidationError(_("Narx 0 dan katta bo'lishi kerak."))
    
    
    if self.stock is not None and self.stock < 0:
        raise ValidationError(_("Soni manfiy bo'lishi mumkin emas."))
    
    
    if self.image is None:
            raise ValidationError(_("Rasmni yuklash majburiy."))
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    description = models.TextField(_("Tavsif"), blank=True, null=True)
    address = models.ForeignKey(
        "common.Address", 
        on_delete=models.CASCADE, 
        related_name="restaurants",
        verbose_name=_("Manzil"),
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        _("Telefon raqam"),
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,12}$', 
                message=_("Telefon raqam formati '+999999999' bo'lishi va 12 ta raqamdan oshmasligi kerak.")
            )
        ]
    )
    rating = models.FloatField(
        _("Reyting"),
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text=_("Reyting 0 va 5 orasida bo'lishi kerak."),
        default=3
    )
    image = models.ImageField(_("Rasm"), upload_to='restaurant_images/', blank=True, null=True)
    delivery_time = models.DurationField(_("Yetkazib berish vaqti"), blank=True, null=True)
    working_time = models.TimeField(_("Ish vaqti"), blank=True, null=True)
    cuisine_type = models.CharField(_("Taom turi"), max_length=255)

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")

    def clean(self):
        super().clean()
        # Validate rating range
        if self.rating < 0 or self.rating > 5:
            raise ValidationError(_("Reyting 0 va 5 orasida bo'lishi kerak."))

    def __str__(self):
        return self.name