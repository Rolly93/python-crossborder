import React, { useState, useMemo } from "react";
import "./Dashboard.css";
import Tracker from "./Track/Tracker";
import CaptureShipment from "./Track/BorderTrack/CatureShipment/CaptureShipmet";

// Import all shipment data outside the component to avoid re-importing on every render
import shipmentsData from "../lib/cruces_finalizados.json"; 
//import ShipmentForm from "../components/ShipmentForm";

export default function Dashboard() {
    
    // State for the search input
    const [shipmentId, setShipmentId] = useState("");
    
    // Handler for input change
    const ShipmentSearch = (event) => {
        setShipmentId(event.target.value);
    };

    const filteredShipments = useMemo(() => {
        const searchInput = shipmentId.toLowerCase();

        if (!searchInput) {
            return shipmentsData;
        }

        return shipmentsData.filter(shipment => {
            return (
                shipment.Cliente.toLowerCase().includes(searchInput) ||
                // Check if property exists before calling toString
                (shipment.numVehiculo && shipment.numVehiculo.toString().toLowerCase().includes(searchInput)) || 
                (shipment.referencia && shipment.referencia.toLowerCase().includes(searchInput))
            );
        });
    }, [shipmentId]); // Dependency array: Re-run calculation only when shipmentId changes
    
    return (
        <div>
            <h2>Dashboard</h2>
            <div className="searchInput">
            <input 
                type="text" 
                placeholder="Search by Client, Trailer, or Reference"
                value={shipmentId}
                onChange={ShipmentSearch} 
                />
                </div>
            
            {filteredShipments.length === 0 && shipmentId.length > 0 ? (
                <div className="dash no-results">
                    <p>⚠️ No shipments found matching "{shipmentId}".</p>
                </div>
            ) : (
                <>
                <CaptureShipment/>
                <Tracker shipments={filteredShipments} />
                </>
            )}
        </div>
    );
}