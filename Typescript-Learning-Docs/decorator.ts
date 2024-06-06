// Class decorator: Menambahkan timestamp saat kelas dibuat
function WithTimestamp(constructor: Function) {
    console.log(`${constructor.name} created at ${new Date().toISOString()}`);
  }
  
  // Method decorator: Melakukan logging setiap kali metode dipanggil beserta argumennya
  function LogMethodCall(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
  
    descriptor.value = function (...args: any[]) {
      console.log(`Method ${propertyName} called with args: ${JSON.stringify(args)}`);
      return originalMethod.apply(this, args);
    };
  
    return descriptor;
  }
  
  // Property decorator: Mengubah nilai properti menjadi huruf besar
  function Capitalize(target: any, propertyName: string) {
    let value: string;
  
    const getter = function () {
      return value;
    };
  
    const setter = function (newVal: string) {
      value = newVal.toUpperCase();
    };
  
    Object.defineProperty(target, propertyName, {
      get: getter,
      set: setter
    });
  }
  
  // Parameter decorator: Melakukan validasi parameter dan logging nama metode serta indeks parameter
  function Validate(target: any, methodName: string, parameterIndex: number) {
    console.log(`Validating parameter at index ${parameterIndex} for method ${methodName}`);
  }

  
//   --------------------------------------

@WithTimestamp // Class decorator
class Book {
  @Capitalize // Property decorator
  title: string;

  constructor(title: string) {
    this.title = title; // Properti ini akan diubah menjadi huruf besar oleh dekorator Capitalize
  }

  @LogMethodCall // Method decorator
  updateTitle(@Validate newTitle: string): void { // Parameter decorator
    this.title = newTitle; // Validasi parameter dan logging akan dilakukan oleh dekorator Validate
  }
}

// ---------------------------------------

// Membuat instance dari kelas Book
const book = new Book("the great gatsby");
// Output: Book created at <timestamp>

// Properti title diubah menjadi huruf besar
console.log(book.title); // Output: THE GREAT GATSBY

// Memanggil metode updateTitle dengan parameter baru
book.updateTitle("war and peace");
// Output: Validating parameter at index 0 for method updateTitle
// Output: Method updateTitle called with args: ["war and peace"]

// Properti title kembali diubah menjadi huruf besar
console.log(book.title); // Output: WAR AND PEACE

