from django.urls import path
from .views import CurrencyConversionListCreate

urlpatterns = [
    path('currency-conversions/', CurrencyConversionListCreate.as_view(), name='currency-conversion-list-create'),
    # other URL patterns...
]
