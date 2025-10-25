import BorderTrack from "./BorderTrack/BorderTrack";

// Tracker component must accept 'shipments' prop
export default function Tracker({ shipments }){ 

    return (
      <div className="dash">
      <table>
      <thead>
        <tr>
        <th>Track Number</th>
        <th>Trailer</th>
        <th>Referencia Cliente</th>
        <th>Cliente</th>
        <th>Tipo Operacion</th>
        <th>Origen</th>
        <th>Destino</th>
        <th>Recoleccion</th>
        <th>Salida de Patio Origen</th>
        <th>Inspeccion Mx</th>
        <th>Sello Nuevo</th>
        <th>Modulacion MX</th>
        <th>Inspeccion USA</th>
        <th>Tipo de Inspeccion</th>
        <th>Nuevo Sello</th>
        <th>Verde USA</th>
        <th>Resguardo</th>
        <th>Patio</th>
        <th>Entrega</th>
        <th>Recibio</th>
        </tr>
      </thead>
        <BorderTrack shipments={shipments} />
    </table>
            </div>
            )
}