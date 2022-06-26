#include <iostream>
#include "Mystring.h"

using namespace std;

#ifndef _MY_STRING_NON_MEM_
#define _MY_STRING_NON_MEM_

MyString operator+(char *s,const MyString &source){
    MyString Temp{s};
    Temp=Temp+source;
    return Temp;
}
MyString operator+(const MyString &source,char *s){
    MyString Temp{s};
    Temp=source+Temp;
    return Temp;
}



#endif
