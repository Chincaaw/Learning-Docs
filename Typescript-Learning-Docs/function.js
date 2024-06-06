"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Function Declarations
function add(x, y) {
    return x + y;
}
console.log(add(2, 3)); // Output: 5
// Function Expressions
const subtract = function (x, y) {
    return x - y;
};
console.log(subtract(5, 3)); // Output: 2
// Arrow Functions
const multiply = (x, y) => x * y;
console.log(multiply(4, 3)); // Output: 12
const divide = (x, y) => x / y;
console.log(divide(10, 2)); // Output: 5
// Optional Parameters
function greet(name, greeting) {
    return `${greeting || 'Hello'}, ${name}!`;
}
console.log(greet("Alice")); // Output: Hello, Alice!
console.log(greet("Bob", "Hi")); // Output: Hi, Bob!
// Default Parameters
function power(base, exponent = 2) {
    return Math.pow(base, exponent);
}
console.log(power(3)); // Output: 9
console.log(power(3, 3)); // Output: 27
// Rest Parameters
function sum(...numbers) {
    return numbers.reduce((acc, cur) => acc + cur, 0);
}
console.log(sum(1, 2, 3, 4)); // Output: 10
console.log(sum(5, 10, 15)); // Output: 30
function display(value) {
    if (typeof value === 'number') {
        console.log(`The number is ${value}`);
    }
    else if (typeof value === 'string') {
        console.log(`The string is ${value}`);
    }
}
display(10); // Output: The number is 10
display("Hello"); // Output: The string is Hello
// Anonymous Functions
setTimeout(function () {
    console.log("This is an anonymous function");
}, 1000);
// IIFE
(function () {
    console.log("This is an IIFE");
})();
(() => {
    console.log("This is an arrow function IIFE");
})();
// Methods in Classes
class Calculator {
    add(x, y) {
        return x + y;
    }
}
const calc = new Calculator();
console.log(calc.add(5, 7)); // Output: 12
// Generator Functions
function* generateSequence() {
    yield 1;
    yield 2;
    yield 3;
}
const generator = generateSequence();
console.log(generator.next().value); // Output: 1
console.log(generator.next().value); // Output: 2
console.log(generator.next().value); // Output: 3
// Asynchronous Functions
function fetchData() {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve("Data fetched");
            }, 1000);
        });
    });
}
fetchData().then((data) => console.log(data)); // Output after 1 second: Data fetched
