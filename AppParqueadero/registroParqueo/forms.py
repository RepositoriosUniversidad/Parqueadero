from django import forms
from registroParqueo.models import Cliente, Autos
from django.forms import ValidationError

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
        

        


        
