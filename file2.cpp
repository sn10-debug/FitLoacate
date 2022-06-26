#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <cmath>
#include <cstring>

using namespace std;
void metaverse(string name, string world = "Sigma");
int increment(int i);

// Function overloading

void sigma(int a = 1);
void sigma(double a);
void sigma(string a);
void sigma(int a[], int length);
void sigma(vector<int> a);
void sigma(float a);

void change_const(const int a[]);

// Pass by reference

void modify_variable(int &a);

void modify_vector(vector<int> &vec);

void print_vector(const vector<int> &vec);


unsigned long long fibonacci(unsigned long long n);


double penny(double penny_1,int n);

inline int sub_number(int a, int b)
{
    return a - b;
}


int * create_int_array(size_t size,int initialization_value=0);




 class Node{
    public:
    //  All the things written after this are public
    string IP_Address {"Node IP Address"};
    string Network_Name {"Network Name"};

    void greeting(){
        cout<<"Hello World The IP Address is : "<<IP_Address<<" in Network "<<Network_Name<<endl;
        
        }
    

};



int main()
{

    metaverse("Shakti Santosh Nayak");

    // You should declare the default value either in prototype or definition but not in both

    cout << fixed << setprecision(2);

    // This will set the precision to 2

    // If one parameter you are declaring as default then all the parameters after has to have a default value

    cout << increment(2) << endl;
    cout << increment(5) << endl;

    int arr1[2]{1, 2};

    cout << *arr1 << endl;

    int a, b, c, *d;

    d = &a;

    *d = 10;

    cout << "The value of a is " << a << endl;
    cout << "The value of d is " << *d << endl;

    int arr2[5]{};

    for (int i{0}; i < 5; i++)
    {
        *(arr2 + i) = i;
    }

    for (auto c : arr2)
    {
        cout << c << " ";
    }

    cout << endl;

    // Function overloading
    // Making functions of same name with different parameters list is possible in C++
    // But function with same name and parameters list but different return type will generate a compiler error because over here the function will get confuse about which function to take and therefore this leads to error

    // vector

    cout << "Function overloading starts" << endl;

    vector<int> k{1, 2};
    sigma(k);
    int arr3[]{1, 2, 3, 4};
    sigma(arr3, 4);

    int var1 = 10;
    sigma(var1);

    double var2 = 10.1;

    sigma(var2);

    float var3 = 7.9;

    sigma(var3);

    string var4{"Shakti Santosh Nayak"};

    sigma(var4);

    cout << "Passing a C-style string" << endl;

    sigma("Shakti Santosh Nayak");

    // Here the C-style string is converted into a C++ string

    // if you pass a character into a function which is expecting a integer then it will not give an error instead it will hold the ascii value of the character

    sigma();

    // Make sure that you declare a default arguement in any one of the overloaded functions else it will give a error because compiler will be confused about which function to execute because we dont comment about the type of the arguement

    int arr4[]{1, 2, 3, 4};

    change_const(arr4);

    arr4[0] = 5;

    // This is fine because when we passed the array into the function at that stage only it was const

    int num = 100;

    cout << "The previous value : " << num << endl;

    modify_variable(num);

    cout << "The modified value : " << num << endl;

    vector<int> vec1{1, 2, 3, 4};

    print_vector(vec1);

    modify_vector(vec1);

    print_vector(vec1);

    // Dynamic memory allocation

    // Using this we can allocate space in heap during runtime

    // malloc

    int *ptr_1;

    ptr_1 = (int *)malloc(15 * sizeof(int));

    // A memory space to store 10 integers will be allocated

    // The return value of malloc is a void pointer so we need to do type casting in order store the integers

    // if memory space is insufficient then malloc returns a null pointer

    // Here the elements are not intialized and they have garbage value in it

    // calloc stands for continous allocation
    // Here the memory is continously allocated like in array

    int *ptr_2;

    ptr_2 = (int *)calloc(15, sizeof(int));

    // Here the parameters are number of blocks and size of each block

    // Also it is more of similar to malloc with some additional features

    for (int i{0}; i < 15; i++)
        *(ptr_2 + i) = i + 1;

    // for (int i{0};i<15;i++) cout<<*(ptr_2+i)<<" ";

    // realloc stands for memory reallocation

    // If we have assigned some memory for a pointer and if we want to allocate more space then we can do it

    ptr_2 = (int *)realloc(ptr_2, 20 * sizeof(int));

    for (int i{15}; i < 20; i++)
        *(ptr_2 + i) = i + 1;

    // free(ptr_2);
    for (int i{0}; i < 20; i++)
        cout << *(ptr_2 + i) << " ";

    cout << endl;

    // The free function is used to free the allocated memory

    free(ptr_2);

    // Static variables are intialized only once and if they are not initialized then it automatically gets initialized to 0

    // Calling a function
    // A acivation record is created for a function

    // When a function is called in the main function then main function pushes space for the parameters as well as return value and push the return address and then the called function pushes the previous activation record and then push any register value needed to be pushed that will be restored before returning tp the calling function and then execution of the code starts and then again restore the resgister values and restore the previous activation record and store any function result and then it returns to the return address and then main function pops out the parameters and return value space

    // return address simply denotes the place where again control has to go in the main function

    // Sometimes this function verhead may take more time than its execution so to avoid this we can declare a inline function where function overhead is not created

    // We usually use inline functions when there is short declaration and this does not pass control to thefunction instead it justs expands during execution just like writing the same code again and again during every call so this takes lot of space


// When we have more than one activation record for the same function then we called it as reccursive function




cout<<endl;

// cout<<fibonacci(30)<<endl;


cout<<penny(0.01,18)<<endl;


// int *ptr;

// int* ptr

// These both methods work the same to declare a pointer
// This time * does not acts as mathematical operator instead it is used to declare a pointer over here

// We have to intialize a pointer or else it stores garbage data

int* ptr_3;

cout<<ptr_3<<endl;

// garbage value

cout<<&ptr_3<<endl;

// Pointer also has a addres which is obvious because it is also a variable so it will have a address



int* ptr_4 {};

cout<<ptr_4<<endl;

// If we dont intialize it will point to garabage memory address

// This is similar to all the variables 



// Size of all pointers is the same because it is just stores the adddress and all the addresses have same size irrespective of the data type the pointer is pointing to


// we know that all pointers have same size so why can't a integer pointer to a double pointer and it is not true because the type matters here and if we try to do here then it will give us a compiler error


// * is known as dereferencing operator when we are getting value from the pointer *ptr



vector <string> names {"Santosh","Reenakhi","Shakti","Snigdha"};

vector <string> *vec_ptr {&names};


// cout<<(*vec_ptr).at(0)<<endl;

// for (auto c:*vec_ptr){
//     cout<<c<<endl;
// }





// Dynamic Memory allocation


int *ptr_5 {nullptr};


ptr_5=new int {23};
// This will allocate a integer in the heap

// Whenever we do dynamic alloaction we allocate memory in heap


// cout<<*ptr_5<<endl;


// cout<<"Enter a integer : ";

// cin>>*ptr_5;


// cout<<*ptr_5<<endl;

// We can deallocate the space we made for integer

// cout<<ptr_5<<endl;

// delete ptr_5;

// cout<<ptr_5<<endl;




// We can also make array in the same way


int *ptr_6 {};


ptr_6=new int[20] {};

// a array of length 20 is allocated in memory

*(ptr_6+2)=2;
cout<<*(ptr_6+2)<<endl;



delete [] ptr_6;
// In this way we deallocate the memory for a array pointer


// before deleting the value stored in the address of pointer , we assign the pointer a new address then the value will be stored in the memory and there will be waste of memory


int *ptr_7 {};

ptr_7=new int[5];

for (int i{0};i<5;i++) *(ptr_7+i)=i;

cout<<"Pointer Increment \n";

ptr_7++;

cout<<*(ptr_7)<<endl;

// This will not give 0 instead it will give by 1 because we incremented the pointer by its size of data type which is quite logical

cout<<"Pointer Decrement \n";

ptr_7--;

cout<<*(ptr_7)<<endl;

ptr_7+=2;

cout<<*(ptr_7)<<endl;
// This will display 2
ptr_7-=1;

cout<<*(ptr_7)<<endl;

// This will display 1

// Pointer arithmetic is specific with the machine because it depends the size of the data type which is quite logical

int *ptr_8{};

ptr_8=new int[5];

for (int i{0};i<10;i+=2){

    *++ptr_8=i;

    // As * and ++ have the same priority and associativity is right to left and therefore it is first incremented and then dereferences the pointer
    // We know that ++ used in prefix returns the incremented value

}


ptr_8-=5;

for (int i{0};i<10;i+=2){

    cout<<*(++ptr_8)<<" ";
}
cout<<endl;

cout<<&ptr_8[3]-&ptr_8[0]<<endl;
// This will return 3 as they are stored contigously stored in the memory


typedef struct chain_member
{
    char public_key[65];
    char private_key[65];
} chain_member;



chain_member member_1;

strcpy(member_1.private_key,"f7888709d3af5bf33b801c647b3d2e74f4c989ca7e0cfee032d097fbdf238015");
strcpy(member_1.public_key,"a198af0f545d0fcc26c5dabadb4ec511b239c295e5e565ba17d059bc32efcb0a");
cout<<member_1.public_key<<endl;
cout<<member_1.private_key<<endl;


vector <int> nums_set {1,2,3,4};

// vector <int> nums_sub_set (0,2,nums_set);



int num_1 {20};
int num_2 {30};

const int* ptr_9 {&num_1};
// Pointer to constants

// *ptr_9=11;

// That is over here the data in the specific address the pointer is pointing to cannot be changed but the address in the pointer can be changed that is data in the pointer is not a constant that is address

int* const ptr_10 {&num_1};
// Here the address in the pointer cannot be changed that is constant pointers 


// ptr_10=&num_2;

*ptr_10=20;

cout<<*ptr_10<<endl;

const int* const ptr_11 {&num_1};

// Here the data as well as address cannot be changed that is constant pointer to constants

// ptr_11=&num_2;



// When we return a pointer from a function then we should always return a pointer which is dynamically allocated and we should avoid returning the address of a local variable of a function because its lifetime is till the execution of the function and also this is in the activation record of the stack and this may lead to problems so we should avoid doing this and we should always dynamically allocate a pointer because dynamic allocation takes place in heap



int *ptr_12=create_int_array(20,30);


cout<<ptr_12[2]<<endl;


// This array is allocated in heap


vector <int> nums_set_2 {1,2,3};
// nums_set_2.find(2)



union idproofs{
    long long aadhar_no;
    char pan_number[20]; 
} ;


typedef struct patient{
    string name;
    int age;
    idproofs idproof;

} patient;


patient patient1 ;

patient1.name="ABC";
patient1.age=100;
patient1.idproof.aadhar_no=41562718819919;

cout<<patient1.idproof.aadhar_no<<endl;

strcpy(patient1.idproof.pan_number,"19020020ABC");

cout<<patient1.idproof.aadhar_no<<endl;
cout<<patient1.idproof.pan_number<<endl;


// Union are allocates the space equal to space occupied by a element of highest size in memory which is quite logical
// We can use only one element of the union and define it and if again we try to define another element then it will store garbage value  in the previous element 




// Dangling pointers are the pointers which refer to the invalid memory location

// Like when pointers returned by a function which point to a address in a stack , they become invalid as soon as the activation record of the function if eliminated out of the stack

// When two pointers are pointing to a same memory location and now if we free any one of the pointer and we try to get the data stored in the address which freed pointer pointed to through another pointer then there may be some unpredicatable results


// Memory Leak

// This usually happen when we have a pointer pointing to a storage in a heap and we lose the pointer then we cannot get the data stored in the particular storage place in the heap and also this memory remains allocated 






vector <int> nums_set_3 {};

for (int i=0;i<=7;i++) nums_set_3.push_back(i);


for (auto &el: nums_set_3) el=20*el;

// Use of references

for (auto el: nums_set_3) cout<<el<<" ";

cout<<endl;



int num_3=200000;
int &refer=num_3;

// &refer=num_2;
// This is will error because we can create a reference for any one variable only and it should be declared and intialized simultaneously

// This can be somewhat similar to constant pointers
cout<<refer<<endl;
refer=20120;
cout<<num_3<<endl;


int * const ptr_13=&num_3;




cout<<*ptr_13<<endl;



// In range based for loop the for loop counter makes a copy of each element of respective data structure
// But we can make a reference by using a ampersan sign which is quite logical



// L-value and R-value

// L-value hold the name of the value and they are addressable
// they are modifiable if they are not constants

// references are referenced to l-values



// The main purpose of OOP is encapsulation

// C++ has destructpr function which are automatically called when objects has to be destroyed

// Procedural programming is what we have been doing

// Modularizing in Procedural programming is just breaking tasks into functions


// int a=1,b=2;
cout<< (1 ^ 2)<<endl;






Node *node_1=new Node();

// node_1 is a pointer to a node object


Node node_2;
cout<<node_2.IP_Address<<endl;
node_2.IP_Address="12345678";
node_2.Network_Name="Sigma";
cout<<node_2.IP_Address<<endl;



cout<<node_1->IP_Address<<endl;

// -> is Called Arrow operator which is a member of pointer operator
cout<<(*node_1).IP_Address<<endl;

// We need to use Parenthesis as dot operator has higher preference over asterik (*) operator



node_2.greeting();

node_1->greeting();



delete node_1;



// If we call a function whose prototype is only declared and if we call it then it will give a linker error







    return 0;
}

// Function Declarations


double penny(double penny_1,int n){
    if (n==1) return penny_1;
    return penny(2*penny_1,n-1);
}


void change_const(const int a[])
{
    cout << "Hello" << endl;
}

void metaverse(string name, string world)
{
    cout << "Your Avatar name is " << name << " and you are in " << world << " world" << endl;
}

int increment(int i)
{
    static int num = i;

    num++;
    return num;
}

void sigma(int a)
{
    cout << a << endl;
}
void sigma(double a)
{
    cout << a << endl;
}
void sigma(float a)
{
    cout << a << endl;
}

void sigma(string a)
{
    cout << a << endl;
}
void sigma(int a[], int length)
{
    for (int i{0}; i < length; i++)
    {
        cout << *(a + i) << " ";
    }
    cout << endl;
}
void sigma(vector<int> a)
{
    for (auto c : a)
        cout << c << " ";
    cout << endl;
}

void modify_variable(int &a)
{

    a = 20;

    // We modified the variable and we used apersan sign in front of the formal parameter to modify the variable

    // here a is allie to the actual parameter
}

void modify_vector(vector<int> &vec)
{
    for (int i{0}; i < vec.size(); i++)
    {
        vec[i] = 838;
    }
}

// Pass by reference saves extra space of copy

void print_vector(const vector<int> &vec)
{
    for (int i{0}; i < vec.size(); i++)
    {
        cout << vec[i] << " ";
    }

    cout << endl;
}



unsigned long long fibonacci(unsigned long long n){
    if (n==0) return 0;
    else if (n==1) return 1;
    else return fibonacci(n-1)+fibonacci(n-2);
}


int * create_int_array(size_t size,int initialization_value){
    int *array {};
    array=new int[size] {initialization_value};

    for (int i{1};i<size;i++) *(array+i)=initialization_value;


    return array;
    
}