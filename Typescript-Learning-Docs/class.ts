// Define a class named Person
class Person {
    // Class properties
    name: string;
    age: number;
  
    // Constructor to initialize the properties
    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  
    // Method to display the person's details
    display(): void {
      console.log(`Name: ${this.name}, Age: ${this.age}`);
    }
  }
  
  // Define a class named Employee
  class Employee {
    // Public property: accessible from anywhere
    public name: string;
    // Private property: accessible only within this class
    private salary: number;
    // Protected property: accessible within this class and subclasses
    protected department: string;
  
    // Constructor to initialize the properties
    constructor(name: string, salary: number, department: string) {
      this.name = name;
      this.salary = salary;
      this.department = department;
    }
  
    // Public method to display the employee's details
    public display(): void {
      console.log(`Name: ${this.name}, Department: ${this.department}`);
    }
  
    // Private method to calculate the bonus
    private calculateBonus(): number {
      return this.salary * 0.1;
    }
  }
  
  // Define a subclass named Manager that extends Employee
  class Manager extends Employee {
    // Constructor to initialize the properties
    constructor(name: string, salary: number, department: string) {
      // Call the constructor of the base class (Employee)
      super(name, salary, department);
    }
  
    // Public method to display the manager's details
    public displayManagerDetails(): void {
      console.log(`Name: ${this.name}, Department: ${this.department}`);
    }
  }
  
  // Define a class with static members
  class MathUtils {
    // Static property: belongs to the class, not an instance
    static pi: number = 3.14;
  
    // Static method: can be called on the class itself
    static calculateCircumference(radius: number): number {
      return 2 * MathUtils.pi * radius;
    }
  }
  
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
  