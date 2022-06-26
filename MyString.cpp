#include <iostream>
#include "Mystring.h"
#include "Mystring_non_mem.h"
using namespace std;
int main(){
    char name[] {"Shakti Santosh Nayak"};
    MyString string_1 {name};
    cout<<string_1.str<<endl;
    
    MyString string_2 {};
    string_2=-string_1;
    cout<<string_2.str<<endl;

    MyString string_3 {};
    string_3=string_1+string_2;

    cout<<string_3.str<<endl;

    MyString string_4 {};
    string_4=string_1*2;
    cout<<string_4.str<<endl;
    string_4=string_2*2;
    cout<<string_4.str<<endl;


    MyString string_5 {"Hello World"};
    MyString string_6{"Good Morning"};

    string_5+=string_6;
    cout<<string_5.str<<endl;

    string_5*=4;
    cout<<string_5.str<<endl;

    MyString string_7 {};
    MyString string_8 {"Hello world "};
    string_7=string_8+" Shakti Santosh Nayak." + " What's Up ?";
    cout<<string_7.str<<endl;
    MyString string_9 {"World "};
    string_9="Hello "+string_9*10;
    cout<<string_9.str<<endl;

    return 0;
}