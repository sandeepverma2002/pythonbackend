from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


from django.http import JsonResponse

def ping_view(request):
    return JsonResponse({'status': 'ok'})
