from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class NotesAPIView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serielizer = NotesSerializer(notes, many=True)
        return Response(serielizer.data)

class IdentifiedErrorsAPIViwe(APIView):
    def get(self, request):
        errors = IdentifiedErrors.objects.all()
        serializers = IdentifiedErrosSerializer(errors, many=True)
        return Response(serializers.data)

class CustomerAPIView(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializers = CustomerSerializer(customer, many=True)
        return Response(serializers.data)

class CaseAPIView(APIView):
    def get(self, request):
        case = Caser.objects.all()
        serializers = CaseSerializer(case, many=True)
        return Response(serializers.data)

class TicketsListAPIView(APIView):
    def get(self, request):
        tickets = TicketsList.objects.all()
        serializers = TicketsListSerializer(tickets, many=True)
        return Response(serializers.data)