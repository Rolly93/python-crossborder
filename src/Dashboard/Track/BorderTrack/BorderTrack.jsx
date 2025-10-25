import { useState, useEffect } from "react";
import Loading from "../../../components/Loading";
import { motion } from "framer-motion";

export default function BorderTrack({shipments}) {



let resTructedShipment = ShipmetDestruter(shipments );


const [isLoading , setIsLoading] = useState(true);

useEffect(() => {
  
const timer = setTimeout(() => {
  setIsLoading(false);
},1500)
return () => clearTimeout(timer);
},[])

if(isLoading)return<Loading />
  

const rowVariants = {
  hidden: { opacity:0 , y:20},
  visible:{
    opacity: 1 ,
    y:0,
    transition:{
      duration:0.5
    }
  }
}

   const shipmentRows = resTructedShipment.map((shipment,index) => (
    
    <tr  key={index}>
      <td>{shipment.index}</td>
      <td>{shipment.trailerNumber}</td>
      <td>{shipment.referencia}</td>
      <td>{shipment.cliente}</td>
      <td>{shipment.mx_Yard}</td>
      <td>{shipment.tipoOperacion}</td>
      <td>{shipment.usa_Yard}</td>
      <td>{shipment.arrival}</td>
      <td>{shipment.departure}</td>
      <td>{shipment.inspecction_MX}</td>
      <td>{shipment.mx_newSeal}</td>
      <td>{shipment.clear_mx_Customs}</td>
      <td>{shipment.inspection_USA}</td>
      <td>{shipment.clear_Usa_Customs}</td>
      <td>{shipment.usa_NewSeal}</td>
      <td>{shipment.clear_Usa_Customs}</td>
      <td>{shipment.resguardo}</td>
      <td>{shipment.safety_Yard}</td>
      <td>{shipment.deliver}</td>
      <td>{shipment.whoRecive}</td>

    </tr>))

  
    return(
       <motion.tbody 
       variants={rowVariants}
       initial="hidden"
       animate="visible"
       transition={{delay: 0.1}}>
        {shipmentRows}
        </motion.tbody> 

    )
  }
function ShipmetDestruter(dictShipmet){
let in_de = 0
const shipments = dictShipmet.map((shipment,index)=>{

  const{
      referencia,
      numVehiculo: trailerNumber, // Rename while destructuring
      Cliente: cliente,
      afsFecha,
      afsTiempo,
      dpuFecha,
      dpuTiempo,
      exrFecha,
      exrTiempo,
      exrNotas: mx_newSeal, // Rename while destructuring
      eccFecha,
      eccTiempo,
      ilrFecha,
      ilrTiempo,
      ilrtipo: inspection_Typ, // Rename while destructuring
      iltNotas: usa_NewSeal, // Rename while destructuring
      clrFecha,
      clrTiempo,
      st1Fecha,
      st1Tiempo,
      st1Notas: safety_Yard, // Rename while destructuring
      tscFecha,
      tscTiempo,
      tscNotas: whoRecive, // You're using st1Notas for two fields, which is fine
  } = shipment;
  return {
    index   :`nd1${in_de++}`,
    referencia  :`${referencia}`,
    trailerNumber,
    cliente,
    tipoOperacion  :`Exportacion`,
    mx_Yard  :`Yarda MX`,
    usa_Yard  :"Bodega Expeditors",
    arrival :`${afsFecha} ${afsTiempo}`,
    departure   :`${dpuFecha} ${dpuTiempo}`,
    inspecction_MX   :`${exrFecha } ${exrTiempo}`,
    mx_newSeal ,
    clear_mx_Customs   :`${eccFecha} ${eccTiempo}`,
    inspection_USA  :`${ilrFecha} ${ilrTiempo}`,
    inspection_Typ ,
    usa_NewSeal  ,
    clear_Usa_Customs :`${clrFecha} ${clrTiempo}`,
    resguardo  :`${st1Fecha} ${st1Tiempo}`,
    safety_Yard ,
    deliver  :`${tscFecha} ${tscTiempo}`,
    whoRecive,
  }
  })
  return shipments
  
}
