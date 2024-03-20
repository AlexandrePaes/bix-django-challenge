from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
# from simplejwt.authentication import JWTAuthentication
# from simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from .models import Usuario, Cliente, Reserva, Hotel, Quarto
from .serializers import (
    UsuarioSerializer,
    ClienteSerializer,
    ReservaSerializer,
    HotelSerializer,
    QuartoSerializer,
    # TokenObtainPairSerializer,
    # TokenRefreshSerializer
)

from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from bookings.tasks import send_user_email
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_user_email.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 0, minute = 1)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"1", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")


class UsuarioViewSet(viewsets.ModelViewSet):
    """
        Testar com:
                    curl http://127.0.0.1:8000/api/bookings/usuarios/ 
        Daí com:
                  curl http://127.0.0.1:8000/api/bookings/usuarios/ -H 'Authorization: Token <Copiar e Colar o token gerado no Admin Site>'  
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    permission_classes = [IsAdminOrReadOnly]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.tipo == 'cliente':
            reservas = Reserva.objects.filter(cliente=request.user.cliente)
        elif request.user.tipo == 'funcionario':
            reservas = Reserva.objects.all()
        else:
            return HttpResponse('Permissão negada')
        serializer = ReservaSerializer(reservas, many=True)
        return JsonResponse(serializer.data)

    def post(self, request):
        if request.user.tipo != 'cliente':
            return HttpResponse('Permissão negada')
        data = request.POST
        serializer = ReservaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse('Dados inválidos')


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # permission_classes = [permissions.AllowAny]


class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
    # permission_classes = [permissions.AllowAny]


# class TokenObtainPairView: #(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer


# class TokenRefreshView: #(TokenRefreshView):
#     serializer_class = TokenRefreshSerializer
