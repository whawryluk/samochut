import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CarCreationForm from './components/CarCreationForm';
import CarList from './components/CarList';
import CarDetails from './components/CarDetails';
import './App.css';

const App = () => {
  const [cars, setCars] = useState([]);
  const [selectedCarId, setSelectedCarId] = useState('');

  const fetchCars = async () => {
    try {
      const response = await axios.get('/api/cars');
      console.log("Cars fetched:", response.data);
      setCars(response.data);
    } catch (error) {
      console.error('Error fetching cars:', error);
    }
  };

  useEffect(() => {
    fetchCars();
  }, []);

  const handleCarCreated = (carId) => {
    setSelectedCarId(carId);
    fetchCars(); // Fetch the updated car list after creating a car
  };

  const handleSelectCar = (carId) => {
    setSelectedCarId(carId);
  };

  return (
    <div className="App">
      <h1>Car Simulator</h1>
      <CarCreationForm onCarCreated={handleCarCreated} />
      <CarList cars={cars} onSelectCar={handleSelectCar} />
      {selectedCarId && <CarDetails key={selectedCarId} carId={selectedCarId} />}
    </div>
  );
};

export default App;
