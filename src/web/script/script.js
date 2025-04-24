const container_capture_data_shipment = document.getElementById("container_capture_data_shipment");
const update_shipment_content = document.getElementById("container-update-shipment");
const formFieldNames = [
  "referencia",
  "operacion",
  "caja",
  "unidad",
  "referencia_interna",
  "cliente",
  "patio_origen",
  "patio_destion",
  "recoleccion",
  "salida",
  "inspeccion_rojo",
  "sello_mex",
  "verde_mex",
  "inspeccion_usa",
  "tipo_inspeccion",
  "sello_usa",
  "verde_usa",
  "resguardo",
  "patio",
  "entrega",
  "recibe"
];
const btnCatureSipment = document.getElementById("btn-cature-shipment").onclick = function() {
  container_capture_data_shipment.style.display = "block";
};

/*interaccion para cerrar las ventanas */

const btnClose = document.querySelectorAll('.close');

btnClose.forEach(function(button,index) {
  button.addEventListener("click", function(e) {
    
    switch (index) {
      case 0:
        container_capture_data_shipment.style.display = "none"
        break;

        case 1:
          update_shipment_content.style.display="none"
    
      default:
        break;
    }

  });
});

const tableRow = document.querySelectorAll('table .row');

tableRow.forEach(row => {
  row.addEventListener('dblclick', function() {
    const cells = this.querySelectorAll('td');
    let update = true;
    updateShipment(cells ,update)


  })});
function updateShipment(cells , update){
/* to display in a form all data and no bieng able to modify it */
const formUpdate = document.getElementById('update')

   
    formFieldNames.forEach((fieldName, index) => {
      if (cells[index].textContent && update) {
        formUpdate[fieldName].value = cells[index].textContent;
        formUpdate[fieldName].disabled = true;
        
      }
    });
    update_shipment_content.style.display = 'block';
  };
;

const btnUpdateShipment = document.getElementById("btn-update-shipment").onclick = function(){
  let formUpdate = document.getElementById("update")
  formFieldNames.forEach((fieldName) => {
    formUpdate[fieldName].value='';
    formUpdate[fieldName].disabled=false;

  })

 update_shipment_content.style.display = "block";
}


function captureShipment(){
 var embarque = document.getElementById("embarque").value;
 var operacion = document.getElementById("operacion").value;
 var unidad = document.getElementById("unidad").value
 var origen = document.getElementById("origen").value
 var destiono = document.getElementById("destino").value
 var referencia = document.getElementById("referencia").value
 var cliente = document.getElementById('cliente').value
 var confrim_data = false

 let shipment = {
"embarque":embarque,
"operacion":operacion,
"unidad":unidad,
"origen":origen,
"destino":destiono,
"referencia":referencia,
"cliente":cliente,
"confrim_data":confrim_data
 }
 console.log(confrim_data)
 pywebview.api.Capture_shipment(shipment)

}