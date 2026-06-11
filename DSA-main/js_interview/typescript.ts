// generic type

function identity<T>(arg: T): T {
    return arg;
}

console.log(identity<number>(1));
console.log(identity<string>("hello"));

// interface

interface Person {
    name: string;
    age: number;
}

function greet(person: Person) {
    return `Hello ${person.name}, you are ${person.age} years old.`;
}

console.log(greet({ name: "John", age: 30 }));

// optional interface

interface Person1 {
    name: string;
    age?: number;
}

function greet1(person: Person1) {
    return `Hello ${person.name}, you are ${person.age} years old.`;
}

console.log(greet1({ name: "John", age: 30 }));
console.log(greet1({ name: "John" }));

// Type Aliases

type Person2 = {
    name: string;
    age?: number;
}

function greet2(person: Person2) {
    return `Hello ${person.name}, you are ${person.age} years old.`;
}

console.log(greet2({ name: "John", age: 30 }));

// function type

type GreetFunction = (person: Person) => string;

function greet3(person: Person, fn: GreetFunction) {
    return fn(person);
}

console.log(greet3({ name: "John", age: 30 }, greet));


interface User {
  id: number;
  name: string;
}

type Status = "active" | "inactive";

interface UserWithStatus {
  user: User;
  status: Status;
}

function processUser(user: UserWithStatus) {
  if (user.status === "active") {
    console.log(`Processing active user: ${user.user.name}`);
  } else {
    console.log(`Processing inactive user: ${user.user.name}`);
  }
}

processUser({ user: { id: 1, name: "John" }, status: "active" })
processUser({ user: { id: 2, name: "Jane" }, status: "inactive" });


// without tuple

function getFirstElement(arr: any[]) {
    return arr[0];
}

console.log(getFirstElement([1, 2, 3]));
console.log(getFirstElement(["hello", "world"]));



// tuple
// Reason : 

function getFirstElementTuple(arr: [number, string]) {
    return arr[0];
}

console.log(getFirstElementTuple([1, "hello"]));
// console.log(getFirstElementTuple(["hello", 1]));

// Intersections

interface Person {
    name: string;
    age: number;
}

interface Employee {
    employeeId: number;
    salary: number;
}

type PersonEmployee = Person & Employee;

function processPersonEmployee(personEmployee: PersonEmployee) {
    console.log(`Name: ${personEmployee.name}, Age: ${personEmployee.age}, Employee ID: ${personEmployee.employeeId}, Salary: ${personEmployee.salary}`);
}

processPersonEmployee({ name: "John", age: 30, employeeId: 1, salary: 1000 });