"use strict";
// Boolean
let isDone = true;
console.log("Boolean value isDone:", isDone);
// Number
let decimal = 6;
let hex = 0xf00d;
let binary = 0b1010;
let octal = 0o744;
console.log("Decimal number:", decimal);
console.log("Hexadecimal number:", hex);
console.log("Binary number:", binary);
console.log("Octal number:", octal);
// String
let color = "blue";
let fullName = `John Doe`;
let age = 30;
let sentence = `Hello, my name is ${fullName}. I'll be ${age + 1} years old next month.`;
console.log("Color:", color);
console.log("Full name:", fullName);
console.log("Sentence:", sentence);
// Array
let list = [1, 2, 3];
let anotherList = [4, 5, 6];
console.log("Number array list:", list);
console.log("Another number array list:", anotherList);
// Tuple
let x;
x = ["hello", 10];
console.log("Tuple:", x);
// Enum
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
let c = Color.Green;
console.log("Enum value Color.Green:", c);
// Any
let notSure = 4;
notSure = "maybe a string instead";
notSure = false;
console.log("Any type variable:", notSure);
// Void
function warnUser() {
    console.log("This is my warning message");
}
warnUser();
// Null and Undefined
let u = undefined;
let n = null;
console.log("Undefined value:", u);
console.log("Null value:", n);
// Never
function error(message) {
    throw new Error(message);
}
// try {
//     error("Something went wrong");
// } catch (e) {
//     console.log("Caught error:", e.message);
// }
