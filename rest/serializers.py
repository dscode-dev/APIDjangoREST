from rest_framework import serializers
from rest.models import *


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title']

    
class IdentifiedErrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifiedErrors
        fields = ['error_id', 'error_desc', 'error_type']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_name', 'siem_name', 'status']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caser
        fields = ['case_number', 'short_description', 'case_date']

class TicketsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsList
        fields = ['id', 'description', 'customer', 'owner', 'priority', 'status', 'create_date']