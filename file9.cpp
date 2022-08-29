#include <iostream>
#include <stdio.h>
#include <memory>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <map>
#include <cctype>
#include <array>
#include <numeric>
#include <math.h>
#include <deque>
#include <forward_list>
#include <iterator>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>

#define NAME "SHAKTI SANTOSH NAYAK"

#define min(a, b) ((a < b) ? a : b)

#define max(a, b) ((a > b) ? a : b)

#define check(ptr) ((ptr == nullptr) ? "This is a null pointer" : "This is not a null pointer")

// As preprocessor does not knwo C++ and if we include semicolon and then it will also store the semicolon as value

// Before the compilation it will just check whether there is variable we defined as macros in the program and then it will just subsitute the value whatever we stored in that macro variable

using namespace std;

template <class L, class M>
void disp_queue(queue<L, M> q)
{

    cout << "[ ";
    while (!q.empty())
    {
        cout << q.front() << " ";
        q.pop();
    }
    cout << "]" << endl;
}

template <class T>
void fuck(T el)
{
    cout << el << endl;
}

class A
{
public:
    ~A()
    {
        cout << "Destructor Called" << endl;
    }
};

template <class t1, class t2>
class nums
{
public:
    t1 num1;
    t2 num2;
    nums(t1 n1, t2 n2) : num1{n1}, num2{n2}
    {
        cout << "Object Created\n";
    }
};

list<int>::iterator operator-(list<int>::iterator rhs, int a)
{
    for (int i = 0; i < a; i++)
    {
        --rhs;
    }

    return rhs;
}

list<int>::iterator operator+(list<int>::iterator rhs, int a)
{
    for (int i = 0; i < a; i++)
    {
        ++rhs;
    }

    return rhs;
}

template <typename T>
void disp_list(T nums)
{
    cout << "[ ";
    for (auto itr = nums.begin(); itr != nums.end(); itr++)
    {
        cout << *itr << " ";
    }
    cout << "]";
    cout << endl;
}

template <class t>
t temp_max(t a, t b)
{

    return ((a > b) ? a : b);
}

struct Square_Functor
{
    void operator()(int x)
    {
        cout << x * x << " ";
    }
};

void square(int x)
{
    cout << x * x << " ";
}

class Text
{
public:
    string str;

    Text(string s = "") : str{s}
    {
        cout << "Main constructor called : " << str << endl;
    }
    Text(const Text &source) : str{source.str}
    {
        cout << "Copy constructor called " << str << endl;
        cout << "-------" << endl;
    }
    Text(const Text &&source) : str{source.str}
    {

        cout << "Move constructor called " << str << endl;
        cout << "-------" << endl;
    }
};

template <typename T>
void getInfo(T container, string container_name)
{
    cout << "Name of the container is : " << container_name << endl;
    cout << "The elements of the Container : " << endl;
    disp_list(container);
    cout << "Number of elements in the Container : " << container.size() << endl;
    cout << "Number of Maximum elements that can be stored in the Container " << container.max_size() << endl;
    cout << "The first element of the Container is : " << container.front() << endl;
    auto itr = container.begin();
    itr++;
    cout << "The second element of the Container is : " << *itr << endl;
    cout << "The Last element of the Container is : " << container.back() << endl;
}

template <class L, class M>
void disp_stack(stack<L, M> s)
{
    vector<L> vec;

    while (!s.empty())
    {
        vec.push_back(s.top());
        s.pop();
    }

    reverse(vec.begin(), vec.end());

    disp_list(vec);
}

bool is_palindrome(string s)
{
    for_each(s.begin(), s.end(), [](auto &c)
             { c = tolower(c); });

    bool palindrome = 1;
    string s1{};

    copy_if(s.begin(), s.end(), back_inserter(s1), [](int c)
            { return c != ' '; });
    s = s1;
    // for (int i = 0; i < s1.size() / 2; i++)
    // {
    //     if (s1.at(i) != s1.at(s1.size() - 1 - i))
    //     {
    //         palindrome = 0;
    //         break;
    //     }
    // }

    // Another Method
    reverse(s1.begin(), s1.end());
    return (s == s1);
}

bool ispalindrome_with_stack(string s)
{

    queue<char> string_1;
    stack<char> string_2;

    for (auto c : s)
    {
        if (c != ' ')
        {
            char k = tolower(c);
            string_1.push(k);
            string_2.push(k);
        }
    }

    bool got = 1;

    while (!string_1.empty())
    {

        if (string_1.front() != string_2.top())
        {
            got = 0;
            break;
        }

        string_1.pop();
        string_2.pop();
    }

    return got;
}

int main()
{

    A *ptr = new A{};

    unique_ptr<A> ptr_2 = make_unique<A>();

    unique_ptr<A> ptr_3{move(ptr_2)};

    // ptr_3.reset();

    nums<int, float> num_1{2, 4.5};

    cout << num_1.num1 << endl;
    cout << num_1.num2 << endl;

    string a{"Shakti Santosh Nayak"};

    string b{a, 0, 2};

    cout << b;

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

    list<int> nums{1, 2, 3, 4, 10, 9, 8};

    list<int>::iterator itr = nums.end();
    itr--;
    list<int>::iterator itr2 = nums.begin();

    vector<int> nums_2{1, 2, 3, 4, 5, 10, 9, 38, 30};
    sort(nums_2.begin(), nums_2.end());

    // This sort function belongs to algorithm and thus the vector is sorted with the help of iterators

    for (auto c : nums_2)
    {
        cout << c << " ";
    }
    cout << endl;

    // Types of Containers

    // Sequence Containers

    // These are the containers which maintain the ordering of the elements

    // Examples:Array,vector,list,forward_list,deque

    // Associative Containers

    // These are the containers where the inserted elements may be ordered or undordered

    // This includes set,map,multi set,multi map

    // Container Adapters

    // These are the containers which do not support iterators and thus they cannot be used with stl algorithms

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

    for (itr; itr != itr2 - 1; itr--)
    {
        cout << *itr << " ";
    }
    cout << endl;

    int *ptr_4 = (int *)calloc(10, sizeof(int));

    int *ptr_5 = (int *)malloc(5 * sizeof(int));

    delete[] ptr_5;
    delete[] ptr_4;

    // Generic Programming is the type of programming where the code works with various types of arguements unless it makes sense to work with the various types

    cout << "List Section\n";

    list<int> list_1{1, 2, 3, 4};

    disp_list(list_1);

    list_1.insert(list_1.begin(), 5);

    disp_list(list_1);
    list_1.push_back(10);

    disp_list(list_1);

    list_1.sort();

    cout << "Elements Arranged in Ascending Order\n";
    disp_list(list_1);

    list_1.reverse();

    cout << "Elements Arranged in Descending Order\n";
    disp_list(list_1);

    list_1.emplace(list_1.begin(), 10);

    disp_list(list_1);

    list_1.unique();

    disp_list(list_1);

    cout << "The size of the list is " << list_1.size() << endl;

    // Macros

    // We should prefer not using

    // We have already used a Macros #define

    // In the context of header guards it is ok to use Macros

    // We already know that which begin with # sign are preprocessor directives

    // We also know that preprocessor does not know C++

    // Use of Macros

    cout << NAME << endl;

    cout << min(2, 7) << endl;
    cout << max(2, 7) << endl;

    cout << check(nullptr) << endl;

    cout << temp_max<float>(2.2, 5.5) << endl;

    cout << temp_max(12, 15) << endl;
    // char s[100];
    // printf("Input a string : ");
    // scanf("%[^\n]",&s);

    // printf("%s\n",s);

    // What type of elements we can store in Containers ?

    // Whenever we store a element in a container a copy of the particular element is stored and thus our object must support copy constructor/copy assignment.

    // Also for more efficiency move constructor / assignment should be supported by the objects

    // As containers can be compared and this comparison is done on the basis of the objects so they must support operator overloading of operator< and operator> and operator==

    // Iterators help us to work with any kind of sequence

    // Iterators are implemented as template classes

    // A iterator can be declared on the basis of the type of container

    // when we write vec.begin(), it represents the first element and when we write vec.end(),it represents 1 element after the last element

    // When the vector is empty then vec.begin() and vec.end() resemble the same thing

    vector<int> nums_3{1, 2, 3, 4, 5, 3939, 93030, 30300};

    sort(nums_3.begin(), nums_3.end());

    list<int> list_2{1, 2, 3, 4, 5, 6};

    list<int>::iterator itr3 = list_2.begin();

    for (auto i = itr3; i != list_2.end(); i++)
    {
        cout << *i << " ";
    }

    cout << endl;

    vector<int>::iterator itr4 = nums_3.begin();

    vector<int>::reverse_iterator itr5 = nums_3.rbegin();

    // This is a reverse iterator used to reverse through the container

    // cbegin() and cend() are the methods which returns a const iterators else they are same as begin() and end() iterator
    // crbegin() and crend() are the methods which returns a const iterators else they are same as rbegin() and rend() iterator

    // We can add a constant number to iterators of vector

    // it+=2 or it=it+4;

    for (auto i = itr4; i != nums_3.end(); i++)
    {

        cout << *i << " ";
    }

    cout << endl;

    for (auto i = itr5; i != nums_3.rend(); i++)
    {

        cout << *i << " ";
    }

    cout << endl;

    // In case of constant iterators the only thing is that we cannot change the value stored in it but we can increment and decrement the iterator

    map<string, string> obj1{
        {"Hello", "World"},
        {"Member-1", "Santosh Nayak"},
        {"Member-2", "Reenakhi Santosh Nayak"},
        {"Member-3", "Shakti Santosh Nayak"},
        {"Member-4", "Snigdha Santosh Nayak"}};

    auto itr6 = obj1.begin();

    while (itr6 != obj1.end())
    {
        cout << itr6->first << " : " << itr6->second << endl;

        // first attribute represents the key and second attribute represents the value and thus making the key-value pair

        itr6++;
    }

    // STL algorithms work on the sequences with the help of iterators

    // STL algorithms sometimes need some extra information in order to do their work which are as follows:
    // 1. Functors(function objects)
    // 2. function pointers
    // 3. lambda expressions

    // Iterator Invalidation

    // Suppose while iterating through a vector using an iterator , we clear the vector and thus iterator will be pointing to a invalid location and thus what will be the behaviour in this situation is undefined

    // Every container documentation contains information about when iterators become invalid

    // FIND FUNCTION

    // This function returns a iterator if the entered element is found in the sequence and if the element is not found then it returns the end iterator

    vector<int> nums_4{838, 34, 399, 299, 2838};
    auto itr7 = find(nums_4.begin(), nums_4.end(), 34);

    // This will find the find the first occurence of the entered element

    // If we want to use the find function for the sequence of user defined object then we need to overload operator== for the user defined objects

    if (itr7 != nums_4.end())
        cout << "Element found and its value is : " << *itr7;
    else
        cout << 34 << " not found in the sequence";

    cout << endl;

    // FOREACH Function

    // Using functor that is function objects

    Square_Functor square_1{};

    for_each(list_2.begin(), list_2.end(), square_1);

    cout << endl;

    // overloaded operator function in square object will be called on each element of the sequence

    // Using function pointers

    for_each(list_2.begin(), list_2.end(), square);

    cout << endl;

    // Using lambda Expressions

    // for_each(list_2.begin(),list_2.end(),[](int value){
    //     cout<<value*value<<" ";
    // });
    // cout<<endl;

    for_each(begin(list_2), end(list_2), [](int value)
             { cout << value * value << " "; });
    cout << endl;

    // This is another type of syntax to mention the beginnning iterator or the ending iterator

    list<int> list_3{1, 2, 1, 3};

    auto itr8 = find(list_3.begin(), list_3.end(), 1);

    itr8 = find(++itr8, list_3.end(), 1);

    cout << *itr8 << endl;

    cout << *++itr8 << endl;

    // COUNT FUNCTION

    cout << "Occurences of 1 in list : " << endl;

    disp_list(list_3);

    cout << count(list_3.begin(), list_3.end(), 1) << endl;

    // COUNT_IF FUNCTION

    // We can also count number of elements which follow certain condition

    list<int> list_4{2, 4, 5, 6, 7, 10, 17, 18, 181, 1001, 13};

    cout << "Even Numbers in the list : ";
    disp_list(list_4);
    cout << count_if(list_4.begin(), list_4.end(), [](int x)
                     { return x % 2 == 0; })
         << " even numbers\n";

    cout << "Odd Numbers in the list : ";
    disp_list(list_4);
    cout << count_if(list_4.begin(), list_4.end(), [](int x)
                     { return x % 2 != 0; })
         << " odd numbers\n";

    // count_if are similar to find and filter functions in javsccript where we return a boolean

    // REPLACE FUNCTION

    vector<int> nums_5{1, 3, 4, 45, 6, 5, 5, 7, 5, 4, 5};

    disp_list(nums_5);

    cout << "All 5 replaced 50" << endl;
    replace(nums_5.begin(), nums_5.end(), 5, 50);

    disp_list(nums_5);

    // ALL_OF FUNCTION

    if (all_of(nums_5.begin(), nums_5.end(), [](int x)
               { return (x < 100); }))
    {
        cout << "All the numbers in the list : ";
        disp_list(nums_5);
        cout << "are less than 100\n";
    }

    else
    {
        cout << "All the numbers in the list : ";
        disp_list(nums_5);
        cout << "are not less than 100\n";
    }

    // ANY_OF FUNCTION

    if (any_of(nums_5.begin(), nums_5.end(), [](int x)
               { return (x >= 50); }))
    {
        cout << "Some numbers in the list : ";
        disp_list(nums_5);
        cout << "are greater than equal to 50\n";
    }

    else
    {
        cout << "No numbers in the list : ";
        disp_list(nums_5);
        cout << "are greater than equal to 50\n";
    }

    // TRANSFORM FUNCTION

    string name{"Shakti Santosh Nayak"};

    cout << name << endl;

    transform(name.begin(), name.end(), name.begin(), ::toupper);

    // As we know that toupper can be applied for each character and thus we are doing here

    cout << name << endl;

    // Whenever we want to use a container of fixed size and array like container
    // We can use the Array container

    // We can easily access the elements of the Array whatever the size of the array maybe
    // We can also access the underlying raw array inside the Array container

    // ARRAY

    array<int, 5> Array_1{1, 2, 3, 4};

    cout << "The size of the Array : ";
    cout << Array_1.max_size() << endl;

    // This will give the size of the array not the number of elements present in it
    cout << "First Element of the Array : ";
    cout << Array_1.front() << endl;
    cout << "Last Element of the Array : ";
    cout << Array_1.back() << endl;

    // This will tell 0 because we have not initialized the last value and thus it will by default initialize to 0

    Array_1 = {1, 2, 3, 4, 5};

    // We can change the overall array in this way

    cout << "Last Element of the Array : ";
    cout << Array_1.back() << endl;

    array<int, 5> Array_2{6, 7, 8, 9, 10};

    for (auto itr = Array_1.begin(); itr != Array_1.end(); itr++)
    {
        cout << *itr << " ";
    }

    cout << endl;

    for (auto itr = Array_2.begin(); itr != Array_2.end(); itr++)
    {
        cout << *itr << " ";
    }

    cout << endl;

    Array_1.swap(Array_2);

    // From here we come to know that the values of both the array are swapped
    for (auto itr = Array_1.begin(); itr != Array_1.end(); itr++)
    {
        cout << *itr << " ";
    }

    cout << endl;

    for (auto itr = Array_2.begin(); itr != Array_2.end(); itr++)
    {
        cout << *itr << " ";
    }

    cout << endl;

    // When we want to dereference a value from the vector we use at method which does bound checking but with subscript operator there is no bound checking
    cout << boolalpha;
    cout << "Checking whether the Array is empty or not : " << Array_1.empty() << endl;

    int *Array_pointer = Array_1.data();

    // .data() method provides the pointer to the raw array

    // There is also fill method

    Array_1.fill(0);

    cout << *Array_pointer << endl;

    *(Array_pointer + 1) = 20;
    cout << *(Array_pointer + 1) << endl;

    vector<int> nums_6{100, 200, 300, 400, 500};
    for (auto &c : nums_6)
    {
        c = 2 * c;
    }

    // MIN_ELEMENT and MAX_ELEMENT

    auto min = min_element(nums_6.begin(), nums_6.end());
    auto max = max_element(nums_6.begin(), nums_6.end());

    // This returns a iterator

    cout << "Minimum element : " << *min << '\n';
    cout << "Maximum element : " << *max << '\n';

    // ADJACENT_FIND

    array<int, 8> Array_3{1, 2, 3, 3, 4, 5, 5, 6};

    auto value = adjacent_find(Array_3.begin(), Array_3.end());

    // This will return the iterator of the value1 where its next value is also equal to value1 and also the first occurence

    cout << *value << endl;

    cout << "Sum of elements in Array3 : " << accumulate(Array_3.begin(), Array_3.end(), 0) << endl;

    // We know that 0 is the initial value

    array<string, 3> Array_4{"Shakti ", "Santosh ", "Nayak "};

    cout << accumulate(Array_4.begin(), Array_4.end(), string{""}) << endl;

    vector<int> nums_7(5, 600);

    // vector takes constant time to add or delete any element at the back of the vector

    // vector takes linear time to add or delete any element at the random position

    cout << nums_7.at(3) << endl;

    nums_7 = {1, 2, 3, 4};
    cout << nums_7.at(3) << endl;

    cout << nums_7.size() << endl;
    // This gives the number of elements in the vector

    cout << nums_7.capacity() << endl;

    // This depends upon the vector if the capacity goes out of limit then dynamic allocation takes place
    // Now this will return 5 because first we initialized the vector with 5 values and now with assignment 4 values but already the capacity has become 5 initially . If we try to add 6 elements with assignment then its capacity and size will become same because capacity has increased to accomodate more elements

    cout << nums_7.max_size() << endl;

    // This will be a huge number and this will depend upon the system

    vector<Text> texts{};

    texts.push_back(Text{"Hello world"});
    texts.pop_back();

    texts.emplace_back("Hello Whatsup ? ");

    // This emplace_back method directly takes the parameters we need to provide for the class

    cout << texts.at(0).str << endl;

    // Here no copy or move is involved, it happens in the normal way as we initialize

    cout << texts.empty() << endl;

    // This will tell whether the vector is empty or not

    nums_7 = {400, 27, 28, 7, 99, 83};
    sort(nums_7.begin(), nums_7.end());

    reverse(nums_7.begin(), nums_7.end());

    nums_7.swap(nums_6);

    cout << nums_6.at(0) << endl;

    //     for (auto &c : nums_7)
    //     cout << c << " ";
    // cout << endl;

    // Only the type has to be same rest size can be different

    // INSERTING ELEMENTS

    nums_7 = {1, 2, 3, 4, 5, 7};

    nums_7.shrink_to_fit();

    // This will make the size and capacity of vector equal

    auto itr9 = find(nums_7.begin(), nums_7.end(), 7);

    // Now we can insert a element at the position of 7 and before 7

    nums_7.insert(itr9, 10);
    itr9 = find(nums_7.begin(), nums_7.end(), 7);

    // We can insert a whole sequence as well
    nums_7.insert(itr9, nums_6.begin(), nums_6.end());

    // reserve method

    nums_7.reserve(100);
    // This will increase the capacity to 100

    nums_7.erase(nums_7.begin(), nums_7.begin() + 2);

    // This will delete the first two elements that is excluding the second arguement but including the first arguement

    for (auto &c : nums_7)
        cout << c << " ";
    cout << endl;

    // Removing the odd numbers

    auto itr10 = nums_7.begin();

    while (itr10 != nums_7.end())
    {
        if ((*itr10) % 2 != 0)
            nums_7.erase(itr10);
        else
            itr10++;
    }

    for (auto &c : nums_7)
        cout << c << " ";
    cout << endl;

    cout << nums_7.capacity() << endl;

    // 100 as we have already reserved space for 100 integers

    // Finding Greatest Common Divisor

    int x = 20, y = 40;

    while (x != y)
    {
        if (x > y)
            x -= y;
        else
            y -= x;
    }

    cout << x << endl;

    // Copy function

    vector<long long> nums_8{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vector<long long> nums_9{400, 500};

    disp_list(nums_9);
    for_each(nums_9.begin(), nums_9.end(), [](auto &x)
             { x *= pow(10, 13); });

    disp_list(nums_9);

    copy(nums_8.begin(), nums_8.end(), back_inserter(nums_9));
    // copying nums_8 vector to nums_9 vector string from the back of the nums_9

    disp_list(nums_9);

    // Copy_if

    // This will only the elements of the sequence if the particular element follows a condition

    copy_if(nums_8.begin(), nums_8.end(), back_inserter(nums_9), [](int x)
            { return (x % 2 == 0); });
    disp_list(nums_9);

    // back_inserted returns the end iterator

    // Transform function

    // This expects two containers

    vector<int> nums_10{1, 2, 3, 4, 5};
    vector<int> nums_11(5, 20);
    vector<int> nums_12{};

    transform(nums_10.begin(), nums_10.end(), nums_11.begin(), back_inserter(nums_12), [](int x, int y)
              { return x * y; });

    disp_list(nums_10);
    disp_list(nums_11);
    disp_list(nums_12);

    // DEQUE CONTAINER

    // They are dynamic in size
    // Insertion and deletion of elements occurs at both front and back and this occurs at constant time
    // While insertion in between occurs at linear time

    // Elements here are not stored in contigous memory

    // Deque contains memory block which consists of the elements of the deque and this elements are contigous in memory block but the memory blocks are not contigous in memory

    deque<int> deque_1{1, 2, 3, 4, 5};
    deque<string> deque_2{"Santosh Nayak", "Reenakhi Santosh Nayak", "Shakti Santosh Nayak", "Snigdha Santosh Nayak"};

    deque_2.push_front("Family deque_2 : ");
    deque_2.push_back("4 deque_2 ");

    disp_list(deque_2);
    getInfo(deque_2, "Deque");

    deque<int> deque_3{6, 7, 8, 9, 10};

    copy(deque_3.begin(), deque_3.end(), back_inserter(deque_1));
    copy_if(deque_3.begin(), deque_3.end(), back_inserter(deque_1), [](int x)
            { return (x % 2 == 0); });
    copy(deque_3.begin(), deque_3.end(), front_inserter(deque_1));

    // In deque we can copy things from front as well
    getInfo(deque_1, "Deque");

    // Inserting elements at the middle of the deque is not efficient , we should prefer list for inserting elements in the middle

    cout << is_palindrome(string{"toot"}) << endl;
    cout << is_palindrome(string{"A Santa at NASA"}) << endl;

    // string str1;

    // reverse(str1.begin(),str1.end());

    // LIST AND FORWARD LIST

    // They are both sequence containers

    // We cannot the access the elements directly

    // They are not contigous in memory

    // Here insertion and deletion is very efficient if once the element is found

    // List is a doubly linked list

    // Though elements are not contigous in memory but the element contain references to the neighbouring elements like in the case of doubly link list if they exist

    list<int> list_5{100, 200, 300, 400, 500, 600};
    getInfo(list_5, "List");

    list_5 = {1, 2, 3, 4, 5};
    // They support assignment as well
    list_5.push_back(6);
    list_5.push_front(0);

    auto itr11 = find(list_5.begin(), list_5.end(), 6);

    list_5.insert(itr11, deque_3.begin(), deque_3.end());

    list_5.erase(itr11);

    // this iterators still points to 6 and it will remove it and now it will be invalidated as it erases that element

    disp_list(list_5);

    list_5.pop_front();
    list_5.pop_back();
    disp_list(list_5);

    // We can use emplace_front and emplace_back here also as well as deque also

    // resize method

    list_5.resize(3);
    // It's size will become 3 and will contain first 3 elements and all the elements after it will be removed

    list_5.resize(7);
    // We know that there are 3 elements and rest other elements will initialized to the default values and here in the case of integers it is 0

    // FORWARD LIST

    // The forward list acts as a singly linked list

    // Reverse iterators are not available for forward list and iterators invalidate after deletion same as list

    // Rest everything is same as list

    // Elements can be inserted anywhere in list

    forward_list<string> greetings{"Hello World", "Good Morning", "Good Afternoon", "Good Evening", "Good Night"};

    greetings.push_front("Hello Whatsup ?");
    // Forward list only has push_front and pop_front and front

    cout << greetings.front() << endl;

    greetings.pop_front();

    // There is no size method attached to forward_list

    auto itr12 = find(greetings.begin(), greetings.end(), "Hello World");

    greetings.insert_after(itr12, "Hey Whatsup ?");

    greetings.erase_after(itr12);
    // This will delete "Hey Whatsup ?"

    // greetings.resize(20);

    // greetings.resize(greetings.max_size());

    // Also there is emplace_front() only with forward_list

    greetings.emplace_after(itr12, "Hey Wahtsup ?");

    itr12 = find(greetings.begin(), greetings.end(), "Good Night");

    list<int> list_6{3000, 6000, 9000, 12000, 15000, 18000};

    // itr12 will start pointing three elements behind the current element

    auto itr13 = find(list_6.begin(), list_6.end(), 18000);

    advance(itr13, -2);

    cout << *itr13 << endl;

    // Associative Containers

    // This includes set and maps

    // Collection of stored objects that allow fast retreival using a key
    // They are behind the scenes are applied as binary tree and therefore we can perform fast operations on them and they are highly efficient

    // The STL consists of 4 types of set

    // 1. Ordered Set <set>
    // 2. Unordered Set <unordered_set>
    // 3. Ordered Multiset <multiset>
    // 4. Unordered Multiset <unordered_multiset>

    set<int> set1{1, 2, 3, 4, 6, 5, 5, 5};

    // for (auto itr=set1.begin(),itr!=set1.end();itr++){
    //     cout<<*itr;
    // }

    // Also the set is sorted

    disp_list(set1);

    // There are push_front or push_back method associated with sets

    set1.insert(-20);

    disp_list(set1);

    cout << set1.size() << endl;
    cout << set1.max_size() << endl;

    // When we insert a element into the set it returns a pair and the first element is the iteartor to the added element and if an element is already present in set then it is an iterator to that element
    // The second element says whether the element was added successfully or not

    auto pair1 = set1.insert(20);
    auto pair2 = set1.insert(20);

    // This returs std::pair type

    cout << *pair1.first << " " << pair1.second << endl;
    cout << *pair2.first << " " << pair2.second << endl;
    // pair.second will return false because we know that 20 is already present in the set and so again it cannot be added

    // erase method

    set<double> set2{1.0, 2.2, 30, 12, 81.9};

    disp_list(set2);
    set2.erase(12);

    auto itr14 = set2.find(30);

    // We should use find method of the set because it knows all about the implementation of the set and thus this is more efficient

    if (itr14 != set2.end())
        cout << *itr14 << endl;

    disp_list(set2);

    cout << set2.count(12) << endl;

    // Obviously count will return 0 or 1 because we can have only one occurence of the element

    set2.clear();

    multiset<int> multiset1{1, 2, 3, 4, 5};

    // unordered_set

    // In case of unordered_set we cannot add duplicate elements in case of set and also we cannot modify the element into it

    // No reverese iterators are allowed for them

    unordered_set<int> unordered1{1, 2, 3, 10, 4, 5, 6, 7};

    // This will be in not a order and also not sorted like ordered set

    unordered_set<int>::iterator itr15 = unordered1.find(2);

    disp_list(unordered1);

    // *itr15 = 20;

    // This will give an error

    unordered_multiset<int> unordered2{1, 1, 2, 2, 2, 3, 4};

    auto itr16 = unordered2.find(3);

    // *itr16 = 11;

    // This will give an error
    disp_list(unordered2);

    // In set we need to overload (<) operator as it uses while sorting for our own user defined objects
    set2 = {1, 2, 3, 4};

    // While emplacing also this checks for (<) operator to find whether the element is already present in the set or not

    // In find method it uses (<) operator because this all works on binary tree and how searching in binary tree we already know

    // Maps

    // They allow fast retrieval using a key

    // They are also implemented as binary tree or hashsets

    // They are efficient to use

    // This also has 4 types

    /* 1. Ordered map
    2. Unordered map
    3. Ordered multimap
    4. Unordered multimap

    */

    //    MAP

    // They are key value pairs
    //    They are ordered by keys

    // Values can be obtained using the key

    // Keys must be unique in a map

    // It supports all type of iterators and they invalidate when the corresponding element is deleted

    map<string, int> map_1{
        {"num1", 1},
        {"num2", 2},
        {"num3", 3}};

    cout << map_1.size() << endl;
    // Returns Number of elements in the

    pair<string, int> pair3{"num4", 4};

    map_1.insert(pair3);

    map_1.insert(make_pair("num5", 5));

    // This will automatically make the key-value pair

    // There is no concept of front and back in Map

    map_1["num6"] = 6;

    // We can insert element this way also like we do in dictionary in python and object in javascript

    cout << map_1["num6"] << endl;
    cout << map_1.at("num5") << endl;

    map_1.erase("num6");

    auto itr17 = map_1.find("num4");

    cout << itr17->first << " : " << itr17->second << endl;

    // There is also count method associated with map which can be used to determine whether the element is present or not

    // As count will 0 or 1 only

    map_1.empty();

    // Boolean value

    map_1.clear();

    // Clears the whole map

    if ((map_1.begin() == map_1.end()) and map_1.empty())
        cout << "Whole Map Cleared" << endl;

    // In case of multi_map

    // They are sorted by key
    // Duplicate elements are allowed

    multimap<string, string> multimap_1{{"Hello", "World"}, {"Hello", "Morning"}};

    cout << multimap_1.find("Hello")->first << " : " << multimap_1.find("Hello")->second << endl;

    cout << "The number of Hello's in mutimap is " << multimap_1.count("Hello") << endl;

    unordered_map<string, string> unordered_map_1{{"Hey", "There"}};

    // Here elements are not ordered

    // No reverse iterators are allowed

    cout << unordered_map_1.at("Hey") << endl;

    // STACK

    // This is LIFO (Last in first out) data structure

    // Implemented as a Apdapter so it can be implemented over vector,deque and list

    // Here we can do operations on one end that is back of the stack

    // Stack does not supports iterator and also there is no need of iterators because all the operations are done on one side of the stack that is back

    // Methods associated with stack

    // push - add elements to the top of the stack
    // pop- remove any element from the top of the stack
    // top - this returns the element which is at the top of the stack and this returns a reference and thus can be modified
    // empty - this tells whether the stack is empty or not
    // size - this tells the number of elements present in the stack

    // As stack is a adapter class so we need to define whether what will be underlying container that should be used by the stack with the primitive type and by default a stack uses a deque if we don't provide the information about underlying container

    stack<int> stack_1{};
    stack<int, vector<int>> stack_2{};
    stack<int, list<int>> stack_3{};
    stack<int, deque<int>> stack_4{};

    stack_1.push(20);
    fuck(stack_1.top());
    // stack_1.pop();

    // cout << stack_1.size() << endl;

    fuck(stack_1.size());

    for (int i = 100; i < 500; i += 100)
    {
        stack_2.push(i);
    }

    stack_2.top() = 500;
    disp_stack<int, vector<int>>(stack_2);
    disp_stack(stack_1);

    for (int c : {100, 200, 300})
    {
        cout << c << " ";
    }
    cout << endl;

    // Queue

    // This is a FIFO (First in First Out) Data structure

    // This is a Adapter class and thus it can be extended over list and deque

    // ELements are pushed at the back and removed from the front

    // This does not support iterator

    // This has 6 methods associated with it

    // push-This is used to put the element at the back
    // pop-This is used to remove the element from the front

    // front-This gives the reference of first element of the queue
    // back-This gives the reference of last element of the queue

    // empty-This finds out whether the queue is empty or not
    // size-This finds out the number of elements in the queue

    queue<int> queue_1{};

    // By default deque
    queue<int, list<int>> queue_2{};
    queue<int, deque<int>> queue_3{};

    queue_1.push(200);
    for (int i = 300; i <= 700; i += 100)
        queue_1.push(i);

    cout << queue_1.front() << " " << queue_1.back() << endl;

    queue_1.pop();

    cout << queue_1.front() << " " << queue_1.back() << endl;

    cout << "The number of elements in the queue : " << queue_1.size() << endl;

    disp_queue(queue_1);

    cout << boolalpha;

    cout << ispalindrome_with_stack("A Santa at Nasa") << endl;

    cout << ispalindrome_with_stack("A Toyotas a toyota") << endl;
    cout << ispalindrome_with_stack("Hello") << endl;

    // Priority queue

    // Here insertion and deletion takes place at the front of the container
    // Internally this uses a vector

    // This uses a data structure called heap and more specifically max heap

    // Elements are inserted in priority order (That is the largest element will be present at the front)

    // This does not supports iterators

    priority_queue<int> pq_1{};

    for (int i = 100; i >= 0; i -= 20)
    {
        pq_1.push(i);
    }

    cout << pq_1.top() << endl;

    // This will return the maximum element of the priority queue

    pq_1.pop();

    cout << pq_1.top() << endl;

    // less than operator has to be overloaded for user defined types

    // deque_1.insert();

    return 0;
}