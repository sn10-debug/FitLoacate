#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
using namespace std;

void print(const int* const nums_arr,size_t arr_size);

int* apply_all(const int* const arr1,size_t size1,const int* const arr2,size_t size2);

int main(){

    // int weight;
    // cin>>weight;
    // int weight_1=(weight/2);
    // int weight_2=weight-weight_1;
    // if (weight_1%2==0 and weight_2%2==0) cout<<"YES"<<endl;
    // else cout<<"NO"<<endl;

    // Challenge-1

    // int *ptr;

    // ptr=(int*) calloc(200,sizeof(int));

    // for (int i{0};i<200;i++) scanf("%d",ptr+i);

    // for (int i{60};i<=100;i++){
    // int num=0;
    //     for (int j{0};j<200;j++){
    //         if (*(ptr+j)==i) num+=1;
    //     }
    //     if (num>0){
    //         printf("%d - %d",i,num);
    //     }
    // }


    // Challenge-2

//     int *ptr;

//     int length;
//     printf("Enter the size of the array : ");
//     scanf("%d",&length);
//     ptr=(int*) calloc(length,sizeof(int));
// printf("Enter the number(s) : ");
//     for(int i{0};i<length;i++) scanf("%d",ptr+i);

//     int *ptr2;
//     int length2=0;

//     for(int i{0};i<length;i++){
//         bool present=0;
//         for (int j{0};j<length2;j++){
//             if (*(ptr2+j)==*(ptr+i)) {
//                 present=1;
//                 break;
//                 }
//         }
//         if (!present){
//             length2+=1;
//             ptr2 = (int*) realloc(ptr2,length2*sizeof(int));
//             ptr2[length2-1]=*(ptr+i);
            

//         }

//     }

// printf("length : %d \n",length2);
// for(int i{0};i<length2;i++) printf("%d ",*(ptr2+i));



int arr1[] {1,2,3,4,5};

int arr2[] {10,20,30};


print(arr1,5);

print(arr2,3);

int *results=apply_all(arr1,5,arr2,3);

print(results,15);

int var_1=20;
int **ptr_1 {};

// This stores the address of the pointers pointing to integers
int *ptr_2 {&var_1};

ptr_1=&ptr_2;


int testcases {};

cin>>testcases;

for(int l=0;l<testcases;l++){
    int n;
    int num;
    cin>>n;

    vector <int> *ptr;
    for (int i=0;i<n;i++) {
        int x;
        cin>>x;
        ptr->push_back(x);
        }

    while(ptr->size()!=0){
        int min=100;

        for (auto c:*ptr){
            if (c<min) min=c;

            
        }


    }
}


    return 0;




}


void print(const int* const nums_arr,size_t arr_size){

    for (int i=0;i<arr_size;i++) cout<<*(nums_arr+i)<<" ";
    cout<<endl;
}


int* apply_all(const int* const arr1,size_t size1,const int* const arr2,size_t size2){

    int *ptr=new int[size1*size2];

    for (int i=0;i<size1*size2;i+=size1){
        for (int j=0;j<size1;j++){
            ptr[i+j]=arr1[j]*arr2[i/size1];
        }
    }

    return ptr;

}