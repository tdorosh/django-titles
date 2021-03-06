from django.contrib import admin
from .models import Title, IncomingLetter, OutgoingLetter, Counterparty
# Register your models here.

def make_done(modeladmin, request, queryset):
	queryset.update(is_done=True)
	
make_done.short_description = 'Make titles done'

class TitleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Інформація про титул', {'fields': ['title', 'type', 'client']}),
		('Інофрмація про дату і час', {'fields': ['incoming_letter', 'outgoing_letter', 'entry_datetime']}),
		('Додаткова інформація', {'fields': ['ministry_agreement', 'is_done', 'notes']}),
	]
	search_fields = ['title']
	list_display = ['title', 'type', 'client', 'ministry_agreement', 'is_done', 'notes']
	list_filter = ['type', 'client']
	actions = [make_done]
	
	

admin.site.register(Title, TitleAdmin)
admin.site.register(IncomingLetter)
admin.site.register(OutgoingLetter)
admin.site.register(Counterparty)