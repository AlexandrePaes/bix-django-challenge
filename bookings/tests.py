from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bookings.models import Usuario, Cliente, Reserva, Hotel, Quarto
from bookings.serializers import (
    UsuarioSerializer,
    ClienteSerializer,
    ReservaSerializer,
    HotelSerializer,
    QuartoSerializer,
)

# from rest_framework.authtoken.models import Token


# Criando uma classe de teste para testar as funcionalidades da API
class APITestCase(TestCase):
    def setUp(self):
        # Criando alguns usuários com diferentes níveis de permissão
        self.customer = User.objects.create_user(username='customer', password='customer', permission_level='C')
        self.staff = User.objects.create_user(username='staff', password='staff', permission_level='S')
        self.admin = User.objects.create_user(username='admin', password='admin', permission_level='A')
        # Criando alguns hotéis e quartos
        self.hotel1 = Hotel.objects.create(name='Hotel 1', location='Location 1', capacity=10)
        self.hotel2 = Hotel.objects.create(name='Hotel 2', location='Location 2', capacity=-5)

class UsuarioViewSetTest(APITestCase):

    def test_get_as_cliente(self):
        # Create a test user with `cliente` role
        cliente_user = self.create_test_user(tipo='cliente')
        self.client.force_authenticate(cliente_user)

        url = reverse('usuario-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], cliente_user.cliente.reservas.count())  # Check for expected reservations

    def test_get_as_funcionario(self):
        # Create a test user with `funcionario` role
        funcionario_user = self.create_test_user(tipo='funcionario')
        self.client.force_authenticate(funcionario_user)

        url = reverse('usuario-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Reserva.objects.all().count())  # Check for all reservations

    def test_get_as_admin(self):
        # Create a test user with `admin` role
        admin_user = self.create_test_user(tipo='admin')
        self.client.force_authenticate(admin_user)

        url = reverse('usuario-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Usuario.objects.all().count())  # Check for all users

    def test_get_unauthorized(self):
        url = reverse('usuario-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_as_cliente(self):
        # Create a test user with `cliente` role
        cliente_user = self.create_test_user(tipo='cliente')
        self.client.force_authenticate(cliente_user)

        # Provide valid data for a new reservation (consider using a helper function)
        valid_data = {
            'hotel': 1,  # Replace with actual hotel ID
            'quarto': 1,  # Replace with actual quarto ID
            # ... other reservation data
        }
        url = reverse('usuario-list')  # This should be 'reserva-list'
        response = self.client.post(url, valid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_as_unauthorized(self):
        # No user authenticated
        valid_data = {
            'hotel': 1,  # Replace with actual hotel ID
            'quarto': 1,  # Replace with actual quarto ID
            # ... other reservation data
        }
        url = reverse('usuario-list')  # This should be 'reserva-list'
        response = self.client.post(url, valid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    