#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include "Wallet.h"
#include "Wallet_spec.h"


using namespace std;


#define NAME "SHAKTI SANTOSH NAYAK";


// #ifndef _WALLET_H_
// define _WALLET_H


// #endif

// This is a include guard

// This prevents the declaration of same header file included multiple times
// Declaration of same thing multiple times will give error


// #pragma once
// This also works same as include guards


// We use anchor brackets with include that is <> to include a system header file and from here the system comes to know the location of the file

// While including self defined header file we have to include in this format include "Wallet.h"


// class Wallet {
//     public:
//     string Name="User";
//     string *pub_key=new string;
//     string *priv_key=new string;

//     void disp_pub_key(){
//         cout<<"Public Key Address : "<<pub_key<<endl;
//         cout<<"Public Key : "<<*pub_key<<endl;
//     }

//     void disp_priv_key(){

//         cout<<"Private Key Address : "<<priv_key<<endl;
//         cout<<"Private Key : "<<*priv_key<<endl;    
//         // We can directly access this variables , first it looks into scope of the class and if the variable is available over there then it takes it unlike in javascript we have to use this keyword
        
//         }

//     void disp_name();
// };


// Declaring methods outside class Declarations
// Before this we have to create a prototype for the method inside class declarations

    // void Wallet::disp_name(){
    //     cout<<Name<<endl;
    // }

// In order to declare a method for the class we have to use the Class name along with scope resolution operator and then the method Name





// void Wallet::disp_name(){
//     cout<<Name<<endl;
// }



class nums{

    public :
    int num_1;
    int num_2;
    int num_3;


    nums(int num1,int num2,int num3) : num_1 {num1},num_3{num_2+num3},num_2{num2}{}

};


class Blocks{
public :
const string *block1;
const string *block2;

Blocks(string key1,string key2):block1{new string{key1}},block2{new string {key2}}{}

Blocks(): Blocks("None","None"){}

Blocks(string key1) :Blocks(key1,"None"){}

void get_data(){

cout<<*block1<<endl;
cout<<*block2<<endl;

}





};




class Product{
    public:
    string Name;
    long double Price;


    Product(string name="None",double price=0) :Name {name},Price {price}{}

    // Declaring default parameters reduced number of constructor functions


};



int main(){

    cout<<"Hello World"<<endl;

    Wallet Wallet_1{"Shakti Santosh Nayak","167282828hdndnnd992jjd9dkd993993","929399hfkkdod002kkfkf00394004009"};
    // *(Wallet_1.pub_key)="167282828hdndnnd992jjd9dkd993993";
    // *(Wallet_1.priv_key)="929399hfkkdod002kkfkf00394004009";
    // Wallet_1.Name="Shakti Santosh Nayak";


    Wallet_1.disp_pub_key();
    Wallet_1.disp_priv_key();
    Wallet_1.disp_name();


    Wallet Wallet_2 {"Santosh Nayak","1290200202020","17892929020"};

    Wallet_2.disp_pub_key();
    Wallet_2.disp_priv_key();
    Wallet_2.disp_name();


    // cout<<NAME;


    // C++ has three Class member access modifiers

    // That is public,private,protected

    // public is accessible everywhere
    // private is accessible only by the members or the friends of the class

    // Protected is used with inheritance


// undefined reference means this has found prototype but not found the declaration


// Constructor in the class can be overloaded and they have same name as the Class
// They are called at the time of new object creation which we already know

// Destructors are special method of the class and they don't have any return type and they are invoked when an object is destroyed
// Basically they can used for releasing memory

// They are proceeded with a tilde (~)
// Destructors cannot be overloaded because C++ automatically calls the destructor
// If it is overloaded then C++ will be confused about which to call

// As constructors are called manually and therefore they can be overloaded


Wallet *Wallet_3=new Wallet("Shakti Santosh Nayak II","155151616","51616161616");




// When the execution of this function is finished then all the Wallets has going to be destroyed as we know the as the execution of a function is finished then the Activation record is deleted for the function


// But as Wallet 3 is there in the heap so there will be memory leak if we dont delete manually

// The Variables which is declared first will be destroyed at last that is First in Last out




delete Wallet_3;


Wallet Wallet_4 ("Reenakhi Santosh Nayak","18282828282828","930300303101");

// Default constructors are the constructors which expect no arguements that is no arg constructor and C++ will automatically generate a default class constructor if it founds no constructor declared for the class and this default constructor does nothing


// When you intialize a object with no arguements then this default constructor is called



// In constructor when we assign value to the attributes it is technically not initialization because before the execution of constructor function this member attributes have already been created





nums num_list(1,2,3);

printf("%d %d %d \n",num_list.num_1,num_list.num_2,num_list.num_3);

// Thus we can see over here the order of intialialization is same as we declared in the class scope


// We can also call a constructor inside another constructor of the same class and we saw intializing attributes has the same sytanx just we are changing the values so we can delegate this work


// Blocks block_1;
// block_1.get_data();
// Blocks block_2("Hello world 1");
// block_2.get_data();
// Blocks block_3("Hello world 1","Hello world 2");
// block_3.get_data();

// Calling the other constructors works only in constructor intialization lists

// If we use a constructor delegator then the body of the constructor which called the constructor delagator is executed as well as the body of the constructor delegator gets executed
// It is obvious that the body of the constructor delegator will be executed first and then the main constructor





// string str("hello",2);



// cout<<str<<endl;


Product Product_1 {"Hello"};
cout<<Product_1.Name<<endl;
cout<<Product_1.Price<<endl;


Product Product_2 {"World",10001.0};
cout<<Product_2.Name<<endl;
cout<<Product_2.Price<<endl;



string name="Shakti Santosh Nayak";

cout<<name.length()<<endl;

string substr (name,0,1);

cout<<substr<<endl;










    return 0;
}