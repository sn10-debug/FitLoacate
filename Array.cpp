#include <iostream>


using namespace std;



template <int N> class Array{


int *arr;
int size;
public:




Array():arr{new int[N]},size{N}{
    this->fill(0);
}

Array(int num):Array(){
    this->fill(num);
}


int length(){
    return size;
}


void fill(int num){

    for (int i=0;i<N;i++) arr[i]=num;
}


Array& append(int num){
    size++;

    int *temp=new int[size];

    for (int i=0;i<size-1;i++) temp[i]=arr[i];

    delete [] arr;

    temp[size-1]=num;

    arr=temp;

    return *this;

}



void pop(){
    int *temp=new int[size];
    size--;
    for (int i=0;i<size;i++) temp[i]=arr[i];

    delete [] arr;


    arr=temp;


}

void disp(){
    cout<<"[ ";
    for (int i=0;i<size-1;i++){
        cout<<arr[i]<<" , ";
    }
    cout<<arr[size-1];

    cout<<" ]"<<endl;
}



template <int L> void concat(Array<L> list){
    int *temp=new int [size+list.length()];

    for (int i=0;i<size;i++){
        temp[i]=arr[i];
    }

    for (int i=size;i<size+list.length();i++){
        temp[i]=list[i-size];

    }

    size+=list.length();

    delete [] arr;
    arr=temp;
    


}

int & operator[](int index){
    return arr[index];
}

template <int L> void operator=(Array <L> &rhs){


    delete [] arr;

    size=rhs.length();
    arr=new int[size];
    for (int i=0;i<size;i++) arr[i]=rhs[i];





}


};


template <int N> ostream& operator<<(ostream &os,Array<N> &lhs){

    lhs.disp();
    return os;
};




int main(){

    Array<3> arr1 {2};

    arr1.disp();

    cout<<arr1[2]<<endl;

    Array<5> arr2 {};
    arr2[3]=20;
    arr2.append(30).append(40).append(50);
    arr2.disp();




    arr2.pop();
    
    cout<<arr2;

    Array<2> arr3{}; 

    arr3=arr2;
    arr2=arr1;
    arr1.fill(0);
    arr2.append(40);

    cout<<arr1<<arr2<<arr3;

    arr3.concat(arr2);

    cout<<arr3;



    
    return 0;
}