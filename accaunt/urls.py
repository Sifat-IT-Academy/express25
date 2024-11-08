from accaunt.views import register_user
from django.urls import path

urlpatterns = [
path('registration/',register_user,name="register-page")
]