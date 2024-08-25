from django.shortcuts import render, redirect
from .models import Cliente, Autos
from .forms import AddClienteForm, EditarClienteForm, AddAutomovilForm, EditarAutomovilForm, imprimirTicketForm
from django.contrib import messages

# Create your views here.

def registroParqueo(request):
    autos = Autos.objects.all()
    form_auto = AddAutomovilForm()
    form_editar = EditarAutomovilForm()
    form_ticket = imprimirTicketForm()
    context = {
        'autos': autos,
        'form_auto': form_auto,
        'form_editar': form_editar,
        'form_ticket_auto': form_ticket,
    }
    return render(request,'registroParqueo.html',context)

def clientes(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
        
    }
    return render(request,'clientes.html',context)

def add_clientes(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al guardar el cliente")
                return redirect('cliente')
    return redirect('cliente')

def edit_clientes(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
        request.POST, request.FILES, instance = cliente)
        if form.is_valid:
            form.save()
    return redirect('cliente')

def delete_clientes(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('cliente')

def add_automovil(request):
    if request.POST:
        form = AddAutomovilForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al Guardar el Auto")
                return redirect('registroParqueo')
    return redirect('registroParqueo')

def edit_automovil(request):
    if request.POST:
        automovil = Autos.objects.get(pk=request.POST.get('id_automovil_editar'))
        form = EditarAutomovilForm(
        request.POST, request.FILES, instance = automovil)
        if form.is_valid:
            form.save()
    return redirect('registroParqueo')

def delete_automovil(request):
    if request.POST:
        auto = Autos.objects.get(pk=request.POST.get('id_automovil_eliminar'))
        auto.delete()
    return redirect('registroParqueo')

def imprimir_ticket(request):
    if request.POST:
        form = imprimirTicketForm()
        automovil = Autos.objects.get(pk=request.POST.get('id_automovil_editar'))
        precioHora= form.cleaned_data.get('precio_Hora')
        valor_a_pagar= form.cleaned_data.get('valor_a_pagar')
    return redirect('registroParqueo')







