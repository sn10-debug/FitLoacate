#include <iostream>
#include <string.h>
#include <vector>
#include <cstring>
#include <math.h>
#include <memory>

using namespace std;



class Customer{
public :
static int num_customers;
string Name;
int age;



static void increase(){
num_customers++;
}

Customer(string name="New User",int age_=1):Name{name},age{age_}{

increase();    
cout<<"New Customer is Created"<<endl;

}

Customer(const Customer &source):Name{source.Name},age{source.age}{}





};



class Account{

friend void change_text(Account &source);
protected:
string private_key;
double Account_Balance;
string Public_key;

static constexpr int Company_Number {150847};
static constexpr const char* name ="Sigma";

private:
string text;


public:
const string* const pub_key;
const double* const acc_ba;


Account(string pu_k="Not Available",string priv_k="Available"):Public_key{pu_k},private_key{priv_k},Account_Balance{0},pub_key{&Public_key},acc_ba{&Account_Balance}{

    cout<<"Account Successfully Created "<<endl;
}


void deposit(double amount){

    Account_Balance+=amount;
}

void withdraw(double amomunt){

    if (Account_Balance>=amomunt) Account_Balance-=amomunt;
}



};


class Personal_Account:public Account{

string Name;
string pin;
public:
const string* const name_p;

Personal_Account(string name="New user",string pin_="0000",string p_key="Not Available",string priv_key="Not Available"):Name{name},name_p{&Name}{
Public_key=p_key;
private_key=priv_key;
Account_Balance=0;
pin=pin_;
}

void Change_Name(string pin,string Name){
    if (pin==this->pin) {this->Name=Name;
    cout<<"Your name is Successfully changed \n";
    }
    else cout<<"You have entered an wrong pin \n";
}


void deposit(double amount){
    Account_Balance+=10;
    Account::deposit(amount);

    // This will overwrite the existing deposit method of the Account class and also delegated some part to Account deposit method
}



};


class Business_Account : public Account{
    string Business_Name;
    
};


void change_text(Account &source){
    source.text="Hello World ";
}



class Base{
    public:
int num;


virtual void greeting(){
    cout<<"Hello this is Base class \n";
}

Base(){
    cout<<"Constructor for Base is called "<<endl;
}

Base(const Base &source):num{source.num}{

    cout<<"Copy constructor for the Base class is Called \n";
}

Base (int x):num{x}{
    cout<<"Constructor for Base with one integer called \n";
}


Base(const Base &&source):num{source.num}{
    cout<<"Move Constructor is Called\n";
}

Base& operator=(const Base &rhs){
    if(this!=&rhs) this->num=rhs.num;
    return *this;
}


virtual ~Base(){
    // cout<<"Destructor for Base is called "<<endl;
}


};


class Derived_1:public Base{

    using Base::Base;

    // If we provide an integer to a Derived class  without declaring a constructor which expects a integer then if it is not present then it will see into the constructor of the base which expects a integer and that will be called and if the constructor in the derived class is present which expects a integer then it will be called and no-args constructor of the Base class will be called
    
    private:
    int num_1;
    public:
    int num_derived;

    Derived_1(){
        cout<<"Constructor for Derived class is called "<<endl;
    }

    

     ~Derived_1(){
        // cout<<"Destructor for Derived class is called "<<endl;
    }

    friend class Derived_2;

};

class Derived_2:public Base{
    
public:
int num_derived;

// void greeting() const override{
//     cout<<"Hello this is derived 2 class \n";
// }

void greeting() override{
    cout<<"Hello this is derived 2 class \n";
}

Derived_2(int x=0):Base{x},num_derived{3*x}{
// This will call the overloaded constructor of the base class which expects a integer
}

Derived_2(const Derived_2 &source):Base{source},num_derived{source.num_derived}{
    cout<<"Copy constructor of Derived class is called "<<endl;

    // We are invoking a copy constructor for the Base class from the Derived class though we didn't inherited

    // We are passing a Derived object into a Base copy constructor which expects a Base object but this works because we know over here in public inheritance which is "IS-A" relationship and here  the Derived object is a Base Object and therefore the Base constructor will slice out the Base object from the Derived object and the source in Base copy constructor will be Base object  
}


Derived_2& operator=(const Derived_2 &rhs){
    if (this!=&rhs) {
    Base::operator=(rhs);
    this->num_derived=rhs.num_derived;
    }

    // This is overloaded assignment
    
    return *this;

}

Derived_2 (const Derived_2 &&source) : Base {source} ,num_derived {source.num_derived}{
    cout<<"Move Constructor is Called \n";

    // This is similar to copy constructor
}


~Derived_2(){
    // Derived_1 hello {};
    // hello.num_1=20;
}



};



class Derived_3:public Derived_2{
    public:
    void greeting(){
        cout<<"This is derived 3 class\n";
    }
};

typedef struct  Tire
{   public:
    double diameter;
    double height;
    double Area;
    double Cost;


    Tire(double diameter_,double height_):diameter{diameter_},height{height_}{
        Area=3.14*diameter*height*2.5*2.5;
        Cost=75*Area;
    }

    
} Tire;



class Base_2 final{

    Base_2(){
        cout<<"Hello world\n";
    }

};

class Base_3 {
    public:

    Base_3(){
        cout<<"Hello world\n";
    }


    virtual void greet() final{
        cout<<"Hello this is Base 3\n";
    }
    

    virtual void class_name(){
        cout<<"Class Name : Base-3\n";
    }

};





// class Derived_3 :public Base_2{
// This will give an error as we have declared Base_2 as final
// };


class Derived_4 final : public Base_3{
    public:

    Derived_4(){
        cout<<"This is Final derived class\n";
    }

    // void greet(){
    //     // This will give an error as greet is declared with final specifier in the base class and greet cannot be overidden in the hierarchy
    //     cout<<"This is Derived 4 class\n";
    // }

    void class_name() override{
        cout<<"Class Name : Derived-4\n";
    }


};

// class Derived_5:public Derived_4{

//     // This also gives an error

// };



void disp_name(Base_3 &ref){
    ref.class_name();
}



class file{
    public:
virtual void open()=0;
virtual void close()=0;

virtual ~file(){}
};



class c_file :public file{
    // Abstract class
    public:
    string name;

    c_file(string name_="New File"):name{name_}{

    }
    virtual void open(){
        cout<<"Opening the file "<<name<<"\n";
    }
    virtual void close(){
         cout<<"Closing the file "<<name<<"\n";
    }

};



int main()
{

    Account Account_1{"185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969","78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524"};
    cout<<*Account_1.pub_key<<endl;

   

//    When one class is inherited from a single base class then it is called as single inheritance
// wWhen one class is inherited from two or more base classes then it called as multiple inheritance

// The base class is also called as super class
// Generalization is combining several classes with the help of common attributes

// Specialization is deriving a class from a general with some add-on's like adding some new attributes and functions

// As we go up in the Hierarchy the generalization increases and as we go down the hierarchy the specilization increases


// A
// | |
// B  C
//    |
//    D
//    |
//    E

// This is the hierarchy and A can be called as the root class
// B and C can be called as child class of A
// A is parent class of B and C
// D is derived from C
// E is derived from D
// Inheritance is transitive that E is also C and E is also A
// E is D
// This is known as Is-A Relationship
// B is not a C
// In this hierarchy A is the most generalized class
// Is-A Relationship is not bidirectional


// For example Building is a root Class
// School and Society are the child class of Building
// Building has a NOC
// School is a Building and this follows 'IS-A' relationship and this public inheritance
// Building has a NOC and this is called as composition 
// As Building has a NOC then school also has a NOC
// When 'IS-A' relationship makes sense then use public inheritance


// If we don't provide a access specifier while inheritance then by default takes it as private

// Public Inheritance follows "IS-A" relationship


Personal_Account personal_account_1 {};
cout<<*personal_account_1.pub_key<<endl;

cout<<*personal_account_1.name_p<<endl;
// personal_account_1.Name="Shakti Santosh Nayak";

personal_account_1.Change_Name("0000","My Account");
cout<<*personal_account_1.name_p<<endl;



// The Protected class members of the base class are accessible from the Derived Class but not accessible from the objects of either base class or protected class



// In case of public inheritance the public,protected,private base class members remain public,protected,private respectively and private members of base class cannot be accessed in the derived class.
// In case of protected inheritance the public,protected,private base class members remain protected,protected,private respectively and private members of base class cannot be accessed in the derived class.
// In case of public inheritance the public,protected,private base class members remain private,private,private respectively and private members of base class cannot be accessed in the derived class but all other are accessible because private members of the derived class are accessible within the base class


// friend function have access to all the class members whether it is public,private or protected.





// When a derived class object is created the constructor of the base class is first executed then the constructor of the derived class is executed


// When a destructor is called then destructor for the derived class is called first and then the destructor for the base class is called which is just reverse of the constructor sequence and also this is logical



// cout<<"-----------------Base class------------------- \n";
// Base base_1 {};

cout<<"-----------------Derived class---------------- \n";
Derived_1 derived_1 {};


// A Derived Class does not inherit Base Class Constructors, Base class Destructors, Base class overloaded assignment operators,Base class friend functions

// There are certain with which we can inherit the constructor



Derived_1 derived_2 {20};

cout<<derived_2.num<<" "<<derived_2.num_derived<<endl;

Derived_2 derived_3 {100};

cout<<derived_3.num<<" "<<derived_3.num_derived<<endl;

Derived_2 derived_4{};

cout<<derived_4.num<<" "<<derived_4.num_derived<<endl;

Derived_2 derived_5 {20};

cout<<derived_5.num<<" "<<derived_5.num_derived<<endl;


Derived_2 derived_6 {derived_5};

cout<<derived_6.num<<" "<<derived_6.num_derived<<endl;


Derived_2 derived_7 {Derived_2 {30}};

cout<<derived_7.num<<" "<<derived_7.num_derived<<endl;

vector <Derived_2> derived_object_list_1;
derived_object_list_1.push_back(Derived_2 {40});

cout<<derived_object_list_1.at(0).num<<" "<<derived_object_list_1.at(0).num_derived<<endl;

Derived_2 derived_8;

derived_8=derived_7;

cout<<derived_8.num<<" "<<derived_8.num_derived<<endl;







// Copy and move constructors are not inherited from the base class



 cout<<ceil(tan(3.14/4))<<endl;


 Tire Tire_1 {2,2};

cout<<Tire_1.Cost<<endl;




// By default C++ does static binding of Methods calls

// This means C++ decides which methods has to be called based on what it sees during the compile time

Personal_Account Account_2 {"Shakti Santosh Nayak","1234","hhdhhdhdhd","jdjdjdjdjdjdj"};

Account_2.deposit(20);

cout<<*Account_2.acc_ba<<endl;

// In order to overwrite the method of Base class in Derived Class we have to use to same signature in Derived Class as per used in the Base Class



cout.precision(2);
cout<<fixed;



// Polymorphism is a fundamental of Object oriented programming
// This allows us to write programs more abstractly

// There are two types of polymorphism that is Compile-time and Run-time
// Compile-time polymorphism includes function overloading and operator overloading
// Run-time polymorphism includes function overriding

Base *ptr=new Derived_2{};
// ptr->greeting();
// Here this is a Base class will be displayed because pointer points to a Base object though we allocated space for Derived_2 object
// But when this is a Derived class will display that will be called run-time polymorphism

// here in run-time polymorphism the method call will not be binded at the compile-time instead during the runtime it will checked to what type of object the pointer has allocated space and its method will be called at the runtime 

// Then the greeting method will be virtual in Base class during runtime polymorphism


// This all are known as dynamic binding




// For Dynamic polymorphism we must have:

// Inheritance
// Base class pointers or Base class reference
// Virtual functions




// Declare the function as virtual in the Base class which you want to override


cout<<"*************Dynamic Polymorphism*****************"<<endl;


Base *ptr_2=new Derived_2;
ptr_2->greeting();


Base *ptr_3=new Derived_3();
ptr_3->greeting();


// If once function  in Base class is declared as a virtual in the hierarchy then it will be virtual throughout the hierarchy

// If we want to override a function then we have to declare with same return type and signature

// Using Base class pointers only the methods are dynamically bound


// When we declare virtual functions then we have to declare virtual destructors

// If we don't delete virtual destructors then destructor of Base class will be called instead of calling the Derived class's destructor

// These may lead to memory leaks

// Sometimes we tend to make a mistake in writing the signature of virtual function and thus in this case it will redefinition not virtual function

// In order to prevent this we can use override specifier and the compiler will show error and thus we can solve it



delete ptr_3;
delete ptr_2;
delete ptr;



// using final specifier with a class helps prevent the class from get subclassed or being base class of a derived class

// This may be done to ensure copying without slicing

// This can also be applied at the function or method level and restrict the function or method from getting overridden



// Base class references





Base_3 obj_1 {};
Derived_4 obj_2{};


disp_name(obj_1);
disp_name(obj_2);


// This everything helps to think abstractly like in a more generalised way which is very powerful and logical

// Abstract classes are the classes which cannot be initialized and mostly they are Base class which is quite logical and more of generalized class

// Concrete classes are the classes we have been using so far and they need to be initialized with some data to store in the attributes

// To be a abstract Base class , the Base class must contain atleast one pure virtual function

// Syntax of declaring a pure virtual function 

// virtual void funtion_name()=0;

// Abstract class can contain some basic functionalities which a Derived class necessarily have these functionalites

// But if we try to initiate a abstract class it will generate a compiler error and if we also try to allocate space on the heap it will also generate a compiler error but we can use it as Base class pointers or references inorder to use dynamic binding or dynamic polymorphism





// file file_1 {};

// This will give an error because file is an abstract class and contains atleast one virtual function


// file *ptr=new file();

// This also will give an error which is quite logical

// You need to override all the pure virtual functions in order to initialize which is quite logical

file *a =new c_file("main.cpp");
// This is totally fine because we are using dynamic bounding over here 

a->open();
a->close();


unique_ptr <file> b=make_unique <c_file>("Hello.cpp");

// This is smart pointer

b->open();
b->close();



// To achieve the concept of interface we use abstract classes


// Sometimes it is seen that the interface classes are named in this format I_classname which is obviously a convention






    return 0;
}