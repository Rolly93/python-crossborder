import React, { useState } from 'react';
// Importa tu archivo CSS de estilos aquí
import './ShipmentForm.css'; 

// --- Estado Inicial del Envío (shipment) ---
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
};

const ShipmentForm = () => {
  const [shipment, setShipment] = useState(initialShipmentState);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setShipment(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Datos del Envío Guardados:', shipment);
    alert('Datos guardados. Revisa la consola para ver el objeto shipment.');
  };

  const handleClear = () => {
    setShipment(initialShipmentState);
  };

  // Función para crear un campo de texto/número/fecha genérico
  const renderField = (label, name, type = 'text') => {
    return (
      <div className="form-group">
        <label htmlFor={name}>{label}</label>
        <input
          id={name}
          name={name}
          type={type}
          value={shipment[name]}
          onChange={handleChange}
          className="form-input"
        />
      </div>
    );
  };

  return (

    <div className="container">
    <div className="form-container">
      <h2 className="form-title">Formulario de Seguimiento Logístico</h2>
      <p className="form-subtitle">Edición de datos para el envío</p>
      
      <form onSubmit={handleSubmit} className="shipment-form">
        

        <div className="section-header">Información General</div>
        <div className="form-section">
          {renderField('Referencia', 'referencia')}
          {renderField('Número de Trailer', 'trailerNumber')}
          {renderField('Cliente', 'cliente')}
          
          <div className="form-group">
            <label htmlFor="tipoOperacion">Tipo de Operación</label>
            <select
              id="tipoOperacion"
              name="tipoOperacion"
              value={shipment.tipoOperacion}
              onChange={handleChange}
              className="form-select"
            >
              <option value="Importación">Importación</option>
              <option value="Exportación">Exportación</option>
              <option value="Transbordo">Transbordo</option>
            </select>
          </div>
          
          {renderField('Resguardo', 'resguardo')}
        </div>
        

        <div className="section-header">Patios y Tiempos</div>
        <div className="form-section">
          {renderField('Patio MX (mx_Yard)', 'mx_Yard')}
          {renderField('Patio USA (usa_Yard)', 'usa_Yard')}
          {renderField('Llegada (arrival)', 'arrival', 'datetime-local')}
          {renderField('Salida (departure)', 'departure', 'datetime-local')}
          {renderField('Patio de Seguridad', 'safety_Yard')}
        </div>

        <div className="section-header">Procesos de Aduana</div>
        <div className="form-section custom-grid">

          <div className="customs-block">
            <h3>Aduana México (MX)</h3>
            {renderField('Inspección MX', 'inspecction_MX', 'datetime-local')}
            {renderField('Nuevo Sello MX', 'mx_newSeal')}
            {renderField('Despacho Aduana MX', 'clear_mx_Customs', 'datetime-local')}
          </div>
          

          <div className="customs-block">
            <h3>Aduana Estados Unidos (USA)</h3>
            {renderField('Inspección USA', 'inspection_USA', 'datetime-local')}
            {renderField('Nuevo Sello USA', 'usa_NewSeal')}
            {renderField('Despacho Aduana USA', 'clear_Usa_Customs', 'datetime-local')}
          </div>
        </div>

        <div className="section-header">Entrega Final</div>
        <div className="form-section">
          {renderField('Entrega (deliver)', 'deliver', 'datetime-local')}
          {renderField('¿Quién Recibe?', 'whoRecive')}
        </div>


        <div className="button-group">
          <button type="button" onClick={handleClear} className="btn-secondary">
            Limpiar Formulario
          </button>
          <button type="submit" className="btn-primary">
            Guardar Envío
          </button>
        </div>
      </form>
    </div>
    </div>
  );
};

export default ShipmentForm;