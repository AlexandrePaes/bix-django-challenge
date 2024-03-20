
# from django.contrib.auth import authenticate
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
from .models import Usuario, Hotel, Quarto, Cliente, Reserva


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


# class TokenObtainPairSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         username = data['username']
#         password = data['password']
#         user = authenticate(username=username, password=password)
#         if user is None:
#             raise serializers.ValidationError('Credenciais inválidas.')
#         return {'username': user.username, 'token': user.token}


# class TokenRefreshSerializer(serializers.Serializer):
#     token = serializers.CharField(max_length=255, write_only=True)

#     def validate(self, data):
#         token = data['token']
#         user = Usuario.objects.filter(token=token).first()
#         if user is None:
#             raise serializers.ValidationError('Token inválido.')
#         return {'token': user.token}



