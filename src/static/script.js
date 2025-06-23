
const showCaptureShipment = document.querySelectorAll(".btn-cature-shipment");
const captureForm = document.querySelectorAll(".capture-data-shipment-content");
const formFieldNames = [
  "referencia",
  "operacion",
  "caja",
  "sello",
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

showCaptureShipment.forEach(function(button,index) {
  button.addEventListener("click", function(e) {
  captureForm[index].style.display = "block";
  
  }  ) 
})

const btnsCancel = document.querySelectorAll(".cancel");
btnsCancel.forEach(function(btnCancel,index) {
btnCancel.addEventListener("click", function(e){
  
  
  captureForm[index].style.display = "none";
})
})

/*interaccion para cerrar las ventanas */
const btnClose = document.querySelectorAll('.close');

btnClose.forEach(function(button,index) {
  button.addEventListener("click", function(e) {
    
    captureForm[index].style.display = "none"

    })
  });

const tableRow = document.querySelectorAll('table .row');

tableRow.forEach(row => {
  row.addEventListener('dblclick', function(e) {
    const cells = this.querySelectorAll('td');
    let update = true;
    updateShipment(cells, update);
  })});
function updateShipment(cells , update){
//to display in a form all data and no bieng able to modify it 
const formUpdate = document.getElementById('update')


formFieldNames.forEach((fieldName, index) => {
  
  if (cells[index].textContent && update) {
    formUpdate[fieldName].value = cells[index].textContent;
    formUpdate[fieldName].disabled = true;
    
  }
  captureForm[1].style.display = 'block';
});
  };
;
document.querySelectorAll(".passwords").forEach(input => {
  input.addEventListener("input", () => {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;
    validatePassword(password, confirmPassword);

  });
});

function updateCheckmark(selector, color) {
  const checkmark = document.querySelector(`${selector} svg`);
  if (checkmark) checkmark.style.fill = color;
}

function validatePassword(password, confirmPassword) {
  // No spaces
  updateCheckmark("#checkmarck_iconNonSpace", password.includes(" ") ? "red" : "green");

  // Lowercase letter
  updateCheckmark("#checkmarck_iconLower", /[a-z]/.test(password) ? "green" : "white");

  // Uppercase letter
  updateCheckmark("#checkmarck_iconUpper", /[A-Z]/.test(password) ? "green" : "white");

  // Number
  updateCheckmark("#checkmarck_iconNum", /[0-9]/.test(password) ? "green" : "white");

  // Minimum 8 characters
  updateCheckmark("#checkmarck_8characters", password.length >= 8 ? "green" : "white");

  // Password match
  if (password.length >= 8) {
    if (password === confirmPassword) {
      updateCheckmark("#checkmarck_iconIqual", "green");
    } else {
      updateCheckmark("#checkmarck_iconIqual", "white");
    }
  } else {
    updateCheckmark("#checkmarck_iconIqual", confirmPassword === "" ? "black" : "white");
  }
}

const clearData = document.querySelector("button[type ='reset']").addEventListener("click", (e)=>{
  document.querySelectorAll("input").forEach(data=>{
    data.value = "";
    document.getElementById("puesto").value ="capturista"
  })
}); 

const operador = document.getElementById("puesto").addEventListener("change",(e)=>{
switch (e.target.value) {
  case "operador":
       document.getElementById("operador").style.display = "block"; 
       document.getElementById("administrador").style.display = "none";    

    break;
  case "administrador" :
    document.getElementById("administrador").style.display = "block"; 
    document.getElementById("operador").style.display = "none"; 
    const admit = document.getElementById("administrador").value="yes"
        break;

  default:
document.getElementById("administrador").style.display = "none"; 
document.getElementById("operador").style.display ="none";    
    break;
}

})