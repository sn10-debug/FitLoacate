#include <iostream>
// #include <cctype>
// #include <iomanip>
#include <vector>
// #include <array>
// #include <list>
// #include <deque>
// #include <map>
#include <set>
// #include <queue>
// #include <stack>
#include <algorithm>
// #include <iterator>
#include <functional>

using namespace std;

template <class T>
void display(T seq)
{

    cout << "[ ";
    for (auto itr = seq.begin(); itr != seq.end(); itr++)
    {
        cout << *itr << " ";
    }
    cout << "]" << endl;
}

class Adder
{
    int num;

public:
    Adder() : num{0} {}
    Adder(int n) : num{n} {}

    int operator()(int n)
    {

        return num + n;
    }
};

template <class T>
class Displayer
{

public:
    void operator()(T x)
    {
        cout << x << " ";
    }
};

template <class T>
void take_lambda(function<void(T)> func, T value)
{
    func(value);
}

template <class T>
void take_lambda(void (*func)(T), T value)
{
    func(value);
}

// Another way of calling the calling the function

// This both the ways was introduced in C++14

template <class T>
void take_lambda(auto func, T value)
{
    func(value);
}

// This was introduced in C++20

using namespace std;

int main()
{

    // Lambda Expressions

    // There are two types of Lambda Expressions

    // 1. Stateless Lambda Expressions
    // 2. Stateful Lambda Expressions

    // In Stateful Lambda Expressions the concept of closure is used

    // The motivation behind Lambda expressions are that we have to write many small function for using stl using function pointers

    // Also many function objects overloaded with () operator and this give rises to many small classes

    // Also the decalaration of the functions and the classes are faraway so may lead to problems

    cout << "This section is of Lambda Expressions \n";

    Adder add{2};

    vector<int> nums_1{200, 300, 400, 500};

    display(nums_1);

    transform(nums_1.begin(), nums_1.end(), nums_1.begin(), add);
    // This will transform all the elements starting from nums_1.begin()
    transform(nums_1.begin(), nums_1.end(), nums_1.begin(), add);

    display(nums_1);

    for_each(nums_1.begin(), nums_1.end(), [](int x)
             { cout << x << " "; });

    cout << endl;

    // Lambda expressions also provide the closure objects

    // We should use Lambda expressions when we have less number of statements to get executed or for complex code we should always prefer function objects

    // Lambdas are converted into function objects behind the scenes

    for_each(nums_1.begin(), nums_1.end(), Displayer<int>());

    cout << endl;

    // []()->return_type specifiers {}

    // [] is called as capture list which can help us capture the closure or context

    // () takes the parameter separated with commas

    // return_type is the return type of the value returned by the function and this can be omitted as the compiler can deduce it

    // specifiers are mutable and constexpr

    // The curly brackets contain the statements of the function

    []() -> void
    {
        cout << "Hello World" << endl;
    }();

    int a = []() -> int
    {
        return 2;
    }();
    cout << a << endl;

    [](int x)
    {
        cout << "The number is " << x << endl;
    }(10);

    auto disp_value =
        [](string x)
    {
        cout << x << endl;
    };

    disp_value("Hey ! Whatsup ?");

    // This all are stateless lambda functions where the capture list is empty

    // Empty capture list means it does not capture any information about the environment ,only keeps information about the parameters in the parameter list and that is stateless lambda functions

    // This stateless lambda functions does not have any information about the environment variables that is the global variables

    auto disp_any_value = [](auto x)
    { cout << x << endl; };

    disp_any_value(12);
    disp_any_value("Hello this is Shakti Santosh Nayak");

    // Passing Lambda expression into a function

    take_lambda<string>(disp_any_value, "Hello Lambda is successfully called");
    take_lambda<int>(disp_any_value, 20);
    take_lambda(disp_any_value, "Random Value");

    // A Predicate lambda is the lambda which takes a arguement and returns a boolean

    function<void(int)> x = [](int y)
    {
        cout << y << endl;
    };

    x(303);

    set<int> nums_2{};

    nums_2.insert(20);
    nums_2.insert(30);
    auto itr = nums_2.begin();
    itr++;

    cout << *itr << endl;

    return 0;
}