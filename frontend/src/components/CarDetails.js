import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';

const CarDetails = ({ carId }) => {
  const [car, setCar] = useState(null);

  const fetchCar = useCallback(async () => {
    console.log(`Fetching details for car ID: ${carId}`); // Log carId
    try {
      const response = await axios.get(`/api/cars/${carId}`);
      console.log('Car details fetched:', response.data); // Log response data
      setCar(response.data);
    } catch (error) {
      console.error('Error fetching car details:', error);
    }
  }, [carId]);

  useEffect(() => {
    fetchCar();
  }, [fetchCar]);

  const startEngine = async () => {
    try {
      await axios.post(`/api/cars/${carId}/start`);
      fetchCar(); // Refresh details after starting the engine
    } catch (error) {
      console.error('Error starting engine:', error);
    }
  };

  const stopEngine = async () => {
    try {
      await axios.post(`/api/cars/${carId}/stop`);
      fetchCar(); // Refresh details after stopping the engine
    } catch (error) {
      console.error('Error stopping engine:', error);
    }
  };

  const shiftUp = async () => {
    try {
      await axios.post(`/api/cars/${carId}/shift_up`);
      fetchCar(); // Refresh details after shifting up
    } catch (error) {
      console.error('Error shifting up:', error);
    }
  };

  const shiftDown = async () => {
    try {
      await axios.post(`/api/cars/${carId}/shift_down`);
      fetchCar(); // Refresh details after shifting down
    } catch (error) {
      console.error('Error shifting down:', error);
    }
  };

  if (!car) return <div>Loading car details...</div>;

  return (
    <div>
      <h2>Car Details - {carId}</h2>
      <p>Engine Status: {car.engine_status}</p>
      <p>Gear: {car.gear}</p>
      <button className="control-button" onClick={startEngine}>Start Engine</button>
      <button className="control-button" onClick={stopEngine}>Stop Engine</button>
      <button className="control-button" onClick={shiftUp}>Shift Up</button>
      <button className="control-button" onClick={shiftDown}>Shift Down</button>
    </div>
  );
};

export default CarDetails;
