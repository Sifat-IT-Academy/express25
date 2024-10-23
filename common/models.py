from django.db import models 
from django.utils.translation import gettext_lazy as _


# Create your models here.


# class BaseModel(models.Model):
#     created_at = models.DateTimeField("created at", auto_now_add=True)
#     updated_at = models.DateTimeField("updated at", auto_now=True)
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="%(class)s_createdby",
#         editable=False,
#     )
#     modified_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         related_name="%(class)s_modifiedby",
#         null=True,
#         blank=True,
#         editable=False,
#     )

#     class Meta:
#         abstract = True

#     def save(self, *args, **kwargs):
#         if hasattr(self, "slug") and hasattr(self, "title"):
#             if not self.slug:
#                 self.slug = generate_unique_slug(self.__class__, self.title)

#         if hasattr(self, "slug") and hasattr(self, "name"):
#             if not self.slug:
#                 self.slug = generate_unique_slug(self.__class__, self.name)
#         super().save(*args, **kwargs)


# Muhammadjon, Boborahim, Norbek

# class PlasticCard(models.Model):
#     pass

# class Address(models.Model):
#     pass



from django.db import models
from account.models import CustomUser
# Create your models here.

class PlasticCart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_number = models.PositiveIntegerField(default=0)
    expiration_date = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("PlasticCart")
        verbose_name_plural = _("PlasticCarts")

    def __str__(self):
        return str(self.user)
    


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=150, blank=True, null=True)
    postal_code = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addreses")
    
    def __str__(self):
        return f"{self.user} from {self.city}"
