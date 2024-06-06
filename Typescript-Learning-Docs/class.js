"use strict";
// Define a class named Person
class Person {
    // Constructor to initialize the properties
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    // Method to display the person's details
    display() {
        console.log(`Name: ${this.name}, Age: ${this.age}`);
    }
}
// Define a class named Employee
class Employee {
    // Constructor to initialize the properties
    constructor(name, salary, department) {
        this.name = name;
        this.salary = salary;
        this.department = department;
    }
    // Public method to display the employee's details
    display() {
        console.log(`Name: ${this.name}, Department: ${this.department}`);
    }
    // Private method to calculate the bonus
    calculateBonus() {
        return this.salary * 0.1;
    }
}
// Define a subclass named Manager that extends Employee
class Manager extends Employee {
    // Constructor to initialize the properties
    constructor(name, salary, department) {
        // Call the constructor of the base class (Employee)
        super(name, salary, department);
    }
    // Public method to display the manager's details
    displayManagerDetails() {
        console.log(`Name: ${this.name}, Department: ${this.department}`);
    }
}
// Define a class with static members
class MathUtils {
    // Static method: can be called on the class itself
    static calculateCircumference(radius) {
        return 2 * MathUtils.pi * radius;
    }
}
// Static property: belongs to the class, not an instance
MathUtils.pi = 3.14;
// Create an instance of Person
const person1 = new Person("Alice", 30);
person1.display(); // Output: Name: Alice, Age: 30
// Create an instance of Employee
const emp = new Employee("John", 50000, "IT");
emp.display(); // Output: Name: John, Department: IT
// Create an instance of Manager
const mgr = new Manager("Jane", 70000, "HR");
mgr.displayManagerDetails(); // Output: Name: Jane, Department: HR
// Access static property and method without creating an instance
console.log(MathUtils.pi); // Output: 3.14
console.log(MathUtils.calculateCircumference(10)); // Output: 62.8
