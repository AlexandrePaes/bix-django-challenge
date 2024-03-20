
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Usuario(AbstractUser):
    tipo = models.CharField(max_length=20, choices=[('cliente', 'Cliente'),
                                              ('funcionario', 'Funcionário'),
                                         ('administrador', 'Administrador')])
    groups = models.ManyToManyField(
        Group,
        # blank=True, null=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        # blank=True, null=True
    )


class Hotel(models.Model):
    nome = models.CharField(blank=True, null=True, max_length=255)
    endereco = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.nome
    

class Quarto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=[('individual', 'Individual'), ('casal', 'Casal'), ('familia', 'Família')])

    def __str__(self):
        return f"Quarto {self.numero} no {self.hotel}"


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateField()
    data_saida = models.DateField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')])

    def __str__(self):
        return f"{self.quarto} reservado por {self.cliente}"


