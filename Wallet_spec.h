#include <iostream>
#include <string>
#include "Wallet.h"

// This is Specification

#ifndef _WALLET_SPEC_
#define _WALLET_SPEC_



void Wallet::disp_name(){
    std::cout<<"Wallet Holder : "<<Name<<std::endl;
}

// Constructor function
Wallet::Wallet(string name,string key):Name {name},pub_key_str{key},priv_key_str{""}{
    std::cout<<"Wallet created with incomplete information"<<endl;
}

#endif

