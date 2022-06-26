#include <iostream>
#include <stdio.h>
#include <memory>
#include <vector>
#include <string>
#include <list>
#include <algorithm>


#define NAME "SHAKTI SANTOSH NAYAK"

#define min(a,b) ((a<b)?a:b)

#define max(a,b) ((a>b)?a:b)


#define check(ptr) ((ptr==nullptr) ? "This is a null pointer" : "This is not a null pointer")

// As preprocessor does not knwo C++ and if we include semicolon and then it will also store the semicolon as value

// Before the compilation it will just check whether there is variable we defined as macros in the program and then it will just subsitute the value whatever we stored in that macro variable



using namespace std;


class A{
    public:
    ~A(){
        cout<<"Destructor Called"<<endl;
    }
};



template <class t1,class t2> class nums{
    public:
    t1 num1;
    t2 num2;
    nums(t1 n1,t2 n2):num1{n1},num2{n2}{
        cout<<"Object Created\n";
    }


};


list<int>::iterator operator-(list<int>::iterator rhs,int a){
    for (int i=0;i<a;i++){
        --rhs;
    }

    return rhs;

}

list<int>::iterator operator+(list<int>::iterator rhs,int a){
    for (int i=0;i<a;i++){
        ++rhs;
    }

    return rhs;

}


void disp_list(list <int> &nums){

    for(list<int>::iterator itr=nums.begin();itr!=nums.end();itr++){
        cout<<*itr<<" ";
    }
    cout<<endl;

}


template <class t> t temp_max(t a,t b){

    
    return ((a>b)?a:b);

}


int main(){

    A *ptr=new A{};

    unique_ptr <A> ptr_2=make_unique <A> ();

    unique_ptr <A> ptr_3 {move(ptr_2)};

    // ptr_3.reset();


    nums<int,float> num_1{2,4.5};

    cout<<num_1.num1<<endl;
    cout<<num_1.num2<<endl;





string a{"Shakti Santosh Nayak"};

string b {a,0,2};

cout<<b;



    

    delete ptr;


// The stl provides a rich set of containers, algorithms and iterators
// The stl is one of the best of the generic library
// The stl is a assortment of the commonly used containers


// The main elements of stl is Algorithm,iterators and containers

// Containers are collection of objects or primitive types

// Containers include array,vector,set,map,stack,deque etc.

// Alogroithms provides function for processing the elements of a container

// There are 60 algorithms

// Iterator are responsible for generating sequence of elements

// It has two other components as well that is functors and allocators





list <int> nums{1,2,3,4,10,9,8};

list<int>::iterator itr=nums.end();
itr--;
list<int>::iterator itr2=nums.begin();


vector <int> nums_2 {1,2,3,4,5,10,9,38,30};
sort(nums_2.begin(),nums_2.end());

// This sort function belongs to algorithm and thus the vector is sorted with the help of iterators

for (auto c:nums_2){
    cout<<c<<" ";
}
cout<<endl;


// Types of Containers

// Sequence Containers

// These are the containers which maintain the ordering of the elements

// Examples:Array,vector,list,forward_list,deque

// Associative Containers

// These are the containers where the inserted elements may be ordered or undordered

// This includes set,map,multi set,multi map

// Container Adapters

// These are the containers which do support iterators and thus they cannot be used with stl algorithms

// This includes stack,queue,priority queue

// Types of Iterators

// Input Iterators:from the container to the program basically while reading elements

// Output Iterators: from the program to the container basically while writing the elements

// Forward Iterator: navigate one item in one direction 

// Bi-directional iterators : navigate one item in both directions

// Random access iterators: directly access a container element

// Random access iterators could consist of subscript operator which we used with array and vectors to get any element





// They are two types of Algorithms 
// Modifying Algorithm that is which changes the squence
// Non Modifying Algorithm is the one which does not make change to the sequence







for (itr;itr!=itr2-1;itr--){
    cout<<*itr<<" ";
}
cout<<endl;

int *ptr_4=(int*) calloc(10,sizeof(int));

int *ptr_5=(int*) malloc(5*sizeof(int));

delete [] ptr_5;
delete [] ptr_4;


// Generic Programming is the type of programming where the code works with various types of arguements unless it makes sense to work with the various types



cout<<"List Section\n";

list <int> list_1 {1,2,3,4};

disp_list(list_1);

list_1.insert(list_1.begin(),5);

disp_list(list_1);
list_1.push_back(10);

disp_list(list_1);

list_1.sort();


cout<<"Elements Arranged in Ascending Order\n";
disp_list(list_1);

list_1.reverse();


cout<<"Elements Arranged in Descending Order\n";
disp_list(list_1);

list_1.emplace(list_1.begin(),10);

disp_list(list_1);

list_1.unique();

disp_list(list_1);


cout<<"The size of the list is "<<list_1.size()<<endl;



// Macros

// We should prefer not using

// We have already used a Macros #define 

// In the context of header guards it is ok to use Macros 

// We already know that which begin with # sign are preprocessor directives

// We also know that preprocessor does not know C++

// Use of Macros

cout<<NAME<<endl;

cout<<min(2,7)<<endl;
cout<<max(2,7)<<endl;

cout<<check(nullptr)<<endl;

cout<<temp_max<float>(2.2,5.5)<<endl;

cout<<temp_max(12,15)<<endl;
char s[100];
printf("Input a string : ");
scanf("%[^\n]",&s);

printf("%s\n",s);










}