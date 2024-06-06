// Boolean
let isDone: boolean = true;
console.log("Boolean value isDone:", isDone);

// Number
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
console.log("Decimal number:", decimal);
console.log("Hexadecimal number:", hex);
console.log("Binary number:", binary);
console.log("Octal number:", octal);

// String
let color: string = "blue";
let fullName: string = `John Doe`;
let age: number = 30;
let sentence: string = `Hello, my name is ${fullName}. I'll be ${age + 1} years old next month.`;
console.log("Color:", color);
console.log("Full name:", fullName);
console.log("Sentence:", sentence);

// Array
let list: number[] = [1, 2, 3];
let anotherList: Array<number> = [4, 5, 6];
console.log("Number array list:", list);
console.log("Another number array list:", anotherList);

// Tuple
let x: [string, number];
x = ["hello", 10];
console.log("Tuple:", x);

// Enum
enum Color { Red, Green, Blue }
let c: Color = Color.Green;
console.log("Enum value Color.Green:", c);

// Any
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false;
console.log("Any type variable:", notSure);

// Void
function warnUser(): void {
    console.log("This is my warning message");
}
warnUser();

// Null and Undefined
let u: undefined = undefined;
let n: null = null;
console.log("Undefined value:", u);
console.log("Null value:", n);

// Never
function error(message: string): never {
    throw new Error(message);
}
// try {
//     error("Something went wrong");
// } catch (e) {
//     console.log("Caught error:", e.message);
// }
