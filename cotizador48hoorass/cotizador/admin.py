from django.contrib import admin
from .models import Cotizador, TypeDocument, CountryDestination, CountryOrigin, CategoryPlan

# Register your models here.


class CotizadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoryplans',
                    'origin', 'destination', 'dates', 'numPax']


class TypeDocumentAdmin(admin.ModelAdmin):
    list_display = ['prefix', 'name']


class CountryOriginAdmin(admin.ModelAdmin):
    list_display = ['id', 'prefix', 'name']


class CountryDestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'prefix', 'name']


class CategoryPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Cotizador, CotizadorAdmin)
admin.site.register(TypeDocument, TypeDocumentAdmin)
admin.site.register(CountryOrigin, CountryOriginAdmin)
admin.site.register(CountryDestination, CountryDestinationAdmin)
admin.site.register(CategoryPlan, CategoryPlanAdmin)
