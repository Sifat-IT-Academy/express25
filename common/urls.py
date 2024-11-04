from django.urls import path
from .views import CommonListCreateAPIView, CommonDetailAPIView

urlpatterns = [
    path('common/', CommonListCreateAPIView.as_view(), name='common-list-create'),
    path('common/<int:id>/', CommonDetailAPIView.as_view(), name='common-detail'),
]