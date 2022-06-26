#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <math.h>
#include <memory>
#include <iomanip>



using namespace std;



class Product{

    // This is a abstract class
    friend ostream & operator<<(ostream &os,const Product &obj);
    
    protected:
    string name;
    double price;

    public:

    
    // virtual void disp_name(ostream &os) const{
    //     os<<name;
    // }

    virtual void disp_name(ostream &os) const=0;

};


class Fashion:public Product{

    // This is a abstract class 
    protected:
    double size;
    string gender;
    string color;
    string cloth_type;
    string brand_name;


};

class Shirt:public Fashion{

    // This is a concrete class 

    friend ostream & operator<<(ostream &os,const Product &obj);




    public:
    // int reg_num;
    // static int shirt_num;
    // static void increase(){
    //     // cout<<"New shirt Added : "<<shirt_num<<endl;
    //     ++shirt_num;
    // }



    Shirt(string gender_,string color_,string brand_name_,double price_,string cloth_type_="cotton",double size_=30){
        gender=gender_;
        color=color_;
        brand_name=brand_name_;
        cloth_type=cloth_type_;
        size=size_;
        price=price_;
        name="Shirt";
        // increase();
        // reg_num=increase();
        
        // cout<<"Shirt Number : "<<Shirt::shirt_num<<endl;

    }
    virtual void disp_name(ostream &os) const{

        os<<"\nDisplaying "<<name;
        // os<<"\nShirt Number : "<<reg_num;
        os<<"\nGender : "<<gender;
        os<<"\nSize : "<<size;
        os<<"\nCloth Type : "<<cloth_type;
        os<<"\nColor : "<<color;
        os<<"\nBrand Name : "<<brand_name;
        os<<"\nPrice: "<<price;

        
    }
};


ostream & operator<<(ostream &os,const Product &obj){

    obj.disp_name(os);
    return os;

}


class Base_1{
public:
Base_1(){
    std::cout<<"Base-1 created\n";
}
};

class Base_2{
    public:
    Base_2(){
        cout<<"Base-2 created\n";
    }
};

class Derived_1:public Base_1,public Base_2{

public:
Derived_1():Base_2(),Base_1(){

    // The constructors of the Base class are called as per they inherited
    cout<<"Derived 1 created\n";
}

~Derived_1()=default;

// This will create a default destructor


};


class Seller_Product{

    friend void disp_Seller_Product(const Seller_Product &c);
    protected:
    string Product_Name;
    double Product_Price;
    public:

    Seller_Product(string product_name_="New Product",double price=0):Product_Name{product_name_},Product_Price{price}{
    }


    string get_name(){
        return Product_Name;
    }
};


void disp_Seller_Product(const Seller_Product &c){
    cout<<"Product Name : "<<c.Product_Name<<endl;
    cout<<"Product Price : "<<c.Product_Price<<endl;

}




class Seller {
    protected:
    vector <Seller_Product> Products;
    public:
    virtual void disp_products() const=0;
    virtual void add_new_product()=0;
    virtual void remove_product()=0;
};

class WholeSeller:public Seller{
    protected:
    string Seller_Name;
    string License_Number;



    public:

    WholeSeller(string name="New WholeSeller",string license_num="Invalid"):Seller_Name{name},License_Number{license_num}{



    }
    void disp_products() const override{

        for(const Seller_Product &c:Products){
            disp_Seller_Product(c);
        }

        

    }

    void add_new_product(string product_name,double product_price){

        bool present=0;

        for (Seller_Product &c :Products){

        }
        Products.push_back(Seller_Product {product_name,product_price});
    }


    void remove_product(string Product_Name){





    }



    





};


class Distributor:public Seller{

};

class Retailer:public Seller{

};


class Score{

    public:
    int points;
    Score():points{0}{

    }

    void increase(){
        points++;
    }
};



 class B;

//  This is called as forward declarations



class A{
    public:
    shared_ptr <B> ptr;
    void set(const shared_ptr <B> &b){
        ptr=b;

    }

    ~A(){
        cout<<"Destructor Called of A \n";
    }

};


class B{

    public:
    shared_ptr <A> ptr;
    void set(const shared_ptr <A> &a){
        ptr=a;

    }

    ~B(){
        cout<<"Destructor Called of B \n";
    }

};


void delete_Class_A(A *ptr){
    cout<<"Smart pointer containing A got deleted\n";
    delete ptr;
}



class trial{
    public:
    int *number;
    trial(int num=0):number{new int {num}}{

    }

    ~trial(){

        cout<<"Trial class of "<<*number<<" is deleted \n";
        delete number;
    }
};


unique_ptr <vector<shared_ptr <trial>>> make(){

    unique_ptr <vector<shared_ptr <trial>>> ptr{new vector<shared_ptr <trial>>}; 
    return ptr;
}


void fill(vector<shared_ptr <trial>> &ptr,int num){

    for (int i=0;i<num;i++){
        int x;
        cout<<"Enter the data number ["<<i+1<<"] : ";
        cin>>x;
        shared_ptr <trial> ptr_2=make_shared <trial>(x);

        ptr.push_back(ptr_2);
        
    }

}

void display(vector<shared_ptr <trial>> &ptr){

    for (int i=0;i<ptr.size();i++){
        cout<<"The Number stored in index ["<<i<<"]"<<" is ";
        cout<<*(ptr.at(i)->number)<<endl;

    }

}


double divide(int num1,int num2){
    if (num1<0 or num2<0) throw string {"Negative Value Entered\n"};
    if(num2==0) throw 1;

    return double(num1)/num2;
}


class Error{
    public:
    string Statement;
    Error(string st="Exception Raised"):Statement{st}{

    }

    ~Error()=default;
};

class Password{
    public:
    string pass;

    Password(string pass_):pass{pass_}{
        if(pass.size()<8) throw Error("Length of Password is less than 8\n");
        
        int num_char=0;
        
        int num_numeric;

        for(auto c:pass){
            if(isalpha(c)) num_char++;
            else if (isdigit(c)) num_numeric++;
        }

        if (num_char<3 || num_numeric<3) throw Error("Given specifications Violated"); 
    }


};


class wrong_word:public exception{
    public:
    wrong_word() noexcept=default;

    ~wrong_word ()=default;

    virtual const char* what() const noexcept{
        return "This is a wrong word\n";

    }
};


class Negative_Balance:public exception{


virtual const char* what() const noexcept{
    return "Negative Balance not Allowed\n";
}
};


class Insufficient_Balance:public exception{


virtual const char* what() const noexcept{
    return "Insufficient Balance\n";
}
};

class Account{
    double balance;
    public:

    Account(double bal=0){
        if(bal<0) throw Negative_Balance{};
        else balance+=bal;

    }

    void depoist(const double amount){
        balance+=amount;
        
    }

    void withdraw(const double amount){

        if (balance>=amount) balance-=amount;
        else throw Insufficient_Balance{};
        
    }
};



int main(){

    Shirt Shirt_1{"M","Black","Demands",1000,"Cotton"};
    Shirt Shirt_2{"M","Black","Demands",2000,"Cotton"};


    cout<<Shirt_1<<Shirt_2<<endl;

    // cout<<Shirt_1.shirt_num<<endl;

    Derived_1 der {};


    // Smart Pointers


    // There are three types of smart pointers:
    // 1.Unique pointers
    // These pointers are used when we have clear idea about ownership that which pointer should own the data
    // 2.Shared pointers
    // 3. Weak Pointers
    // 4. auto pointers

    // Also there are custom deleters
    // We can call a particular version of delete as per our choice

    // dangling pointers are the pointers which point to a storage in heap which is already de allocated

    // They are objects which is found in C++ template classes


    // Smart pointers point to the heap allocated memory


    // They are deleted when they are not needed

    // Pointer arithmetic is not allowed in case of Smart Pointers

    // The Implementation of Smart pointers is compiler dependent

    // RAII-Resource Aquistion is Initialization


    // Resource Aquistion

    // Opening a file
    // Allocate a memory
    // Aquire a lock

    // Resource is aquired at the time of intialization like basically when the constructor of the object is called

    // Resource relinquishing

    // De allocate a memory
    // Close the file
    // Release the lock



    // Unique pointers

    // There can only be one unique pointer pointing to a object on the heap
    // Owns what it points to
    // Cannot be assigned or copied
    // Can be moved
    // if the pointer is destroyed automatically the destructor of the object it is pointing to is called

    

    unique_ptr <int> p1{new int{100}};

    cout<<*p1<<endl;


    cout<<p1.get()<<endl;

    // This will return the address stored in p1

    p1.reset();

    // This will deallocate memory in heap and the pointer will be pointing to nullptr

    if(p1==nullptr) cout<<"This is a null pointer \n";
    
    // As smart pointer cannot be assigned or copied then it won't be possible to push a smart pointer to a vector

    vector <unique_ptr <int>> ptr_int {};


    // ptr_int.push_back(p1);
    // This won't be possible 


    ptr_int.push_back(move(p1));

    // This can be used to make a unique pointer to a vector and as the vector goes out of scope the pointers in the vector will be automatically deallocated

    // Make unique function

    
unique_ptr <int> ptr_2=make_unique <int> (2);



unique_ptr <int> owner_1=make_unique <int> (200);

unique_ptr <int> owner_2;

// owner_2=owner_1;

// This is not possible because we can assign a smart pointer


owner_2=move(owner_1);

// Now owner 1 become null pointer and ownership will be passed to owner 2;

cout<<owner_1.get()<<endl;


if (owner_1==nullptr) cout<<"Owner 1 is null pointer"<<endl;


// Shared Pointers

shared_ptr <int> ptr_3{new int{10}};

cout<<"Counter Value\n";

cout<<ptr_3.use_count()<<endl;

shared_ptr <int> ptr_4{ptr_3};

// If there are multiple pointers pointing to the same object then when will be the object destroyed ?
// And this can be done like if as the Number of Shared pointer increases then a particular counter increases by 1 and thus as each shared pointer goes out of scope then the counter decreases by 1 and thus when the counter becomes 0 then the object's destructor is called and the object is destroyed



cout<<ptr_3.use_count()<<endl;

// This will give the value of counter

cout<<ptr_4.use_count()<<endl;



ptr_3.reset();

// Now the counter will decrease by 1 and thus ptr_3 will be set to null pointer

cout<<ptr_4.use_count()<<endl;

cout<<ptr_3.use_count()<<endl;


shared_ptr <Score> Score_1=make_shared <Score> ();

shared_ptr <Score> Score_2 {Score_1};


Score_2->increase();
Score_1->increase();

cout<<Score_1->points<<endl;

// We can call increase method on either of shared method and this can also be done by using raw pointers

// Unlike unique pointers, The shared pointers can be assigned , copied and moved;

// There won't be uninitialized pointers in case of smart pointers and if they are not intialized manually then they will initialized to null pointer


// Weak pointer
// Does not participate in owning relationship

shared_ptr <int> ptr_5=make_shared <int> (20);
weak_ptr <int> ptr_6 {ptr_5};






cout<<"The counter of pointer 5\n";
cout<<ptr_5.use_count()<<endl;

// The pointer 6 didn't participated in owning relationship







shared_ptr <A> a1=make_shared <A>();

shared_ptr <B> b1=make_shared <B>();

a1->set(b1);
b1->set(a1);

// Here there will be memory leak as we have created shared pointers to the objects


// Weak pointer can be helpful in preventing in circular instances


// Custom deleters

// We can make a custom deleter function which will be called when a smart pointer will be destroyed

// we cannnot use make_unique or make_shared function with the smart pointers having custom deleters

// We can make a custom deleter with function and lamda




shared_ptr <A> ptr_7{new A{},delete_Class_A};


shared_ptr <A> ptr_8 {new A{},[] (A *ptr){

cout<<"Calling the lamda function for the pointer 8\n";
delete ptr;
}};

// Make sure you declare the formal paramters in the function as raw pointers




// This deleter function is called as lamda expression


unique_ptr <A> ptr_9;

cout<<ptr_9.get()<<endl;





unique_ptr <vector<shared_ptr <trial>>>vec_trials_ptr;

vec_trials_ptr=make();


int Num_data {};

// cout<<"Enter the Number of data you want to enter : ";
// cin>>Num_data;

// fill(*vec_trials_ptr,Num_data);

// display(*vec_trials_ptr);




// Exception Handling

// First of all Exception is a object like int,boolean and many other objects

int x{};

try{

    if (x==0) throw 0;

    // Here we throw a int object

    // Instead of int we should throw objects


    
    cout<<"X is non-zero number\n";

}

catch( int &ex) {

    // Whenever int object is thrown as an exception then this catch block will be executed
    
    cout<<"X is zero\n";

}

cout<<"Program Finished\n";


cout<<100.0/0<<endl;

// This will print infinite
// cout<<100/0<<endl;

// This will make the program crash



cerr<<"This is an error message\n";


// This is like console.error() in the javascript but it doesn't change the design of Message , it will be simply displayed as like of cout does




try{
    double value =divide(-7,0);

    // Execption occured in the function but we catched over here


}
catch(int &ex){
    cout<<"We cannot divide by 0 by a function\n";
}

catch(string &ex){
    cout<<ex;
}

catch(...){
    cout<<"Unknown Execption and Catch all handler is called\n";
}
    


// If an exception is thrown then the remaining lines of the try block does not executes which is quite logical



// When there is a function which generates a exeception and there is no catch handler in the function and then it goes down the stack and seraches for a catch handler and if doesn't find a handler then the program terminated and if handler is found then it gets executed


// 


cout<<log2(32)<<endl;

// When a function gives an execption then it has to be handled ad if it is not handled in the scope of the function then stack unwinding occurs like the function gets removed from the stack and in try block in which function is called , the handler handles the execption and it is not present in try block then again stack unwinding occurs

// If the stack is unwound to main and no catch handler is present then it terminates

// try{}
// catch(...){
//     cout<<"Hello this is an exception\n";
// }


try{
    double x;
    x=0;

    if(x==0) throw Error("This is an Zero");


}
catch(const Error &st){
    cout<<st.Statement<<endl;
}


// We should not throw exceptions from the Destructor, as Destructors are by default no except and also if Exception is thrown then it has to be handled within the Destructor itself




try{
    string pass="abc51234";
    Password pass_1 {pass};
    cout<<"Password is Set\n";

}
catch(const Error &er){
    cout<<er.Statement<<endl;
}



// There is a class named exception which can be used as a base while defining any kind of Execption class

// There is a 'what' named virtual function which we need to overwrite


// noexcept keyword is just to mention that particular method or function will throw no exception

// The destructor is noexcept by default

try{
Account account_1{20};
account_1.withdraw(40);
}
catch(const exception &ex){
    cout<<ex.what();
}


// Stream helps to abstract the complextity of how to work with different input and output devices


// Stream,Files and I/O

// fstream

// fstream provides definitions for formatted input and output from/to file streams.

// fstrean is a object derived from ifstream and ofstream 

// If you want to read a file then we have to use ifstream class and in order to write or create a new file we use ofstream

// In order to both the tasks that is reading and writing simulataneously we use fstream

// cin is an instance of istream
// cout is an instance of ostream

// cerr and clog are unbuffered


// We can do formatting with member functions as well as manipulators

// cout.width(10);//This is member function
// cout<<setw(10);


cout<<boolalpha;
// This is manipulator version
cout.setf(ios::boolalpha);
// This is method version


cout<<(1==1)<<endl;


cout<<noboolalpha;

cout<<(1==1)<<endl;

// cout.setf(ios::noboolalpha);


cout<<resetiosflags(ios::boolalpha);

// This will set to default

cout<<(1==1)<<endl;


// Integer formatters

// noshowbase-this will not show prefix used to show hexadecimal or octal
// hex is represented by prefix 0x and octal is represented by prefix 0

// nouppercase-when displaying a prefix or hex it will be lowercase

// noshowpos-no '+' is shown for positive numbers

// This above are default manipulators

cout<<showpos<<endl;

// This will show + sign for positive numbers

cout<<2<<endl;


int num1=255;
int num2=8282;

cout<<noshowpos;


cout<<showbase;
// This will enable the prefixes for each bases
cout<<uppercase;

// From here all the characters will be in uppercase
cout<<num1<<" "<<num2<<endl;
cout<<hex;

// The numbers from here will be displayed in hexadecimal form
cout<<num1<<" "<<num2<<endl;


cout<<oct;

// The numbers from here will be displayed in octal form
cout<<num1<<" "<<num2<<endl;

// cout<<resetiosflags(ios::oct);
// This also works

cout<<resetiosflags(ios::basefield);


// Using methods
cout<<noshowpos;
cout<<2<<endl;
cout.setf(ios::showpos);
cout<<2<<endl;

// positive sign is show for just the hexadecimal numbers


float a=2.0;
cout<<a<<endl;

cout<<noshowpos;

cout<<setprecision(7);

// setpricision decides the number of digits to be displayed and by default it is 6

cout<<pow(10,6)<<endl;

cout<<noshowpoint;

// Trailing zeros are not displayed

// In setprecision rounding occurs

cout<<fixed;
// This will set precision of 6 after the decimal

cout<<setprecision(4)<<fixed;

// This will set a precision of 4 after the decimal

cout<<100.23456<<endl;


// cout<<setprecision(3)<<scientific;

cout<<showpoint;

cout<<1.23<<endl;

// This showpoint manipulator will add trialing zeros to the float number to get a precison of 4 as we have set the precision to be 4

cout<<resetiosflags(ios::floatfield);

// This will reset to the default values

cout.unsetf(ios::scientific | ios::fixed);

// This will also change to the default values


// Whenever we just paste a hexadecimal decimal number in the console then javascript automatically converts it to a decimal number



// setw is not set by default
// left-when no field width
// right-when fill width is defined
// fill-not set by default-blank space is used
// fill is used to fill the blank space

// right is by default


string greet{"Hello"};

cout<<left;
cout<<setw(10)<<234<<setw(20)<<"Hello World"<<setw(10)<<greet<<endl;
// If we set left then the number will be at leftmost and it will leave space to make the width as 10




// This setw is valid for the next data item only and floating point




cout<<right<<setfill('@')<<setw(10)<<"SSN"<<endl;

// This setfill only when there is setwidth is defined
// Here the space is replaced by the follwing characters

// Stairs

// setfill will be persistent until we change it



cout<<setfill(' ');

int length=8;
for(int i=1;i<=length;i++){
    string s;
    for(int j=0;j<i;j++){
        s+='*';
    }

    cout<<setw(length)<<s<<endl;

}
for(int i=1;i<=length;i++){
    string s;
    for(int j=0;j<i;j++){
        s+='*';
    }

    cout<<left<<setw(length)<<s<<endl;

}







    return 0;
}