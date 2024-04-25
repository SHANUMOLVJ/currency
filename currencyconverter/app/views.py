from rest_framework import generics
from .models import CurrencyConversion
from .serializers import CurrencyConversionSerializer

class CurrencyConversionListCreate(generics.ListCreateAPIView):
    queryset = CurrencyConversion.objects.all()
    serializer_class = CurrencyConversionSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Currency Converter API!")
