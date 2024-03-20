
# V3

from django.contrib import admin

from .models import Usuario, Hotel, Quarto, Cliente, Reserva


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo')
    list_editable = ('username', 'email', 'tipo')
    list_display_links = None


class HotelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    list_editable = ('nome', 'endereco')
    list_display_links = None

class QuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'hotel')
    list_editable = ('numero', 'tipo', 'hotel')
    list_display_links = None

# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'tipo')
#     list_editable = ('username', 'email', 'tipo')
#     list_display_links = None

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_editable = ('nome', 'email')
    list_display_links = None

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'quarto', 'data_entrada', 'data_saida', 'status')
    list_editable = ('cliente', 'quarto', 'data_entrada', 'data_saida', 'status')
    list_display_links = None

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Quarto, QuartoAdmin)
# admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva, ReservaAdmin)



################################################################

# V2

# from django.contrib import admin
# from .models import Hotel, Room, Customer, Reservation

# class HotelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address')
#     list_editable = ('address',)
#     list_display_links = None

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('room_number', 'hotel', 'capacity')
#     list_editable = ('hotel', 'capacity')
#     list_display_links = None

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'email')
#     list_editable = ('email',)
#     list_display_links = None

# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'room', 'check_in', 'check_out', 'is_cancelled')
#     list_editable = ('check_in', 'check_out', 'is_cancelled')
#     list_display_links = None

# admin.site.register(Hotel, HotelAdmin)
# admin.site.register(Room, RoomAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Reservation, ReservationAdmin)



########################################################

# from django.contrib import admin
# from .models import Hotel, Room, Reservation


# @admin.register(Hotel)
# class HotelAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     list_display = ('name', 'location', 'capacity')
#     list_editable = ('name', 'location', 'capacity')
#     list_display_links = None


# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     list_display = ('number', 'type', 'price', 'status', 'hotel')
#     list_editable = ('number', 'type', 'price', 'status', 'hotel')
#     list_display_links = None


# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     list_display = ('customer', 'room', 'check_in', 'check_out')
#     list_editable = ('customer', 'room', 'check_in', 'check_out')
#     list_display_links = None