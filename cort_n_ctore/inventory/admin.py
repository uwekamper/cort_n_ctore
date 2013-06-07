from django.contrib import admin
from models import Part, Place

class PartAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Part, PartAdmin)
admin.site.register(Place, PlaceAdmin)