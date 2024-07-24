import React from 'react';

const CarList = ({ cars, onSelectCar }) => {
  return (
    <div>
      <h2>Car List</h2>
      <ul>
        {cars.map((car) => (
          <li key={car.car_id}>
            {car.car_id} - {car.engine_type} - {car.transmission_type}
            <button onClick={() => onSelectCar(car.car_id)}>View Details</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarList;
