from django.urls import path
from .views import *

urlpatterns = [
    path("notes/", NotesAPIView.as_view(), name='notes'),
    path("errors/", IdentifiedErrorsAPIViwe.as_view(), name='id_errors'),
    path("customers/", CustomerAPIView.as_view(), name='customers'),
    path("cases/", CaseAPIView.as_view(), name='cases'),
    path("tickets/list/", TicketsListAPIView.as_view(), name='tickets')

]
