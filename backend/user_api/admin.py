from django.contrib import admin
from .models import Client, Staff, Service, Appointment

# Register the Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

# Register the Staff model
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'experience')
    search_fields = ('user__username', 'position')

# Register the Service model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)
    list_filter = ('price',)

# Register the Appointment model
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'staff', 'appointment_date', 'appointment_time', 'is_confirmed')
    search_fields = ('client__user__username', 'service__name', 'staff__user__username')
    list_filter = ('appointment_date', 'is_confirmed')
    ordering = ('appointment_date', 'appointment_time')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # if the object is already created, make these fields read-only
            return ['client', 'service', 'appointment_date', 'appointment_time']
        return []

