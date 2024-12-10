from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Payment
from delivery.utils import send_sms_to_couriers

@receiver(post_save, sender=Payment)
def notify_couriers(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        order = instance.order
        send_sms_to_couriers(order.id)
        print("Kurierlarga sms yuborildi!!!")
