#include <iostream>
#include <string>
using namespace std;

// This is Impementation


#ifndef _WALLET_H_
#define _WALLET_H_

// #pragma once




class Wallet {
    public:
    const string Name;
    string pub_key_str {};
    string priv_key_str{};

    string *pub_key=new string {pub_key_str};
    string *priv_key=new string {priv_key_str};

    


    void disp_pub_key(){
        cout<<"Public Key Address : "<<pub_key<<endl;
        cout<<"Public Key : "<<*pub_key<<endl;
    }




    void disp_priv_key(){

        cout<<"Private Key Address : "<<priv_key<<endl;
        cout<<"Private Key : "<<*priv_key<<endl;    
        // We can directly access this variables , first it looks into scope of the class and if the variable is available over there then it takes it unlike in javascript we have to use this keyword
        
        }

    void disp_name();


    // Overloaded Constructors
// Basically 2**n constructor constructor functions can be created to cover all the possibility where n is the number of variables


// Cosntructors

    Wallet():Name{"User"},pub_key_str{""},priv_key_str{""}{
        cout<<"Wallet is created without Credentials"<<endl;
    }
// Here values are intialized to the attributes we have intialized over here as soon as they are created and so we are not intializing to a garbage and not assigning after its initialization

// This is called constructor intialization lists

// If you tried to change the order of the constructor intialization lists works because it will be intialized in order that is declared in the class scope that is under private or public


//  Wallet(){
//         cout<<"Wallet is created without Credentials"<<endl;
//     }
   

    Wallet(string Name_, string pub_key_str, string priv_key_str) :Name{Name_}{

        // From here also we can prove that Name is intialized to first time to Name_ because const variables are need to be intialized while declarartion
        cout<<"Wallet Created with all the required Credentials"<<endl;
        // Name=Name_;
        *pub_key=pub_key_str;
        *priv_key=priv_key_str;
    }


    
    Wallet(string name,string key);

// Destructors

    ~Wallet(){
        cout<<"Destructor called for "<<Name<<"'s Wallet"<<endl;

        // This Destructor function is called before the object is destroyed 

        delete pub_key;
        delete priv_key;
    }



};


#endif
