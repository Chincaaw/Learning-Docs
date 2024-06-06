// Define an interface for a person
interface Person {
    name: string;
    age: number;
    // Optional property
    email?: string;
  }
  
  // Function that accepts an object adhering to the Person interface
  function greet(person: Person): void {
    console.log(`Hello, ${person.name}!`);
  }
  
  // Class implementing an interface
  interface Shape {
    area(): number;
    perimeter(): number;
  }
  
  class Circle implements Shape {
    constructor(public radius: number) {}
  
    area(): number {
      return Math.PI * Math.pow(this.radius, 2);
    }
  
    perimeter(): number {
      return 2 * Math.PI * this.radius;
    }
  }
  
  const circle = new Circle(5);
  console.log(circle.area()); // Output: 78.53981633974483
  console.log(circle.perimeter()); // Output: 31.41592653589793
  
  // Extending interfaces
  interface BasicPerson {
    name: string;
    age: number;
  }
  
  interface Employee extends BasicPerson {
    salary: number;
    department: string;
  }
  
  const employee: Employee = {
    name: "Jane",
    age: 25,
    salary: 60000,
    department: "HR"
  };
  
  // Using optional properties
  const car: { make: string; model: string; year?: number } = {
    make: "Toyota",
    model: "Camry"
  };
  
  // Object destructuring
  const user = {
    id: 1,
    username: "user1",
    email: "user1@example.com"
  };
  
  const { id, username, email } = user;
  
  // Array destructuring
  const numbers = [1, 2, 3, 4, 5];
  const [first, second, ...rest] = numbers;
  
  console.log(first); // Output: 1
  console.log(second); // Output: 2
  console.log(rest); // Output: [3, 4, 5]
  