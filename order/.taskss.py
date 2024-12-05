from celery import shared_task
from twilio.rest import Client
from accaunt.models import Courier

@shared_task
def notify_couriers_task(order_id):
    from .models import Order
    order = Order.objects.get(id=order_id)

    couriers = Courier.objects.filter(availability=True)
    twilio_account_sid = "your_account_sid"
    twilio_auth_token = "your_auth_token"
    twilio_phone_number = "your_twilio_phone_number"

    client = Client(twilio_account_sid, twilio_auth_token)

    for courier in couriers:
        user = courier.user
        phone_number = user.phone_number if user else None
        if phone_number:
            try:
                message = (
                    f"Assalomu alaykum, {user.first_name}! "
                    f"Yangi buyurtma mavjud: Buyurtma ID {order.id}. "
                    "Batafsil ma'lumot uchun tizimni tekshiring."
                )
                client.messages.create(
                    body=message,
                    from_=twilio_phone_number,
                    to=phone_number
                )
            except Exception as e:
                print(f"SMS yuborishda xatolik ({phone_number}): {e}")
