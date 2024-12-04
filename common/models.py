from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError  
from datetime import datetime

class PlasticCard(models.Model):
    user = models.ForeignKey('accaunt.user',on_delete=models.CASCADE,related_name=_("plastic_cards"))
    card_number = models.CharField(_("card_number"),max_length=16)
    expiration_date = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("PlasticCard")
        verbose_name_plural = _("PlasticCards")

    def __str__(self):
        return str(self.card_number)
    

    def clean(self):
        if not self.card_number.isdigit() or len(self.card_number) !=16:
            raise ValidationError(_("Karta raqami haqiqiy 16 xonali raqam bo'lishi kerak."))
        try:
            expiration = datetime.strptime(self.expiration_date, "%m/%y")
            
        except ValueError:
            raise ValidationError(_("Yaroqlilik muddati MM/YY formatida bo'lishi kerak."))
        if expiration < datetime.now():
            self.is_active = False
            raise ValidationError(_("Ushbu kartaning amal qilish muddati tugagan va uni ishlatib bo'lmaydi."))
         

def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



class Address(models.Model):
    user = models.ForeignKey('accaunt.user',on_delete=models.CASCADE,related_name=_("addresses"))
    label = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=6,decimal_places=4,null=True,blank=True)
    longitude = models.DecimalField(max_digits=6,decimal_places=4,null=True,blank=True) 
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=50)
    street_adress =models.CharField(max_length=150)
    postal_code = models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"{self.user} from {self.city}"


