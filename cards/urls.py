from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet
from cards.views import ping_view

router = DefaultRouter()
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
        path('ping/', ping_view),  # 👈 add this line

]


