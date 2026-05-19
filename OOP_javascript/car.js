// ============================================================
// OOP in JavaScript - Classes, Multilevel Inheritance,
// Polymorphism, and Abstract Classes
// ============================================================

// ─────────────────────────────────────────────
// ABSTRACT CLASS (simulated in JavaScript)
// JavaScript doesn't have built-in abstract classes,
// so we simulate them by throwing errors in the base class.
// ─────────────────────────────────────────────
class Vehicle {
  constructor(make, model, year) {
    if (new.target === Vehicle) {
      throw new Error("Cannot instantiate abstract class 'Vehicle' directly.");
    }
    this.make = make;
    this.model = model;
    this.year = year;
  }

  // Abstract method - must be overridden by subclasses
  fuelType() {
    throw new Error("Abstract method 'fuelType()' must be implemented.");
  }

  // Concrete method shared by all vehicles
  displayInfo() {
    console.log(`Make: ${this.make}`);
    console.log(`Model: ${this.model}`);
    console.log(`Year: ${this.year}`);
    console.log(`Fuel: ${this.fuelType()}`);
  }
}

// ─────────────────────────────────────────────
// LEVEL 1 INHERITANCE: Engine extends Vehicle
// ─────────────────────────────────────────────
class Engine extends Vehicle {
  constructor(make, model, year, horsepower) {
    super(make, model, year);
    this.horsepower = horsepower;
  }

  start() {
    console.log(`${this.make} engine started.`);
  }

  stop() {
    console.log(`${this.make} engine stopped.`);
  }

  // Implements the abstract method
  fuelType() {
    return "Unknown";
  }
}

// ─────────────────────────────────────────────
// LEVEL 2 INHERITANCE (Multilevel): Car extends Engine
// ─────────────────────────────────────────────
class Car extends Engine {
  constructor(make, model, year, horsepower, numDoors) {
    super(make, model, year, horsepower);
    this.numDoors = numDoors;
  }

  // POLYMORPHISM: overrides fuelType() from Engine
  fuelType() {
    return "Petrol";
  }

  displayInfo() {
    super.displayInfo(); // Call parent displayInfo()
    console.log(`Horsepower: ${this.horsepower}`);
    console.log(`Doors: ${this.numDoors}`);
  }
}

// ─────────────────────────────────────────────
// LEVEL 2 INHERITANCE (Multilevel): ElectricCar extends Engine
// POLYMORPHISM: different fuelType() than Car
// ─────────────────────────────────────────────
class ElectricCar extends Engine {
  constructor(make, model, year, horsepower, batteryRange) {
    super(make, model, year, horsepower);
    this.batteryRange = batteryRange;
  }

  // POLYMORPHISM: overrides fuelType() differently
  fuelType() {
    return "Electric";
  }

  displayInfo() {
    super.displayInfo();
    console.log(`Horsepower: ${this.horsepower}`);
    console.log(`Battery Range: ${this.batteryRange} km`);
  }
}

// ─────────────────────────────────────────────
// DEMO
// ─────────────────────────────────────────────

console.log("===== Petrol Car =====");
const myCar = new Car("Toyota", "Camry", 2022, 203, 4);
myCar.displayInfo();
myCar.start();
myCar.stop();

console.log("\n===== Electric Car =====");
const myEV = new ElectricCar("Tesla", "Model 3", 2023, 450, 560);
myEV.displayInfo();
myEV.start();
myEV.stop();

// ─────────────────────────────────────────────
// POLYMORPHISM DEMO: same method, different behavior
// ─────────────────────────────────────────────
console.log("\n===== Polymorphism Demo =====");
const vehicles = [myCar, myEV];
vehicles.forEach((v) => {
  console.log(`${v.make} ${v.model} => Fuel: ${v.fuelType()}`);
});

// ─────────────────────────────────────────────
// ABSTRACT CLASS ENFORCEMENT DEMO
// ─────────────────────────────────────────────
console.log("\n===== Abstract Class Enforcement =====");
try {
  const v = new Vehicle("Generic", "Unknown", 2020);
} catch (e) {
  console.log(`Caught: ${e.message}`);
}
