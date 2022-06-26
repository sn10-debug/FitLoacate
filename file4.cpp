#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;






class Employee{

    private:
        string Name;
        string Designation;
        long double Salary;
        static int Employee_Number;

    public:


    static int get_employee_number(){
        return Employee_Number;
    }

    Employee(string name="New Employee",string designation="Sigma Employee",long double salary=0):Name{name},Designation{designation},Salary{salary}{

        cout<<"New Employee is Created"<<endl;
        Employee_Number++;
    }


    Employee(const Employee &source):Name{source.Name},Designation{source.Designation},Salary{source.Salary}{

        cout<<"Object is Successfully copied"<<endl;
    }

    string get_Employee_name() const{
        // The const qualifier should be passes after the initializer list and this is const correctness
            return Name;
    }

    // This is a copy constructor

    ~Employee(){
        cout<<"Destructor is successfully called"<<endl;
        Employee_Number--;
    }






};


int Employee::Employee_Number=0;


Employee Employee_details(){
    string name,designation;
    long double salary;
    cout<<"Enter the name of the Employee : ";
    getline(cin,name);
    cout<<"Enter the Designation of the Employee : ";
    getline(cin,designation);
    cout<<"Enter the Salary of the Employee : ";
    cin>>salary;

    Employee Employee_{name,designation,salary};

    cout<<"The Address of the Employee is : "<<&Employee_<<endl;
    return Employee_;


}



//MOve Constructor


class Address{



    public:
    string *data;


    Address(string data="") {

        this->data=new string{data};
        //  this->data=new string{};
        //  this is a pointer to the object same as used in javascript
        // this is only accessible inside the class scope
        // *data=addr_;

    }


    Address(const Address &source): Address(*source.data) {

        cout<<"Copy Constructor-deep copy is Called"<<endl;
    };

    Address(Address &&source):Address(*source.data){
        source.data=nullptr;
        cout<<"Move Constructor is Called"<<endl;
    }

    ~Address(){

        if (data!=nullptr)
            cout<<"Destructor is Called for "<<*data<<endl;
        else cout<<"Destructor is called for nullptr"<<endl;
        delete data;
    }


    
    
};



void change_data(Address addr){

}


#include <cstring>
void take(const char *s){
    
    // We can directly pass string into these instead of address

    cout<<s<<endl;
    // As it is a C-style string We can directly display it
    cout<<strlen(s)<<endl;

    
}






int main(){

    // Employee Employee1=Employee_details();
    Employee Employee1 {"ABC","MD",7881188};

    // This is returned by reference

    cout<<"Copying the object "<<endl;

    Employee Employee2 {Employee1};

    // This created a copy


    cout<<"The Address of the returned Employee  1 is : "<<&Employee1<<endl;
    cout<<"The Address of the returned Employee  2 is : "<<&Employee2<<endl;
    

    // If we don't create a copy constructor then C++ automatically creates copy constructor



    // Move constructors and this was introduced C++11

    // Creating a reference to r-value

    int x{100};

    int &&y=100;
    y=200;

    // int &&z=x;
    // This will generate an error because we are assigning a l-value to r-value reference

    int &z=x;
    // This will work because we are assigning a l-value to a l-value reference


// Sometimes copy constructors are not called and this is due compiler optimization which is return value optimization
// This means when a object is returned by function compiler does not makes the copy of the objects and stores in the variable

int total{0};
total=100+400;

// Here 100+400 is evaluated first and then stored in a temp value and then it is stored in the total variable
// There will be lot of copy constructors

// C++11 instroduced move semantics and the move constructors

// Move constructor moves the object rather than copy 


Address address1 {"Hello World This is Address 1"};
Address address2{address1};

*address2.data="Hello this is Address 2";

vector <Address> addr_list{};

Address address3{Address {"Hello this is address 3"}};

addr_list.push_back(Address {"Hello this is Address 1 of vector"});

// Here first the Address is stored in a temp value and then copied so copy constructor is called and then the destructor for the temp before delcaring a move constructor

// Address {"Hello this is address 1 of vector"} as this is an r-value therefore the move constructor will be called


cout<<ceil(5.0/2)<<endl;



// When we declare a object with const we cannot change its attributes

// If we try to use the getter functions in the const objects then also it will give error

// So the solution is declare functions with const qualifiers and then we can use the method in a const object and if once the function is called but if it finds that the function is trying to change any of attributes it will generate compiler error




const Employee Employee_4 {"ABC","MD",1101010};

cout<<Employee_4.get_Employee_name()<<endl;

// Without declaring const qualifier with the methods we cannot use this

// return value func_name(parameters) const ;



// Static class members

// This are attributes or function which belongs to the class as well not only the objects

cout<<"Total Number of Employees is : "<<Employee::get_employee_number()<<endl;
cout<<"Total Number of Employees is : "<<Employee1.get_employee_number()<<endl;


// Static functions only have access to static data members which is quite logical


// If we just declare the prototype of the static member function and if we want to declare it in some other place and so while doing that we don't need to write 'static' while writing the return type


// By default in the struct all the members are public but in class by default they are private and we need to manually declare them public



struct Member{
    private:
    string ID;
    public:
    string Name;

    Member(string name):Name{name}{
        ID="Hello "+Name;
    }

    string get_id(){
        return ID;
    }

    
};


Member Member_1{"Shakti Santosh Nayak"};
// Member_1.Name="Shakti Santosh Nayak";

cout<<Member_1.Name<<endl;
cout<<Member_1.get_id()<<endl;

// We can declare private and public in a structure


// Operator Overloading allow programmers to overload most of the operators to work with user defined classes

// This allows to make our code more readable and writable

// In C++ we have seen that we can use the operators are used with C++ built in types only
// We know + operator was used to add integers,doubles,floats
// But there is operator overloading in them also that is they can be used with two different primitive data types that is we can integers and doubles,doubles and floats and we have already seen that we have integer division ,float division

// C++ allows use to overload operators for our own user defined types

// The only operator which C++ which provides for default implementation that is the operator we can use for user-defined data types is assignment operator (=)

// That s because the compiler may assign one object to another

// All other operators has to explicitly overloaded by the programmers

// We can overload majority of operators but the ones we cannot overload is scope resolution operator (::), conditional operator (:'' ? '') , pointer to member operator (.*),dot operator (.), sizeof operator
cout<<"Size of Integer is : "<<sizeof(int)<<endl;

// When your overloading operator the precedence and associativity cannot be changed

// 'arity' of a operator cannot be changed if the operator works with two arguements that is binary than it cannot be changed to unary while operator overloading

// We cannot overload operators and change the way how they work with the primitive data types

// Operators can be overloaded using function and member methods

// char text1[] {"Shakti"};

// cout<<text1<<endl;




// take("Shak\0ti");

// This will give 4 as there is null character after 'k'


// C++ provides a default assignment operator for assigning one object to another



Employee Employee_5=Employee_4;

// This is not assignment this is intialization


Employee_5=Employee2;

// This is assignment and this is same like copy constructor where it does memberwise copy

// This will be problematic when we will use a raw pointer










    return 0;
}

