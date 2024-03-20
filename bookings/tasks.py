
from django.contrib.auth import get_user_model

from celery import shared_task
from .models import Reserva, Cliente
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"


@shared_task
def send_user_email():
    sent = False
    reservas = Reserva.objects.all().filter(status='confirmada') 
    
    for reserva in reservas:
        mail_subject = 'Confirmação da sua Reserva'
        message = f"""
        Olá {reserva.cliente.nome},

        Sua reserva para o quarto {reserva.quarto} foi confirmada!

        **Detalhes da Reserva:**

        * Data de Entrada: {reserva.data_entrada}
        * Data de Saída: {reserva.data_saida}

        Agradecemos a sua escolha e esperamos a sua estadia!

        Atenciosamente,

        Equipe do Hotel Bix
        """
    
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[-reserva.cliente.email],
            fail_silently=True,
        )

        sent = True

    return f'Emails de confirmação enviados para {len(reservas)} reservas\n' \
            f'incluindo {reserva.cliente.email}'


@shared_task
def liberar_quartos_cancelados():
    today = timezone.now()
    for reserva in Reserva.objects.filter(
        status='cancelada', data_saida__lte=today
    ):
        reserva.quarto.available = True
        reserva.save()

