#include <iostream>
#include <iomanip>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <string>
#include <math.h>
#include <cmath>
#include <ctime>
using namespace std;

string encrypter(string text){
string character {"abcdefghijklmnopqrstuvxyz"};

string characters {character};
for (int i {0};i<character.length();i++) characters+=toupper(character[i]); 

characters+="0123456789 ";



string enc_keys;

// cout<<static_cast <int> (characters.length())<<endl;

for (int i {static_cast <int>(characters.length())-1};i>=0;i-=1) enc_keys+=characters[i];

string encrypted_text;
for (char a:text){
    for (int i {0};i<characters.length();i++) {
        if (characters[i]==a) {
            
            encrypted_text+=enc_keys[i];
            break;
            }
        else if (i==characters.length()-1){
            encrypted_text+=a;
        }
    }
}
return encrypted_text;  
}



void n_times_hello(int n){
if (n>=1) {
cout<<"hello"<<endl;
n_times_hello(n-1);
}
else return;


}


void func1(int a,int b=10);


void func2(vector <int> nums){
    nums[0]=100;

}

void func3(int a[]);
 




// This is callled as function prototype like just declaring the function and not mentioning the statements of the function which are going to be executed

// The compiler just needs to know the header of the function that is just the return type and function name and the number of parameters it is taking

// And we can declare this below the main function also
const string name {"Shakti Santosh Nayak"};

int main(){
// char name[100] {};
// cout<<"Enter your full name : ";
// cin.getline(name,99);
// cout<<"Your name is "<<name<<endl;
// cout<<"The number of characters in your name is : "<<strlen(name)<<endl;

// char my_name[90] {};
// strcpy(my_name,"Shakti Santosh Nayak");

// if (strcmp(name,my_name)==0) cout<<"Shakti you are itself the developer of this program .\n";
// else cout<<"You are not the developer of this program .\n";


// strcat(my_name," , CEO and Chairman of Sigma .");
// cout<<strcmp(name,my_name)<<endl;


// strcmp is used to compare if both arguements provided in the function are same then it returns 0
// This function checks till a null character comes and if till then both are same then it returns 0 else it returns -1
// This will return greater than 0 if the first string comes lexically after the the second string
// less than 0 if the secodn string comes lexically after the first string



// cout<<"Your identity in block letters is : ";
// for(size_t i {0};i<strlen(my_name);i++) {
//     if (isalpha(my_name[i])) my_name[i]=toupper(my_name[i]);
//     cout<<my_name[i];
//     }
// cout<<endl;
// cout<<toupper(2)<<endl;


string name_2 {"Shakti Santosh Nayak"};
// In order to use the string we need to include the library named string with pre processor operator.
//string class is available in the standard namespace
// This is quite better tha c-tyle string because this has lot of methods and also this is dynamic and also we can use lot of operator which also include relational operators and also this C++ string can be easily converted to c style string if needed.


/*

// cout<<name_2<<endl;

// String are dynamic in size

string string_1 {"Shakti"};
string string_2 {string_1,0,3};
// This will start from index 0 and take 3 characters from there


string string_3 {string_1,4};

// This will start from index 4 and go till end

string string_4 (4,'S');

// This will store SSSS that is 4 times S repeated and one more thing is that we initialized using a constructor initializer


cout<<string_1<<endl<<string_2<<endl<<string_3<<endl<<string_4<<endl;

string string_5="My name is ";
string intro=string_5+"Shakti Santosh Nayak";

// string string_6="My name is "+"Shakti Santosh Nayak";

// We cannot conacanate only c-style literal instead it should be mix of C++ string and c-style literal

// Any sentence written in double quotation is called c-style literal 

cout<<intro<<endl;

// for (char c:string {"Shakti"}) cout<<c<<endl;

// This will take each character of the string

// for (int c:string {"Shakti"}) cout<<c<<endl;
// This will print the integer representing the character in memory

cout<<('h'>'a')<<endl;

// This will compare the ascii key values of the characters

// We can use relational operators for following type of strings

// two std::string objects that is C++ strings

// one std::string and c-style literal

// one std::literal and c-style string that is array of characters


// cout<<intro.at(1)<<endl;
// cout<<intro[1]<<endl;

// Like how we used in vectors
// With subscript there is no bound checking but with 'at' method there is bound checking



// substr method

cout<<intro.substr(11,6)<<endl;

// This will take 6 characters from the index 11
// if some case the number of characters are less after a certain index we assigned then it will be printing the whatever remaining characters are there after the index.


cout<<intro.substr(11)<<endl;


// It is quite logical that substr is a substring

// find method on strings

string string_6 {"Sigma : Summation of Imagination "};

cout<<string_6.find("Sigma")<<endl;
// This will tell the index at which the occurence of word starts

cout<<string_6.find("tion")<<endl;
cout<<string_6.find('a')<<endl;

// find method takes string as well as character

cout<<string_6.find("Sigma",0)<<endl;


// Here 0 tells that it will start finding the particular c-style literal in the string from the index 0

cout<<string_6.find("Sigma",1)<<endl;

// This will return garbage as Sigma doesn't occur after index 1

cout<<string_6.rfind("tion")<<endl;

// As we know the find method returns the index of first occurenece
// in case of rfind method it start searching from behind and from it will return the index of the first occurenece and therefore here it returned the last occurence of 'tion' but according rfind it is first occurenece which is quite logical



// Erase method

string string_7="Hello this is a C++ program";

cout<<string_7.erase(0,6)<<endl;
// from 0 index it will erase 5 characters and also it returns the mutated string after erasing.
string_7.at(0)=toupper(string_7.at(0));

cout<<string_7<<endl;

cout<<string_7.length()<<endl;

// This length method gives the length of the string


string_7.clear();

// This clears the whole string and the string variable becomes empty

cout<<"Empty String : "<<string_7<<endl;


string string_8 {};

getline(cin,string_8);

// This will take space as well


cout<<string_8<<endl;

// Extraction operator stops when it sees whitespace and this happen when we directly use cin function
// But this is not true with getline() function it reads till it sees \n


// Another variant of getline method


getline(cin,string_8,'g');

// Another arguement should be a character and what geline does with these that it does not take the other part of string after this character and it will not include the character as well

// Good good is the input
// Good -only this will be stored with this method

cout<<string_8<<endl;

*/


// string string_9;

// even if we dont initialize it wont store garabage because string is a class and we are making a object out of it

// cout<<string_9<<endl;
// cout<<string_9.length()<<endl;
// This will be 0 over here which is quite obvious

// string string_10 {"Hello"};

// string string_11 {string_10};

// string_11 will make a copy of string_10 and they will not be linked to same memory location


// string string_12 {"Meta"};

// string string_13 {"Sigma"};

// cout<<boolalpha;

// cout<<string_13<<" > "<<string_12<<" : "<<(string_13>string_12)<<endl;

// string_13[0]='s';

// We can change it with only to a character which in python string assignment is not allowed


// cout<<string_13<<endl;

// string_13.at(0)='S';

// cout<<string_13<<endl;




// You can only add c-style and C++ strings

// We can also use range based for loop on strings


// for (auto c: string_13) cout<<c;
// cout<<endl;


// size_t word_pos=string_13.find("Hello");

// if (word_pos==string::npos) cout<<"Word not found";
// else cout<<"Word Found";

// string::npos is return when no such word exist basically no position

// We can see here that size_t can also hold error along with unsigned integers

// cout<<endl;


// string_13.insert(5," Hello");
// This will insert "Hello" from fifth index and including index 5

// cout<<string_13<<endl;

// pow(2,2);

// Storing password along with name but on printing only name will be printed


// string name {};

// getline(cin,name);

// char info[name.length()+10] {};

// for (int i {0};i<name.length();i++) info[i]=name[i];

// info[name.length()]='\0';

// cout<<name<<endl;

// for (size_t i {name.length()+1};i<name.length()+9;i++) cin>>info[i];


// cout<<info<<endl;

// for (size_t i {name.length()+1};i<name.length()+9;i++) cout<<info[i];


// Encryption


cout<<"Hello world"<<endl;

// string character {"abcdefghijklmnopqrstuvxyz"};

// string characters {character};
// for (int i {0};i<character.length();i++) characters+=toupper(character[i]); 

// characters+="0123456789 ";

// cout<<characters<<endl;

// string enc_keys;

// // cout<<enc_keys<<endl;
// cout<<static_cast <int> (characters.length())<<endl;

// for (int i {static_cast <int>(characters.length())-1};i>=0;i-=1) enc_keys+=characters[i];


// string text;
// cout<<"Enter a text which has to be encrypted"<<endl;
// getline(cin,text);


// cout<<"Encrypting message ...\n"<<endl;

// cout<<encrypter(text)<<endl<<endl;
// cout<<"Decrypting message ...\n"<<endl;
// cout<<encrypter(encrypter(text))<<endl;

// cout<<encrypted_text<<endl;




// char letters[4] {};

// cin>>letters;

// cout<<letters;



// string letters;
// getline(cin,letters);

// int length_string=static_cast <int> (letters.length());

// length_string=2*(length_string)-1;

// for (char letter:letters){

//     string segment;

//     for (int i{0};i<length_string;i++) segment+=" ";

//     segment[length_string/2]=letter;
    
//     int num_remaining_letters=letters.find(letter);
    
//     string remaining_letters=letters.substr(0,num_remaining_letters);
    
//     string reversed_remaining_letter {};
//     for (int i {static_cast <int>(remaining_letters.length())-1};i>=0;i--) reversed_remaining_letter+=remaining_letters[i];
//     for(int i{1};i<=num_remaining_letters;i++){
//         segment[length_string/2-i]=reversed_remaining_letter[i-1];
//         segment[length_string/2+i]=reversed_remaining_letter[i-1];
//     }
//     cout<<segment<<endl;





// }

// cout<<sqrt(200.0)<<endl;

// cout<<pow(2,0.5)<<endl;


// // This returns a double

// // cout<<letters<<endl;


// cout<<cbrt(20)<<endl;
// // This provides the cube root of the number

// srand(time(nullptr));
// // this srand function needs a seed and we have seeded it

// // the srand has seed value has 1 by default


// int num1=rand();
// cout<<num1<<endl;

// // IF we use only rand function then it will generate the same sequence of numbers and we dont want this so before declaring we need to use srand

// // This will generate random numbers but it will be of same sequence and we can see this by printing multiple numbers

// cout<<log10(100)<<endl;

// cout<<log(2.73)<<endl;

// cout<<sin(M_PI/6)<<endl;

// cout<<ceil(15.6)<<endl;
// // 16

// // This is not like greatest integer function instead it provides the next integer number of the integral part of the number

// cout<<floor(15.6)<<endl;
// // 15 and this works like greatest integer function

// cout<<ceil(-2.5)<<endl;
// cout<<floor(-0.5)<<endl;


// cout<<RAND_MAX<<endl;


// int num2 {};
// // Thus variable is intialized to 0

// cout<<num2<<endl;

// cout<<time(nullptr)<<endl;

// cout<<rand()%(51)<<endl;

// // This will generate a random number between 0 and 50
// cout<<abs(-2)<<endl;

// n_times_hello(10);











func1(2,4);

cout<<name<<endl;

// This is a global variable


// Before callling a function we need to create the prototype of a function if we are declaring the function anywhere else so while declaring the function prototype we have to give the return value function name and the parameters list and if try to give another type of parameters list in the function it will give an error

// In a prototype it is ok if we dont name the parameters just write the type of parameter

// To make a function after the main function and use it in the main function we should first create its prototype because the compiler reads from top to bottom and during this will not able to access the function which is decalared after the main function if we have'nt declared the prototype of the function before the main function

// challenge

string letters (4,'y');
cout<<letters<<endl;


cout<<"Checking for vectors"<<endl;

vector <int> nums {10,20,30};

for(auto c: nums){
    cout<<c<<" ";
}

cout<<endl;

func2(nums);
for(auto c: nums){
    cout<<c<<" ";
}

cout<<endl;


cout<<"Checking for array"<<endl;

int arr[3] {1,2,3};
for (auto c:arr){
    cout<<c<<" ";
}
cout<<endl;

func3(arr);

for (auto c:arr){
    cout<<c<<" ";
}
cout<<endl;


// The array is mutated

return 0;


}

void func1(int a,int b){
cout<<a<<endl<<b<<endl;
cout<<"Hello world"<<endl;

}

void func3(int a[]){
a[0]=100;
}