import React,{  useState } from "react"
import "./CaptureShipment.css"

const initialShipmentState = {

     // General Info
  index: '',
  trailerNumber: '',
  referencia: '',
  cliente: '',
  tipoOperacion: 'Importación', 
  resguardo: '',
  
  // Yard & Times
  mx_Yard: '',
  usa_Yard: '',
  arrival: '',
  departure: '',
  safety_Yard: '',

  // Customs MX
  inspecction_MX: '',
  mx_newSeal: '',
  clear_mx_Customs: '',
  
  // Customs USA
  inspection_USA: '',
  clear_Usa_Customs: '',
  usa_NewSeal: '',

  // Delivery
  deliver: '',
  whoRecive: '',

}
const   CaptureShipment = () => {
  const [shipment, setShipment] = useState(initialShipmentState);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setShipment(prev => ({
      ...prev,
      [name]: value
    }));
  }
const handelSubmit = (e) => {
    e.preventDefault();
    console.log("Datos del Envio Guardados",shipment)
    alert("datos guardados Revisa");
}
const handelClear =()=>{
    setShipment(initialShipmentState)
}

return (
    <div className="container">
        <form action="" onSubmit={handelSubmit} className="">
        <h2>Shipmet Capture</h2>
        <p>Edicion de datos para el Envio</p>

        <div className="firstcolum"></div>
        <div className="secondcolumn"></div>
        <div className="thircolum"></div>
        </form>
    </div>
)

};



export  default CaptureShipment