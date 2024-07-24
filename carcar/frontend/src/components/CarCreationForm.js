import React, { useState } from 'react';
import axios from 'axios';

const engineOptions = [
  { value: 'GasolineEngine', label: 'Gasoline' },
  { value: 'ElectricEngine', label: 'Electric' },
  { value: 'DieselEngine', label: 'Diesel' }
];

const transmissionOptions = [
  { value: 'ManualTransmission', label: 'Manual' },
  { value: 'AutomaticTransmission', label: 'Automatic' }
];

const CarCreationForm = ({ onCarCreated }) => {
  const [carId, setCarId] = useState('');
  const [engineType, setEngineType] = useState(engineOptions[0].value);
  const [transmissionType, setTransmissionType] = useState(transmissionOptions[0].value);
  const [message, setMessage] = useState('');

  const handleCreateCar = async () => {
    try {
      const response = await axios.post('/api/cars', {
        id: carId,
        engine_type: engineType,
        transmission_type: transmissionType
      });
      setMessage(response.data.message);
      onCarCreated(carId);
    } catch (error) {
      console.error('Error creating car:', error);
      if (error.response && error.response.data && error.response.data.error) {
        setMessage(error.response.data.error);
      } else {
        setMessage('Error creating car');
      }
    }
  };

  return (
    <div>
      <h2>Create a Car</h2>
      <input
        type="text"
        placeholder="Car ID"
        value={carId}
        onChange={(e) => setCarId(e.target.value)}
      />
      <select value={engineType} onChange={(e) => setEngineType(e.target.value)}>
        {engineOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <select value={transmissionType} onChange={(e) => setTransmissionType(e.target.value)}>
        {transmissionOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <button onClick={handleCreateCar}>Create Car</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default CarCreationForm;
