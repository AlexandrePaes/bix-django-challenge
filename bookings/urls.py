from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    UsuarioViewSet,
    ClienteViewSet,
    ReservaViewSet,
    HotelViewSet,
    QuartoViewSet,
    # TokenObtainPairView,
    # TokenRefreshView,
)

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuario')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('hoteis', HotelViewSet, basename='hotel')
router.register('quartos', QuartoViewSet, basename='quarto')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

