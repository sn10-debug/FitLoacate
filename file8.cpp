#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <memory>
#include <fstream>
#include <sstream>
#include <limits>

using namespace std;


typedef struct City{
    string name;
    double population;
    double price;
} City;

typedef struct Country{
    string name;
    vector <City> cities;

} Country;

typedef struct Tour{
    string name;
    vector <Country> countries;
} Tour ;


template <typename T> T disp(T x){
    cout<<x<<endl;
    return x;
}



template <class X> void disp_arr(int length,X *arr){

    
    for(int i=0;i<length;i++){
        if(sizeof(float)==sizeof(X)) cout<<fixed<<setprecision(1)<<arr[i]<<" ";
        else cout<<arr[i]<<" ";




    }

    cout<<endl;
}



template <int N> class Array{

    int size{N};
    int arr[N];

    // We can also take size using template

    public:

    Array(){
        this->fill(0);
    }

    Array(int initial_value){
        this->fill(initial_value);
    }

    void fill(int val){
        for (auto &c:arr) c=val;


    }


    
    
};


int main(){

    Tour Tour_1{"Tour To Asia",{
        {
            "India",{
                {
                "Mumbai",400,2000
                },
                {
                "Goa",200,1500
                },
                {
                "Ahmedabad",300,1500
                },{
                    "Bangalore",400,2000
                }
            }
        },
        {
            "Sri Lanka",{
                {
                    "Colombo",200,1000
                }
            }
        },
        {
            "China",{
                {
                    "Shanghai",500,1500
                },
                {
                    "Honk Kong",300,2000
                },{
                    "Beijing",600,2000
                }
            }
        },


    }};



    // double max_country_name{0},max_city_name{0};
    // double max_pop_length=20;
    // double max_price_length=10;

    // cout<<fixed<<setprecision(2);
    

    // for (auto c:Tour_1.countries){
    //     if (max_country_name<c.name.size()) max_country_name=c.name.size();
    // }

    // for (auto c:Tour_1.countries){
    //     for (auto d:c.cities){
    //         if (max_city_name<d.name.size()) max_city_name=d.name.size();
    //     }
    // }


    // double title_length=max_city_name+5+max_country_name+5+max_pop_length+max_price_length;
    // cout<<"\n";
    // cout<<setw(double(title_length)/2)<<Tour_1.name<<setw(title_length/2)<<endl;
    // cout<<"\n";
    // cout<<setfill('-')<<setw(title_length)<<""<<endl;
    // cout<<setfill(' ');
    // max_country_name+=5;
    // cout<<setw(double(max_country_name)/2-4)<<left<<"|"<<"Country"<<setw(max_country_name/2-3)<<right<<"|";
    // cout<<setw(double(max_country_name)/2-2)<<left<<""<<"City"<<setw(max_country_name/2-2)<<right<<"|";
    // cout<<setw(double(max_pop_length)/2-5)<<left<<""<<"Population"<<setw(max_pop_length/2-5)<<right<<"|";
    // cout<<setw(double(max_price_length)/2-3)<<left<<""<<"Price"<<setw(max_country_name/2-2)<<right<<"|"<<endl;


    // max_city_name+=5;
        


    // cout<<fixed<<setprecision(2);

    // for(auto c:Tour_1.countries){
    //     cout<<left<<setw(max_country_name)<<c.name;
    //     int i=0;
    //     for(auto city:c.cities){
    //         if(i>=1) cout<<setw(max_country_name)<<"";

    //         cout<<left<<setw(max_city_name)<<city.name<<right<<setw(max_pop_length-2)<<city.population<<setw(2)<<""<<right<<setw(max_price_length)<<city.price<<endl;
    //         i++;
    //     }
    //     cout<<setfill('-')<<setw(title_length)<<""<<endl;
    //     cout<<setfill(' ');
        
    // }




disp<string>("Hello World");
disp<int>(1);



// template functions

int arr_1[] {1,2,3,4,5};

float arr_2[] {10.0,12.8,292.83,920.19};

disp_arr(5,arr_1);
disp_arr(4,arr_2);

disp_arr(3,new int[3]{0});

unique_ptr <int> ptr_1=make_unique <int> (20);


// By default files are opened in text mode
// We open the files in input mode when we don't want to write to the file instead we just want to read from it

fstream file_1 {"c_trial.txt",ios::in};
fstream file_2 {"c_trial.txt",ios::in | ios::binary};

// 'ios::in' is used to sepcific that is only going to read the file but we know that fstream object can read and write the file at the same time


ifstream file_3 {"c_trial.txt"};
ifstream file_4 {"c_trial.txt",ios::in};

// Here we can provide the 'ios::in' or not also because this is used to read the files only




// There is another way of opening the file


ifstream file_5;
file_5.open("c_trial.txt",ios::binary);


ifstream file_6;

file_6.open("c_trial.txt");

// In this way also we can open the file


// Checking whether the file was successfully opened or not

if(file_5.is_open()){
    cout<<"File Successfully Opened\n";
    string s;
    // getline(file_5,s);
    // cout<<s<<endl;
    // getline(file_5,s);
    // cout<<s<<endl;

    // while(1){
    //     getline(file_5,s);
    //     if(s=="") break;
    //     cout<<s<<endl;
    //     s="";

        // file_5>>s;
        // This is also right but it will stop taking input after space
        // Here we can also chain as we do in cin operator to get the inputs



    // }

    // Another way of doing the same line

    // while(!file_5.eof()){

        // This eof functiion checks whether we are at the end of the file or not
        // getline(file_5,s);
        // cout<<s<<endl;
    // }

    // Another way to do the same thing

    // while(getline(file_5,s)){
        // cout<<s<<endl;
        // this returns a boolean whether it was in successfull in extracting the lines and this we can use with extraction operatpr as well
    // }

    char c;

    // This is read to file in a unformatted manner

    // while(file_5.get(c)){
        // This will read each character at a time
        // cout<<c;

    // }
    // cout<<endl;


    file_5.close();
}
else {
    cout<<"File not opened\n";
}

// if(file_6.is_open()){
//     cout<<"File Successfully Opened\n";
//     file_6.close();
// }
// else {
//     cout<<"File not opened\n";
// }



// Another way of checking whether the file is successfully opened or not

if(file_6){
    cout<<"File Successfully Opened\n";
    file_6.close();
}
else {
    cout<<"File not opened\n";
    exit(1);
    // This will exit the program over here
}



ifstream file_7;

// file_7.open("c_trial2.txt");

// if(file_7){
//     cout<<"File 7 successfully opened\n";
//     string s;
//     // while(!file_7.eof()){
//         while(getline(file_7,s)){
//         cout<<s<<endl;
//     }
//     file_7.close();
// }
// else{
//     cout<<"File not opened"<<endl;
// }

// if(file_7){
//     string correct_ans{};
//     file_7>>correct_ans;
//     int num=1;
//     vector <string> stud_names{};
//     vector <int> stud_marks{};
//     string name,options;

//     while(!file_7.eof()){
//         if(num%2!=0) {
//             file_7>>name;
//             stud_names.push_back(name);            
//         }
//         else {
//             file_7>>options;
//             int mark=0;
//             for (int i=0;i<correct_ans.size();i++){
//                 if(options[i]==correct_ans[i]) mark++;
//             }
//             stud_marks.push_back(mark);
            
//         }
//         num++;

//     }
    

//     double class_average {};
    
//     int max_name_size{0};
//     for(auto c:stud_names){
//         if(c.size()>max_name_size) max_name_size=c.size();
//     }

//     cout<<setw(max_name_size+5)<<left<<"Student"<<"Marks"<<endl;
//     for (int i=0;i<stud_marks.size();i++){
//         cout<<setw(max_name_size+5)<<left<<stud_names.at(i)<<right<<stud_marks.at(i)<<endl;
    
//     }



//     for (int i=0;i<stud_marks.size();i++){
//         class_average+=stud_marks.at(i);
//     }
//     class_average=class_average/stud_marks.size();

//     cout<<right;
//     cout<<"Class Average : "<<class_average<<endl;
// }
// else{
//     cout<<"File Cannot be Opened\n";
// }


// ifstream file_8 {};

// file_8.open("c_trial3.txt");

// string word{};

// cout<<"Enter a word which you want to search and find its occurrences : ";
// cin>>word;

// for (auto &c:word) c=tolower(c);

// char letter{};

// if(file_8){
//     string word_;
//     int num_words{};
//     int search_num{};
//     int num=0;
//     while(file_8.get(letter)){
//         // for(auto &c:word_) c=tolower(c);
//         // if(word==word_) search_num++;
//         if(letter==word[num]) {
//             num++;
//         }
//         else{
//             num=0;
//         }

//         if(num==word.size()){
//             num=0;
//             search_num++;
//         }
//         if(letter==' ' or letter=='\n') num_words++;
//     }

//     cout<<"Number of Words : "<<num_words<<endl;
//     cout<<"Searched Word Occurences : "<<search_num<<endl;


// }
// else{
//     cout<<"File Cannot be opened\n";
// }




// Writing to a file


// fstream file_9 {"c_trial2.txt",ios::out};

// If the file exists then it will not create a new file but if does not exits then it will automatically create a new file



// trunc is to overwriting the existing content

// app is used to append whatever we want to write to the existing content

// ate- this will take to the end of the file stream


// ofstream file_10 {"c_trial2.txt",ios::trunc};
// the second parameter is method of writing


// By default the file is open for truncation

ofstream file_11 {"c_trial2.txt",ios::app};

// if(file_11.is_open()){

    // Two Ways of doing the same thing
if(file_11){
file_11<<"LMN\n"<<"AAAAAA";

// endl flushes out unwritten buffer

file_11.put(' ');
// put method is to write a character to the file


file_11.close();
}
else {
    cout<<"File Cannot be Opened or created\n";
    exit(1);
}

// ofstream file_12 {"c_trial2.txt",ios::ate};




ifstream file_13 {"c_trial3.txt"};

ofstream file_14 {"c_trial.txt",ios::trunc};

if(file_13 and file_14){
    string line;
    int num_line=1;

    while(getline(file_13,line)){
        if (line!=""){
            file_14<<num_line<<". "<<line<<endl;
            num_line++;
        }
        
        
    }

    file_13.close();
    file_14.close();

}
else {
    cout<<"Error opening the files\n";
}





// string stream

string trial_line {"ABC 1490 "};
istringstream sstream_1 {trial_line};

// Using this we can string stream while is same like file stream

string word_2{};
int num_2 {};


sstream_1>>word_2;
sstream_1>>num_2;


cout<<word_2<<" "<<num_2<<endl;



ostringstream sstream_2 {"This is the ostringstream\n",ios::app};

// We can initialize or we can just leave it as we know while writing if the file is not available then it automatically creates the file and if available it makes changes depending on how we are opening


// if we don't mention ios::app then it will simply truncate which usually happens writing in a file

sstream_2<<"Name : "<<word_2<<" Number : "<<num_2;
// Here anything we can add as just we were doing with the files
cout<<sstream_2.str()<<endl;

bool stop=false;

do{

int value;
string text{};
cout<<"Enter a Integer : ";
cin>>text;
istringstream validate {text};

if(validate>>value) {
stop=true;
cout<<"You entered an Integer\n";
cout<<"Entered Integer : "<<value<<endl;
}
else {
    cout<<"You have not entered an Integer . Take a next attempt \n";
}


cin.ignore(numeric_limits <streamsize>::max() ,'\n');

// This will delete all the Buffer till a new line occurs in the user input







}
while(!stop);


// When we declare a template the compiler does not generate code for it instead it simply considers as a blueprint

// When we provide the typename with the template function call then the compiler generates code for the specific type and then the function is called

// From here we can undersatnd that the vectors,smart pointers use generic programming

Array <10> arr2 {};





    return 0;
}