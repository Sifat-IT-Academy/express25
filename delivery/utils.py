from accaunt.models import User

def send_sms_to_couriers(order_id):
    couriers = User.objects.filter(is_courier=True)
    for courier in couriers:
        # SMS yuborish funksiyasini chaqirish
        pass
        # send_sms(courier.phone, f"Yangi zakaz mavjud: {order_id}. Yetkazib berishni boshlang.")
