// OOP in JavaScript - Class Example

class Engine {
  constructor(horsepower, fuelType) {
    this.horsepower = horsepower;
    this.fuelType = fuelType;
  }

  start() {
    console.log("Engine started");
  }

  stop() {
    console.log("Engine stopped");
  }
}

class Car extends Engine {
  constructor(make, model, year, horsepower, fuelType) {
    super(horsepower, fuelType); // Call the parent (Engine) constructor
    this.make = make;
    this.model = model;
    this.year = year;
  }

  displayInfo() {
    console.log(`Make: ${this.make}`);
    console.log(`Model: ${this.model}`);
    console.log(`Year: ${this.year}`);
    console.log(`Horsepower: ${this.horsepower}`);
    console.log(`Fuel Type: ${this.fuelType}`);
  }
}

// Create an object of the Car class
const myCar = new Car("Toyota", "Camry", 2022, 203, "Petrol");

// Call the methods
myCar.displayInfo();
myCar.start();
myCar.stop();
