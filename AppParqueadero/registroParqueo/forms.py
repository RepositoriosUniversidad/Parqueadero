from django import forms
from registroParqueo.models import Cliente, Autos
from django.forms import ValidationError
from datetime import datetime

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'fecha_ingreso', 'fecha_salida','valor_a_pagar')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre Cliente: ',
            'telefono': 'Teléfono Cliente:',
            'fecha_ingreso': 'Fecha de ingreso:',
            'fecha_salida': 'Fecha de salida:',
            'valor_a_pagar': 'Valor a pagar:'
        }
        widgets={
            'fecha_ingreso': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
            'fecha_salida': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        }
        
    
    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"]
        existe = Cliente.objects.filter(codigo = codigo).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return codigo
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get('fecha_ingreso')
        fecha_salida = cleaned_data.get('fecha_salida')
        if fecha_ingreso >= fecha_salida:
            raise ValidationError('La fecha de ingreso debe ser menor que la fecha de salida.')
    
class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'fecha_ingreso', 'fecha_salida','valor_a_pagar')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre Cliente: ',
            'telefono': 'Teléfono Cliente',
            'fecha_ingreso': 'Fecha de ingreso:',
            'fecha_salida': 'Fecha de salida:',
            'valor_a_pagar': 'Valor a pagar:'
        }
        widgets= {
            'codigo': forms.TextInput(attrs={'type':'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date-local','id':'fecha_ingreso_editar'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date-local','id':'fecha_salida_editar'}),
            'valor_a_pagar': forms.TextInput(attrs={'id': 'valor_a_pagar_editar'})
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
            'horaEntrada': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
            'horaSalida': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
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
            'horaEntrada': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'horaEntrada_editar'}),
            'horaSalida': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'horaSalida_editar'}),
        }
        
class imprimirTicketForm(forms.ModelForm):
    precioHora = forms.CharField(label='Precio Hora:', max_length=255, disabled=True)
    valor_a_pagar = forms.CharField(label='Valor a Pagar:', max_length=255, disabled=True)
    class Meta:
        model = Autos
        fields = ('horaEntrada', 'horaSalida')
        labels = {
            'horaEntrada': 'Hora Entrada:',
            'horaSalida': 'Hora Salida:',
        }
        widgets= {
            'horaEntrada': forms.TextInput(attrs={'id': 'horaEntrada_imprimir'}),
            'horaSalida': forms.TextInput(attrs={'id': 'horaSalida_imprimir'}),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(imprimirTicketForm, self).__init__(*args, **kwargs)
        # Asignar valores fijos
        self.fields['precioHora'].initial = '2000'  # Ejemplo: Precio por hora fijo
       
        hora_entrada = self.initial.get('horaEntrada')
        hora_salida = self.initial.get('horaSalida')
        print(hora_entrada)
        print(hora_salida)
        if hora_entrada and hora_salida:
            valor_total = self.calcular_valor_a_pagar(hora_entrada, hora_salida, float(self.fields['precioHora'].initial))
            self.fields['valor_a_pagar'].initial = valor_total
    
    def calcular_valor_a_pagar(self, hora_entrada_str, hora_salida_str, tarifa_por_hora):
        formato = "%Y-%m-%dT%H:%M"  # Ajusta el formato según el formato de tus horas (datetime-local en HTML5)

        try:
            # Convertir las cadenas de texto en objetos datetime
            hora_entrada = datetime.strptime(hora_entrada_str, formato)
            hora_salida = datetime.strptime(hora_salida_str, formato)

            # Calcular la diferencia en horas
            diferencia_horas = (hora_salida - hora_entrada).total_seconds() / 3600

            # Calcular el valor a pagar
            valor_a_pagar = diferencia_horas * tarifa_por_hora

            # Redondear a dos decimales y retornar el valor
            return round(valor_a_pagar, 2)

        except ValueError as e:
            # Manejo de errores si el formato de la fecha es incorrecto
            print(f"Error al convertir la hora: {e}")
            return None
