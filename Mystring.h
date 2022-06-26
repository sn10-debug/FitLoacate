#include <iostream>
#include <cstring>
#include <string>

using namespace std;

#ifndef _MY_STRING_H
#define _MY_STRING_H
class MyString{
public:
    char *str;
    MyString(char *s=nullptr):str{nullptr}{
        if(s==nullptr) {
            str=new char[1];
            str[0]='\0';
        }else{

            str=new char[strlen(s)+1];
            strcpy(str,s);

        }

    }



    MyString(const MyString &source){

        str=new char[strlen(source.str)+1];
        strcpy(str,source.str);
        // cout<<"Copy constructor is Called "<<endl;

    }

    MyString(MyString &&source){

        str=source.str;
        source.str=nullptr;
        // cout<<"Move constructor is Called "<<endl;

        
    }

    MyString & operator=(const MyString &rhs){
        if(this==&rhs) return *this;
        
        delete [] this->str;
        str=new char[strlen(rhs.str)+1];
        strcpy(str,rhs.str);
        return *this;
    }

    MyString operator+(const MyString &rhs) const {
        char *trial=new char[strlen(this->str)+strlen(rhs.str)+1];
        strcpy(trial,this->str);
        strcat(trial,rhs.str);
        MyString Temp {trial};
        delete [] trial;
        cout<<"This is adding string "<<endl;
        return Temp;
    }

    MyString operator*(int times){
        char *trial=new char[strlen(this->str)*times+1];
        strcpy(trial,this->str);
        for (int i=0;i<times-1;i++) strcat(trial,this->str);
        
        MyString Temp{trial};
        delete [] trial;
        return Temp;
    }

    MyString operator-(){
        char *trial=new char[strlen(this->str)+1];
        for(int i=0;i<strlen(this->str);i++){
            trial[i]=tolower(str[i]);
        }
        MyString Temp {trial};
        return Temp;
    }

    MyString operator+=(const MyString &source){

        MyString Temp{this->str};
        Temp=Temp+source;
        
        delete [] str;
        str=new char[strlen(Temp.str)+1];
        strcpy(str,Temp.str);
        return *this;
    }

    MyString operator*=(int num){
        MyString Temp {};
        Temp=(*this)*num;
        this->str=Temp.str;
        return *this;
    }



};
#endif