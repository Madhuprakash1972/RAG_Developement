# Complete DSA Guide: C & C++ with OOPs Concepts

---

# PART 1: C vs C++ - Major Differences

## Overview

| Feature | C | C++ |
|---------|---|-----|
| **Paradigm** | Procedural only | Multi-paradigm (Procedural, OOP, Generic) |
| **Programming Style** | Function-driven | Object-driven |
| **Data Security** | No data hiding | Encapsulation (private, protected, public) |
| **Functions** | No function overloading | Function overloading supported |
| **Memory Management** | malloc/free | new/delete + smart pointers |
| **References** | Not supported | Supported |
| **Exceptions** | Not supported | try-catch supported |
| **Templates** | Not supported | Templates for generic programming |
| **Standard Library** | Limited (stdio.h, stdlib.h) | STL (vector, map, set, algorithm) |

---

## Difference Examples

### 1. Program Structure

**C:**
```c
#include <stdio.h>
#include <stdlib.h>

// Data structure
struct Point {
    int x;
    int y;
};

// Functions operate on data
void print_point(struct Point p) {
    printf("(%d, %d)\n", p.x, p.y);
}

struct Point create_point(int x, int y) {
    struct Point p;
    p.x = x;
    p.y = y;
    return p;
}

int main() {
    struct Point p = create_point(10, 20);
    print_point(p);
    return 0;
}
```

**C++:**
```cpp
#include <iostream>
using namespace std;

// Class with data and functions together
class Point {
private:
    int x, y;  // Private by default (data hiding)
    
public:
    // Constructor
    Point(int x = 0, int y = 0) : x(x), y(y) {}
    
    // Member function
    void print() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
    
    // Getter with const
    int getX() const { return x; }
    
    // Setter
    void setX(int x) { this->x = x; }
};

int main() {
    Point p(10, 20);  // Cleaner syntax
    p.print();
    return 0;
}
```

---

### 2. Memory Management

**C:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Static allocation
    int arr[5];
    
    // Dynamic allocation
    int *ptr = (int*)malloc(5 * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    
    // Use memory
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
    }
    
    // Manual deallocation (must remember!)
    free(ptr);
    
    // String handling
    char *str = (char*)malloc(20 * sizeof(char));
    strcpy(str, "Hello");
    free(str);
    
    return 0;
}
```

**C++:**
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    // Static allocation
    int arr[5];
    
    // Dynamic allocation with new
    int *ptr = new int[5];
    
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
    }
    
    // Manual deallocation
    delete[] ptr;
    
    // Better: Use vector (automatic memory management)
    vector<int> vec(5);
    for (int i = 0; i < 5; i++) {
        vec[i] = i * 10;
    }
    // No need to delete - automatic
    
    // String handling
    string str = "Hello";  // No manual memory management
    cout << str << endl;
    
    // Smart pointers (C++11)
    unique_ptr<int[]> smartPtr(new int[5]);
    // Automatically deleted when out of scope
    
    return 0;
}
```

---

### 3. Function Overloading

**C:** (Not supported - must use different names)
```c
#include <stdio.h>

void print_int(int x) {
    printf("Int: %d\n", x);
}

void print_float(float x) {
    printf("Float: %.2f\n", x);
}

void print_string(char *str) {
    printf("String: %s\n", str);
}

int main() {
    print_int(10);
    print_float(3.14f);
    print_string("Hello");
    return 0;
}
```

**C++:** (Supported - same name, different parameters)
```cpp
#include <iostream>
using namespace std;

// Function overloading
void print(int x) {
    cout << "Int: " << x << endl;
}

void print(float x) {
    cout << "Float: " << x << endl;
}

void print(string str) {
    cout << "String: " << str << endl;
}

int main() {
    print(10);        // Calls print(int)
    print(3.14f);     // Calls print(float)
    print("Hello");   // Calls print(string)
    return 0;
}
```

---

### 4. References

**C:** (Not supported - only pointers)
```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(&x, &y);  // Must use pointers
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

**C++:** (References supported - cleaner syntax)
```cpp
#include <iostream>
using namespace std;

// Using references (cleaner)
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 5, y = 10;
    swap(x, y);  // No & needed - cleaner!
    cout << "x = " << x << ", y = " << y << endl;
    
    // Reference example
    int num = 10;
    int &ref = num;  // ref is an alias for num
    ref = 20;        // modifies num
    cout << num << endl;  // prints 20
    
    return 0;
}
```

---

### 5. Exception Handling

**C:** (Not supported - use return codes)
```c
#include <stdio.h>
#include <stdlib.h>

int divide(int a, int b, int *result) {
    if (b == 0) {
        return -1;  // Error code
    }
    *result = a / b;
    return 0;  // Success
}

int main() {
    int result;
    int status = divide(10, 0, &result);
    
    if (status != 0) {
        printf("Error: Division by zero\n");
        return 1;
    }
    
    printf("Result: %d\n", result);
    return 0;
}
```

**C++:** (Exception handling with try-catch)
```cpp
#include <iostream>
using namespace std;

class DivisionByZeroError : public exception {
    const char* what() const noexcept override {
        return "Division by zero";
    }
};

int divide(int a, int b) {
    if (b == 0) {
        throw DivisionByZeroError();  // Throw exception
    }
    return a / b;
}

int main() {
    try {
        int result = divide(10, 0);
        cout << "Result: " << result << endl;
    }
    catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

### 6. Templates (Generic Programming)

**C:** (Not supported - must write separate functions)
```c
#include <stdio.h>

int max_int(int a, int b) {
    return (a > b) ? a : b;
}

float max_float(float a, float b) {
    return (a > b) ? a : b;
}

char* max_string(char *a, char *b) {
    return (strcmp(a, b) > 0) ? a : b;
}
```

**C++:** (Templates - one function for all types)
```cpp
#include <iostream>
#include <string>
using namespace std;

// Template function
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << max(5, 10) << endl;           // int
    cout << max(3.14, 2.71) << endl;      // double
    cout << max("hello", "world") << endl; // const char*
    
    return 0;
}
```

---

### 7. STL vs C Standard Library

**C:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare_ints(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // Sort
    qsort(arr, n, sizeof(int), compare_ints);
    
    // Print
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
```

**C++ (STL):**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr = {5, 2, 8, 1, 9};
    
    // Sort (no comparator needed for basic types)
    sort(arr.begin(), arr.end());
    
    // Print using range-based for loop
    for (int x : arr) {
        cout << x << " ";
    }
    
    // Other STL operations
    arr.push_back(3);           // Add element
    arr.erase(arr.begin());     // Remove first element
    int max_val = *max_element(arr.begin(), arr.end());
    int count = count(arr.begin(), arr.end(), 5);
    
    return 0;
}
```

---

# PART 2: OOPs Concepts with C++

## 1. Classes and Objects

### Description
- **Class:** Blueprint/template for creating objects
- **Object:** Instance of a class
- **Access Specifiers:** private, protected, public

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    // Private members - accessible only within class
    int rollNumber;
    string name;
    float marks;
    
protected:
    // Protected members - accessible in derived classes
    string grade;
    
public:
    // Public members - accessible from anywhere
    
    // Constructor
    Student(int roll, string n, float m) {
        rollNumber = roll;
        name = n;
        marks = m;
        calculateGrade();
    }
    
    // Default constructor
    Student() {
        rollNumber = 0;
        name = "";
        marks = 0;
        grade = "F";
    }
    
    // Parameterized constructor with defaults
    Student(int roll = 0, string n = "", float m = 0) 
        : rollNumber(roll), name(n), marks(m) {
        calculateGrade();
    }
    
    // Destructor
    ~Student() {
        cout << "Student " << name << " destroyed" << endl;
    }
    
    // Getter methods (accessors)
    int getRollNumber() const { return rollNumber; }
    string getName() const { return name; }
    float getMarks() const { return marks; }
    string getGrade() const { return grade; }
    
    // Setter methods (mutators)
    void setName(string n) { name = n; }
    void setMarks(float m) { 
        marks = m; 
        calculateGrade();
    }
    
    // Member function
    void display() const {
        cout << "Roll: " << rollNumber 
             << ", Name: " << name 
             << ", Marks: " << marks 
             << ", Grade: " << grade << endl;
    }
    
private:
    // Private helper function
    void calculateGrade() {
        if (marks >= 90) grade = "A";
        else if (marks >= 80) grade = "B";
        else if (marks >= 70) grade = "C";
        else if (marks >= 60) grade = "D";
        else grade = "F";
    }
};

int main() {
    // Creating objects
    Student s1(1, "Alice", 95);
    Student s2(2, "Bob", 82);
    Student s3;  // Default constructor
    
    // Accessing members
    s1.display();
    s2.display();
    
    // Using setters/getters
    s3.setName("Charlie");
    s3.setMarks(78);
    s3.display();
    
    cout << s1.getName() << " got grade " << s1.getGrade() << endl;
    
    return 0;
}
```

---

## 2. Encapsulation

### Description
Wrapping data (variables) and code (methods) together as a single unit. Data hiding is achieved by making members private.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;
    
public:
    BankAccount(string accNum, string name, double initialBalance) {
        accountNumber = accNum;
        accountHolder = name;
        balance = initialBalance;
    }
    
    // Deposit with validation
    bool deposit(double amount) {
        if (amount <= 0) {
            cout << "Invalid deposit amount" << endl;
            return false;
        }
        balance += amount;
        cout << "Deposited: $" << amount << endl;
        return true;
    }
    
    // Withdraw with validation
    bool withdraw(double amount) {
        if (amount <= 0) {
            cout << "Invalid withdrawal amount" << endl;
            return false;
        }
        if (amount > balance) {
            cout << "Insufficient balance" << endl;
            return false;
        }
        balance -= amount;
        cout << "Withdrew: $" << amount << endl;
        return true;
    }
    
    // Get balance (read-only access)
    double getBalance() const {
        return balance;
    }
    
    // Cannot directly modify balance from outside
    // balance = -1000000;  // ERROR: balance is private
    
    void display() const {
        cout << "Account: " << accountNumber 
             << ", Holder: " << accountHolder
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount acc("12345", "John Doe", 1000);
    
    acc.deposit(500);    // Valid
    acc.withdraw(200);   // Valid
    
    // acc.balance = -500;  // ERROR: Cannot access private member
    
    acc.display();
    cout << "Current Balance: $" << acc.getBalance() << endl;
    
    return 0;
}
```

---

## 3. Inheritance

### Description
Mechanism where one class (derived/child) acquires properties of another class (base/parent).

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class
class Person {
protected:
    string name;
    int age;
    string address;
    
public:
    Person(string n = "", int a = 0, string addr = "") 
        : name(n), age(a), address(addr) {}
    
    virtual ~Person() {}
    
    void display() const {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Address: " << address << endl;
    }
    
    // Virtual function for polymorphism
    virtual void introduce() const {
        cout << "Hi, I'm " << name << endl;
    }
};

// Derived class - Single Inheritance
class Student : public Person {
private:
    int studentId;
    string major;
    vector<double> grades;
    
public:
    Student(string n, int a, string addr, int id, string m)
        : Person(n, a, addr), studentId(id), major(m) {}
    
    void addGrade(double grade) {
        grades.push_back(grade);
    }
    
    double getAverage() const {
        if (grades.empty()) return 0;
        double sum = 0;
        for (double g : grades) sum += g;
        return sum / grades.size();
    }
    
    void introduce() const override {
        cout << "Hi, I'm " << name << ", a " << major << " student" << endl;
    }
    
    void display() const {
        Person::display();
        cout << "Student ID: " << studentId << endl;
        cout << "Major: " << major << endl;
        cout << "Average Grade: " << getAverage() << endl;
    }
};

// Another derived class
class Employee : public Person {
private:
    int employeeId;
    string department;
    double salary;
    
public:
    Employee(string n, int a, string addr, int id, string dept, double sal)
        : Person(n, a, addr), employeeId(id), department(dept), salary(sal) {}
    
    void giveRaise(double percentage) {
        salary += salary * percentage / 100;
    }
    
    void introduce() const override {
        cout << "Hi, I'm " << name << ", working in " << department << endl;
    }
    
    void display() const {
        Person::display();
        cout << "Employee ID: " << employeeId << endl;
        cout << "Department: " << department << endl;
        cout << "Salary: $" << salary << endl;
    }
};

// Multilevel Inheritance
class GraduateStudent : public Student {
private:
    string thesisTopic;
    string supervisor;
    
public:
    GraduateStudent(string n, int a, string addr, int id, string m, 
                   string topic, string sup)
        : Student(n, a, addr, id, m), thesisTopic(topic), supervisor(sup) {}
    
    void display() const {
        Student::display();
        cout << "Thesis: " << thesisTopic << endl;
        cout << "Supervisor: " << supervisor << endl;
    }
};

int main() {
    // Single inheritance
    Student s("Alice", 20, "NYC", 1001, "Computer Science");
    s.addGrade(95.5);
    s.addGrade(88.0);
    s.addGrade(92.5);
    
    cout << "=== Student ===" << endl;
    s.display();
    s.introduce();
    
    cout << "\n=== Employee ===" << endl;
    Employee e("Bob", 30, "LA", 2001, "Engineering", 75000);
    e.display();
    e.introduce();
    e.giveRaise(10);
    cout << "After 10% raise:" << endl;
    e.display();
    
    cout << "\n=== Graduate Student (Multilevel) ===" << endl;
    GraduateStudent gs("Charlie", 25, "Boston", 3001, "AI", 
                       "Machine Learning", "Dr. Smith");
    gs.addGrade(98.0);
    gs.display();
    
    return 0;
}
```

---

## 4. Polymorphism

### Description
Ability to take different forms. Two types:
- **Compile-time:** Function overloading, operator overloading
- **Run-time:** Virtual functions (function overriding)

### A. Compile-time Polymorphism (Function Overloading)

```cpp
#include <iostream>
using namespace std;

class Calculator {
public:
    // Function overloading - same name, different parameters
    
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
    
    string add(string a, string b) {
        return a + b;
    }
};

int main() {
    Calculator calc;
    
    cout << calc.add(5, 10) << endl;           // int
    cout << calc.add(5.5, 10.2) << endl;       // double
    cout << calc.add(1, 2, 3) << endl;         // 3 params
    cout << calc.add("Hello", " World") << endl; // string
    
    return 0;
}
```

### B. Operator Overloading

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
    double real, imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Overloading + operator
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    
    // Overloading - operator
    Complex operator-(const Complex& other) const {
        return Complex(real - other.real, imag - other.imag);
    }
    
    // Overloading * operator
    Complex operator*(const Complex& other) const {
        // (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        return Complex(
            real * other.real - imag * other.imag,
            real * other.imag + imag * other.real
        );
    }
    
    // Overloading << operator (must be friend)
    friend ostream& operator<<(ostream& os, const Complex& c);
    
    // Overloading == operator
    bool operator==(const Complex& other) const {
        return real == other.real && imag == other.imag;
    }
};

ostream& operator<<(ostream& os, const Complex& c) {
    os << c.real;
    if (c.imag >= 0) os << "+";
    os << c.imag << "i";
    return os;
}

int main() {
    Complex c1(3, 4);
    Complex c2(1, 2);
    
    Complex sum = c1 + c2;      // Uses operator+
    Complex diff = c1 - c2;     // Uses operator-
    Complex prod = c1 * c2;     // Uses operator*
    
    cout << "c1 = " << c1 << endl;
    cout << "c2 = " << c2 << endl;
    cout << "c1 + c2 = " << sum << endl;
    cout << "c1 - c2 = " << diff << endl;
    cout << "c1 * c2 = " << prod << endl;
    
    if (c1 == c1) {
        cout << "c1 equals itself" << endl;
    }
    
    return 0;
}
```

### C. Run-time Polymorphism (Virtual Functions)

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Base class with virtual function
class Shape {
protected:
    string color;
    
public:
    Shape(string c = "white") : color(c) {}
    virtual ~Shape() {}
    
    // Virtual function - can be overridden
    virtual double area() const {
        return 0;
    }
    
    // Pure virtual function - makes class abstract
    virtual double perimeter() const = 0;
    
    virtual void draw() const {
        cout << "Drawing a shape" << endl;
    }
    
    string getColor() const { return color; }
};

// Derived class
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r, string c = "red") : Shape(c), radius(r) {}
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * 3.14159 * radius;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " circle" << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h, string c = "blue") 
        : Shape(c), width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " rectangle" << endl;
    }
};

class Triangle : public Shape {
private:
    double a, b, c;  // sides
    
public:
    Triangle(double a, double b, double c, string c = "green")
        : Shape(c), a(a), b(b), c(c) {}
    
    double area() const override {
        // Heron's formula
        double s = (a + b + c) / 2;
        return sqrt(s * (s-a) * (s-b) * (s-c));
    }
    
    double perimeter() const override {
        return a + b + c;
    }
    
    void draw() const override {
        cout << "Drawing a " << color << " triangle" << endl;
    }
};

int main() {
    // Vector of base class pointers (polymorphism)
    vector<Shape*> shapes;
    
    shapes.push_back(new Circle(5));
    shapes.push_back(new Rectangle(4, 6));
    shapes.push_back(new Triangle(3, 4, 5));
    
    // Runtime polymorphism - correct function called
    for (Shape* shape : shapes) {
        shape->draw();  // Calls derived class's draw()
        cout << "Area: " << shape->area() << endl;
        cout << "Perimeter: " << shape->perimeter() << endl;
        cout << "---" << endl;
    }
    
    // Cleanup
    for (Shape* shape : shapes) {
        delete shape;
    }
    
    return 0;
}
```

---

## 5. Abstraction

### Description
Hiding implementation details and showing only essential features.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Abstract class (interface-like)
class Database {
public:
    virtual ~Database() {}
    
    // Pure virtual functions - abstract interface
    virtual bool connect() = 0;
    virtual void disconnect() = 0;
    virtual void query(string sql) = 0;
    virtual vector<string> fetchAll(string sql) = 0;
};

// Concrete implementation - MySQL
class MySQLDatabase : public Database {
private:
    string host;
    string user;
    string password;
    bool connected;
    
public:
    MySQLDatabase(string h, string u, string p)
        : host(h), user(u), password(p), connected(false) {}
    
    bool connect() override {
        cout << "Connecting to MySQL at " << host << endl;
        // Actual connection logic here
        connected = true;
        return connected;
    }
    
    void disconnect() override {
        cout << "Disconnecting from MySQL" << endl;
        connected = false;
    }
    
    void query(string sql) override {
        if (!connected) {
            cout << "Not connected to database" << endl;
            return;
        }
        cout << "Executing MySQL query: " << sql << endl;
        // Execute query logic
    }
    
    vector<string> fetchAll(string sql) override {
        cout << "Fetching results from MySQL" << endl;
        return {"row1", "row2", "row3"};  // Mock data
    }
};

// Concrete implementation - PostgreSQL
class PostgreSQLDatabase : public Database {
private:
    string host;
    bool connected;
    
public:
    PostgreSQLDatabase(string h) : host(h), connected(false) {}
    
    bool connect() override {
        cout << "Connecting to PostgreSQL at " << host << endl;
        connected = true;
        return connected;
    }
    
    void disconnect() override {
        cout << "Disconnecting from PostgreSQL" << endl;
        connected = false;
    }
    
    void query(string sql) override {
        if (!connected) return;
        cout << "Executing PostgreSQL query: " << sql << endl;
    }
    
    vector<string> fetchAll(string sql) override {
        return {"pg_row1", "pg_row2"};
    }
};

// Usage - client code doesn't care about implementation
class UserRepository {
private:
    Database* db;
    
public:
    UserRepository(Database* database) : db(database) {}
    
    void getUser(int id) {
        db->connect();
        db->query("SELECT * FROM users WHERE id = " + to_string(id));
        auto results = db->fetchAll("SELECT * FROM users");
        db->disconnect();
    }
};

int main() {
    // Can't instantiate abstract class
    // Database* db = new Database();  // ERROR!
    
    // Use concrete implementations
    Database* mysqlDb = new MySQLDatabase("localhost", "root", "password");
    Database* pgDb = new PostgreSQLDatabase("192.168.1.100");
    
    UserRepository mysqlRepo(mysqlDb);
    UserRepository pgRepo(pgDb);
    
    // Same interface, different implementations
    mysqlRepo.getUser(1);
    pgRepo.getUser(1);
    
    delete mysqlDb;
    delete pgDb;
    
    return 0;
}
```

---

# PART 3: DSA Implementation in C

## Arrays in C

```c
#include <stdio.h>
#include <stdlib.h>

// Dynamic Array structure
typedef struct {
    int* data;
    int size;
    int capacity;
} DynamicArray;

// Initialize array
void init_array(DynamicArray* arr, int capacity) {
    arr->data = (int*)malloc(capacity * sizeof(int));
    arr->size = 0;
    arr->capacity = capacity;
}

// Resize array
void resize_array(DynamicArray* arr) {
    int new_capacity = arr->capacity * 2;
    arr->data = (int*)realloc(arr->data, new_capacity * sizeof(int));
    arr->capacity = new_capacity;
}

// Append element
void append(DynamicArray* arr, int value) {
    if (arr->size == arr->capacity) {
        resize_array(arr);
    }
    arr->data[arr->size++] = value;
}

// Get element
int get(DynamicArray* arr, int index) {
    if (index < 0 || index >= arr->size) {
        printf("Index out of bounds\n");
        return -1;
    }
    return arr->data[index];
}

// Delete element
void delete_element(DynamicArray* arr, int index) {
    if (index < 0 || index >= arr->size) return;
    for (int i = index; i < arr->size - 1; i++) {
        arr->data[i] = arr->data[i + 1];
    }
    arr->size--;
}

// Free memory
void free_array(DynamicArray* arr) {
    free(arr->data);
    arr->data = NULL;
    arr->size = 0;
    arr->capacity = 0;
}

// Print array
void print_array(DynamicArray* arr) {
    printf("[");
    for (int i = 0; i < arr->size; i++) {
        printf("%d", arr->data[i]);
        if (i < arr->size - 1) printf(", ");
    }
    printf("]\n");
}

int main() {
    DynamicArray arr;
    init_array(&arr, 4);
    
    append(&arr, 10);
    append(&arr, 20);
    append(&arr, 30);
    append(&arr, 40);
    append(&arr, 50);  // Triggers resize
    
    print_array(&arr);
    
    printf("Element at index 2: %d\n", get(&arr, 2));
    
    delete_element(&arr, 1);
    print_array(&arr);
    
    free_array(&arr);
    return 0;
}
```

## Linked List in C

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Linked List structure
typedef struct {
    Node* head;
    Node* tail;
    int size;
} LinkedList;

// Create new node
Node* create_node(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Initialize list
void init_list(LinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
}

// Insert at beginning
void prepend(LinkedList* list, int data) {
    Node* node = create_node(data);
    if (list->head == NULL) {
        list->head = list->tail = node;
    } else {
        node->next = list->head;
        list->head = node;
    }
    list->size++;
}

// Insert at end
void append(LinkedList* list, int data) {
    Node* node = create_node(data);
    if (list->tail == NULL) {
        list->head = list->tail = node;
    } else {
        list->tail->next = node;
        list->tail = node;
    }
    list->size++;
}

// Delete by value
int delete_value(LinkedList* list, int data) {
    if (list->head == NULL) return 0;
    
    Node* current = list->head;
    Node* prev = NULL;
    
    while (current != NULL) {
        if (current->data == data) {
            if (prev == NULL) {
                list->head = current->next;
            } else {
                prev->next = current->next;
            }
            if (current == list->tail) {
                list->tail = prev;
            }
            free(current);
            list->size--;
            return 1;
        }
        prev = current;
        current = current->next;
    }
    return 0;
}

// Search
int search(LinkedList* list, int data) {
    Node* current = list->head;
    int index = 0;
    while (current != NULL) {
        if (current->data == data) return index;
        current = current->next;
        index++;
    }
    return -1;
}

// Reverse
void reverse(LinkedList* list) {
    Node* prev = NULL;
    Node* current = list->head;
    Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    list->tail = list->head;
    list->head = prev;
}

// Print list
void print_list(LinkedList* list) {
    Node* current = list->head;
    printf("[");
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) printf(" -> ");
        current = current->next;
    }
    printf("]\n");
}

// Free list
void free_list(LinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        Node* next = current->next;
        free(current);
        current = next;
    }
    list->head = list->tail = NULL;
    list->size = 0;
}

int main() {
    LinkedList list;
    init_list(&list);
    
    append(&list, 10);
    append(&list, 20);
    append(&list, 30);
    prepend(&list, 5);
    
    print_list(&list);  // [5 -> 10 -> 20 -> 30]
    
    printf("Search 20: index %d\n", search(&list, 20));
    
    delete_value(&list, 10);
    print_list(&list);  // [5 -> 20 -> 30]
    
    reverse(&list);
    print_list(&list);  // [30 -> 20 -> 5]
    
    free_list(&list);
    return 0;
}
```

## Stack in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int* data;
    int top;
    int capacity;
} Stack;

void init_stack(Stack* stack, int capacity) {
    stack->data = (int*)malloc(capacity * sizeof(int));
    stack->top = -1;
    stack->capacity = capacity;
}

bool is_empty(Stack* stack) {
    return stack->top == -1;
}

bool is_full(Stack* stack) {
    return stack->top == stack->capacity - 1;
}

void push(Stack* stack, int value) {
    if (is_full(stack)) {
        printf("Stack overflow\n");
        return;
    }
    stack->data[++stack->top] = value;
}

int pop(Stack* stack) {
    if (is_empty(stack)) {
        printf("Stack underflow\n");
        return -1;
    }
    return stack->data[stack->top--];
}

int peek(Stack* stack) {
    if (is_empty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->data[stack->top];
}

void free_stack(Stack* stack) {
    free(stack->data);
}

int main() {
    Stack stack;
    init_stack(&stack, 5);
    
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    
    printf("Top: %d\n", peek(&stack));  // 30
    printf("Pop: %d\n", pop(&stack));   // 30
    printf("Pop: %d\n", pop(&stack));   // 20
    
    free_stack(&stack);
    return 0;
}
```

## Queue in C

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int* data;
    int front;
    int rear;
    int size;
    int capacity;
} Queue;

void init_queue(Queue* queue, int capacity) {
    queue->data = (int*)malloc(capacity * sizeof(int));
    queue->front = 0;
    queue->rear = -1;
    queue->size = 0;
    queue->capacity = capacity;
}

bool is_empty(Queue* queue) {
    return queue->size == 0;
}

bool is_full(Queue* queue) {
    return queue->size == queue->capacity;
}

void enqueue(Queue* queue, int value) {
    if (is_full(queue)) {
        printf("Queue is full\n");
        return;
    }
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->data[queue->rear] = value;
    queue->size++;
}

int dequeue(Queue* queue) {
    if (is_empty(queue)) {
        printf("Queue is empty\n");
        return -1;
    }
    int value = queue->data[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return value;
}

void free_queue(Queue* queue) {
    free(queue->data);
}

int main() {
    Queue queue;
    init_queue(&queue, 5);
    
    enqueue(&queue, 10);
    enqueue(&queue, 20);
    enqueue(&queue, 30);
    
    printf("Dequeue: %d\n", dequeue(&queue));  // 10
    printf("Dequeue: %d\n", dequeue(&queue));  // 20
    
    free_queue(&queue);
    return 0;
}
```

---

# PART 4: DSA Implementation in C++ (Using STL)

## Vectors (Dynamic Arrays)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Create vectors
    vector<int> v1;                    // Empty
    vector<int> v2(5);                 // Size 5, initialized to 0
    vector<int> v3(5, 10);             // Size 5, all 10s
    vector<int> v4 = {1, 2, 3, 4, 5};  // Initializer list
    
    // Basic operations
    v1.push_back(10);
    v1.push_back(20);
    v1.push_back(30);
    
    cout << "Size: " << v1.size() << endl;
    cout << "Capacity: " << v1.capacity() << endl;
    
    // Access
    cout << "Element at 1: " << v1.at(1) << endl;
    cout << "Front: " << v1.front() << endl;
    cout << "Back: " << v1.back() << endl;
    
    // Modify
    v1[1] = 25;
    
    // Remove
    v1.pop_back();
    
    // Insert
    v1.insert(v1.begin(), 5);      // At beginning
    v1.insert(v1.begin() + 2, 15); // At position
    
    // Erase
    v1.erase(v1.begin());          // First element
    v1.erase(v1.begin(), v1.begin() + 2); // Range
    
    // Sort
    sort(v1.begin(), v1.end());
    
    // Reverse
    reverse(v1.begin(), v1.end());
    
    // Find
    auto it = find(v1.begin(), v1.end(), 20);
    if (it != v1.end()) {
        cout << "Found 20 at position " << distance(v1.begin(), it) << endl;
    }
    
    // Range-based for loop
    cout << "Vector: ";
    for (int x : v1) {
        cout << x << " ";
    }
    cout << endl;
    
    return 0;
}
```

## Maps and Sets

```cpp
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
using namespace std;

int main() {
    // Map (sorted by key)
    map<string, int> grades;
    grades["Alice"] = 95;
    grades["Bob"] = 87;
    grades["Charlie"] = 92;
    
    // Access
    cout << "Alice: " << grades["Alice"] << endl;
    cout << "Size: " << grades.size() << endl;
    
    // Iterate
    cout << "All grades (sorted by name):" << endl;
    for (auto pair : grades) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    // Check if exists
    if (grades.find("Bob") != grades.end()) {
        cout << "Bob exists" << endl;
    }
    
    // Remove
    grades.erase("Bob");
    
    // Unordered map (faster, not sorted)
    unordered_map<string, int> fastGrades;
    fastGrades["Alice"] = 95;
    
    // Set (sorted, unique)
    set<int> uniqueNumbers;
    uniqueNumbers.insert(5);
    uniqueNumbers.insert(3);
    uniqueNumbers.insert(5);  // Duplicate, ignored
    uniqueNumbers.insert(1);
    
    cout << "Set: ";
    for (int n : uniqueNumbers) {
        cout << n << " ";  // 1 3 5
    }
    cout << endl;
    
    // Unordered set
    unordered_set<int> fastSet;
    fastSet.insert(10);
    fastSet.insert(20);
    
    return 0;
}
```

---

# Quick Reference: C vs C++ for DSA

| Task | C | C++ |
|------|---|-----|
| **Dynamic Array** | Manual malloc/realloc | `vector<int>` |
| **String** | `char[]` with strcpy | `string` |
| **Sort** | `qsort()` with comparator | `sort(v.begin(), v.end())` |
| **Map** | Manual hash table | `map<K,V>` or `unordered_map<K,V>` |
| **Stack** | Manual array/linked list | `stack<int>` |
| **Queue** | Manual circular buffer | `queue<int>` |
| **Memory** | malloc/free | new/delete or automatic |
| **Functions** | Pass by value/pointer | Pass by reference `&` |

---

# Practice Problems

## C Problems
1. Implement Dynamic Array
2. Implement Linked List with all operations
3. Implement Stack using array and linked list
4. Implement Queue using array and linked list
5. Implement Binary Search
6. Implement Sorting algorithms (Bubble, Merge, Quick)
7. Implement Hash Table with collision handling

## C++ Problems (Using STL)
1. Two Sum (use unordered_map)
2. Valid Anagram (use map)
3. Group Anagrams (use map<string, vector<string>>)
4. Top K Frequent Elements (use map + vector + sort)
5. Merge Intervals (use vector + sort)
6. Valid Parentheses (use stack)
7. LRU Cache (use unordered_map + list)
