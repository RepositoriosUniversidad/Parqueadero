
function editarPersonal(id, codigo, nombre, telefono,fecha_ingreso, fecha_salida, valor_a_pagar) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("codigo_editar").value = codigo;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("telefono_editar").value = telefono;
  document.getElementById("fecha_ingreso_editar").value = fecha_ingreso;
  document.getElementById("fecha_salida_editar").value = fecha_salida;
  document.getElementById("valor_a_pagar_editar").value = valor_a_pagar;
}

function eliminarPersonal(id) {
  document.getElementById("id_personal_eliminar").value = id;
}

function editarAuto(id, placa, modelo, color, horaEntrada, horaSalida) {
  document.getElementById("id_automovil_editar").value = id;
  document.getElementById("placa_editar").value = placa;
  document.getElementById("modelo_editar").value = modelo;
  document.getElementById("color_editar").value = color;
  document.getElementById("horaEntrada_editar").value = horaEntrada;
  document.getElementById("horaSalida_editar").value = horaSalida;
}

function imprimirTicket(id, placa, horaEntrada, horaSalida) {
  document.getElementById("id_automovil_imprimir").value = id;
  document.getElementById("placa_editar").value = placa;
  document.getElementById("horaEntrada_imprimir").value = horaEntrada;
  document.getElementById("horaSalida_imprimir").value = horaSalida;
  
}

function eliminarAutomovil(id) {
  document.getElementById("id_automovil_eliminar").value = id;
}


$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 