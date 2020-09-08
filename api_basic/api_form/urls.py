from django.urls import path
from .views import ContactAPIView,ContactDetails

urlpatterns = [
    path('contact/',ContactAPIView.as_view()),
    path('detail/<int:id>/',ContactDetails.as_view()),
]
