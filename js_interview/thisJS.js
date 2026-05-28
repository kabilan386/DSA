const user = {
    name : "Jhon",
    greet : function(){
        console.log(`Hello ${this.name}`)
    },
    greetArrow : () => {
        console.log(`Hello ${this.name}`)
    },
    greet2 : (function(){
        return function(){
            console.log(`Hello ${this.name}`)
        }
    })(),

    greet3 : function(){
        setTimeout(function(){
            console.log(`Hello ${this.name}`)
        }, 1000)
    },
    greet4 : function(){
        setTimeout(() => {
            console.log(`Hello ${this.name}`)
        }, 1000)
    },
    greet5 : function(){
        const self = this
        setTimeout(function(){
            console.log(`Hello ${self.name}`)
        }, 1000)
    },
    greet6 : function(){
        // const self = this
        setTimeout(() => {
            console.log(`Hello ${this.name}`)
        }, 1000)
    },
    greet7 : (() => {     
        return function(){
            console.log(`Hello ${this.name}`)
        }
    })(),
     greet8 : (() => {   
        // const self = this  
        return () => {
            console.log(`Hello ${this.name}`)
        }
    })(),
}

// user.greet()
// user.greetArrow()
// user.greet2()
// user.greet3()
// user.greet4()
// user.greet5()
// user.greet6()
// user.greet7()
user.greet8()

// --- INTERVIEW QUESTION 1: Losing 'this' context ---
// console.log("\n--- Q1: Losing 'this' context ---");
const extractedGreet = user.greet;
// extractedGreet(); // Prints "Hello undefined" (or throws an error in strict mode)

// --- INTERVIEW QUESTION 2: Explicit Binding (call, apply, bind) ---
// console.log("\n--- Q2: Explicit Binding ---");
const user2 = { name: "Alice" };
// user.greet.call(user2); // Output: Hello Alice
// user.greet.apply(user2); // Output: Hello Alice
const boundGreet = user.greet.bind(user2);
// boundGreet(); // Output: Hello Alice

// --- INTERVIEW QUESTION 3: 'this' in Constructor Functions ---
// console.log("\n--- Q3: Constructor Function ---");
function Person(name) {
    this.name = name;
    this.sayName = function() {
        console.log(`My name is ${this.name}`);
    };
}
const p1 = new Person("Bob");
// p1.sayName(); // Output: My name is Bob

// --- INTERVIEW QUESTION 4: 'this' inside nested objects ---
// console.log("\n--- Q4: Nested Objects ---");
const company = {
    name: "Tech Corp",
    employee: {
        name: "Charlie",
        printName: function() {
            console.log(`Employee is ${this.name}`);
        }
    }
}
// company.employee.printName(); // Output: Employee is Charlie