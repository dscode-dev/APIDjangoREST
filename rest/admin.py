from django.contrib import admin
from rest.models import *

class NotesAdmin(admin.ModelAdmin):
    pass

class IdentifiedErrorsAdmin(admin.ModelAdmin):
    pass

class OnNoticeAdmin(admin.ModelAdmin):
    pass

class FlowsAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class CaserAdmin(admin.ModelAdmin):
    pass

class TicketsListAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notes, NotesAdmin)
admin.site.register(IdentifiedErrors, IdentifiedErrorsAdmin)
admin.site.register(OnNotice, OnNoticeAdmin)
admin.site.register(Flows, FlowsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Caser, CaserAdmin)
admin.site.register(TicketsList, TicketsListAdmin)


# Register your models here.
