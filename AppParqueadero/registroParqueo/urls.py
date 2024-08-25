from django.urls import path 
from . import views

urlpatterns = [
    path('', views.registroParqueo, name='registroParqueo'),
    path('clientes/', views.clientes, name='cliente'),
    path('add_clientes/', views.add_clientes, name='AddCliente'),
    path('edit_clientes/', views.edit_clientes, name='EditCliente'),
    path('delete_clientes/', views.delete_clientes, name='DeleteCliente'),
    path('add_automovil/', views.add_automovil, name='AddAutomovil'),
    path('edit_automovil/', views.edit_automovil, name='EditAutomovil'),
    path('delete_automovil/', views.delete_automovil, name='DeleteAutomovil'),
    path('imprimir_Ticket/', views.imprimir_ticket, name='ImprimirTicket')
]