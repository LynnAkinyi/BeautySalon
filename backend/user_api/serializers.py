from rest_framework import serializers
from .models import Client, Staff, Service, Appointment

# Serializer for the Client model
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'phone_number', 'address']
        read_only_fields = ['user']

# Serializer for the Staff model
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'user', 'position', 'experience']
        read_only_fields = ['user']

# Serializer for the Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'duration']

# Serializer for the Appointment model
class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    staff = StaffSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id', 'client', 'staff', 'service', 
            'appointment_date', 'appointment_time', 
            'is_confirmed', 'created_at', 'updated_at'
        ]
        read_only_fields = ['is_confirmed', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')
        client = Client.objects.get(user=request.user)
        appointment = Appointment.objects.create(client=client, **validated_data)
        return appointment
