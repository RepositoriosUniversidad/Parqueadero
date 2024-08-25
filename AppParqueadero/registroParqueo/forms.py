from django import forms
from registroParqueo.models import Cliente, Autos
from django.forms import ValidationError
from datetime import datetime

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre Cliente: ',
            'telefono': 'Teléfono Cliente',
        }
    
    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"]
        existe = Cliente.objects.filter(codigo = codigo).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return codigo

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre Cliente: ',
            'telefono': 'Teléfono Cliente',
        }
        widgets= {
            'codigo': forms.TextInput(attrs={'type':'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'})
        }
        

class AddAutomovilForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = ('placa', 'modelo', 'color', 'horaEntrada', 'horaSalida')
        labels = {
            'placa': 'Placa Automóvil: ',
            'modelo': 'Modelo Automóvil: ',
            'color': 'Color Automóvil:',
            'horaEntrada': 'Hora Entrada: ',
            'horaSalida': 'Hora Salida: '
        }
        widgets={
            'horaEntrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'horaSalida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def clean_placa(self):
        placa = self.cleaned_data["placa"]
        esta = Autos.objects.filter(placa = placa).exists()
        if esta:
            raise ValidationError("Este nombre ya existe")
        return placa
    
    def clean(self):
        cleaned_data = super().clean()
        hora_entrada = cleaned_data.get('horaEntrada')
        hora_salida = cleaned_data.get('horaSalida')
        
        if hora_entrada >= hora_salida:
            raise ValidationError('La hora de entrada debe ser menor que la hora de salida.')
        
class EditarAutomovilForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = ('placa', 'modelo', 'color', 'horaEntrada', 'horaSalida')
        labels = {
            'placa': 'Placa Automóvil: ',
            'modelo': 'Modelo Automóvil: ',
            'color': 'Color Automóvil:',
            'horaEntrada': 'Hora Entrada:',
            'horaSalida': 'Hora Salida:',
        }
        widgets= {
            'placa': forms.TextInput(attrs={'type':'text', 'id': 'placa_editar'}),
            'modelo': forms.TextInput(attrs={'id': 'modelo_editar'}),
            'color': forms.TextInput(attrs={'id': 'color_editar'}),
            'horaEntrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'horaSalida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class imprimirTicketForm(forms.ModelForm):
    precioHora = forms.CharField(label='Precio Hora:', max_length=255, disabled=True)
    valor_a_pagar = forms.CharField(label='Valor Total:', max_length=255, disabled=True)
    class Meta:
        model = Autos
        fields = ('placa', 'horaEntrada', 'horaSalida')
        labels = {
            'placa': 'Placa Automóvil: ', 
            'horaEntrada': 'Hora Entrada:',
            'horaSalida': 'Hora Salida:',
        }
        widgets= {
            'placa': forms.TextInput(attrs={'type':'text', 'id': 'placa_editar'}),
            'horaEntrada': forms.TextInput(attrs={'id': 'horaEntrada_editar', 'readonly':'readonly'}),
            'horaSalida': forms.TextInput(attrs={'id': 'horaSalida_editar', 'readonly':'readonly'}),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(imprimirTicketForm, self).__init__(*args, **kwargs)
        # Asignar valores fijos
        self.fields['precioHora'].initial = '2000'  # Ejemplo: Precio por hora fijo
        #self.fields['valor_a_pagar'].initial = '100.00'  # Ejemplo: Valor total fijo
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_hora= datetime.strptime('horaEntrada', '%Y-%m-%d %H:%M:%S')
        hora = fecha_hora.hour
        print(f'La hora extraída es: {hora}')
        self.fields['valor_a_pagar'].initial = 'hora'  # Ejemplo: Valor total fijo
            
      

    
        


        
