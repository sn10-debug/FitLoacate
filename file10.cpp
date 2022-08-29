#include <iostream>
#include <string.h>


using namespace std;


template <typename T> class ArrayTemp{
public:
T* ptr;
int size;

ArrayTemp(int size_,T *arr):size{size_},ptr{arr}{


}


void disp(){

    for (int i=0;i<size;i++){
        cout<<*(ptr+i)<<" ";
    }
    cout<<endl;

}



};



struct Order{
string item_name;
double product_price;
};



int main(){

    int arr[] {1,2,3,4,5,6,7};
    ArrayTemp<int> arr1 {7,arr};
    arr1.disp();


    ArrayTemp <double> arr2 {8,new double[8]{1,2,3,4,5,6,7,8}};

    arr2.disp();


    ArrayTemp <string> arr3 {5,new string[5]{"Santosh Nayak","Reenakhi Santosh Nayak","Shakti Santosh Nayak","Snigdha Santosh Nayak","Sigma"}};
    arr3.disp();


    Order order_1 {"Biscuit",100};
    cout<<order_1.item_name<<endl;


    



    

    

}