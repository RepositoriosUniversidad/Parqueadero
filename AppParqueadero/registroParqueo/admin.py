from django.contrib import admin
from registroParqueo.models import Cliente, Autos
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono','codigo', 'fecha_ingreso', 'fecha_salida', 'valor_a_pagar')
    search_fields = ['nombre']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Cliente, ClienteAdmin)

class AutoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo','color', 'horaEntrada', 'horaSalida')
    search_fields = ['placa']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Autos, AutoAdmin)
