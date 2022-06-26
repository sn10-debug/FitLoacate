#include <stdio.h>


int main(void){

int n;
printf("Enter the number of integers : ");
scanf("%d",&n);

int arr[n];

for(int i=0;i<n;i++) scanf("%d",(arr+i));

int max=arr[0];
int index_month=0;
for (int i=0;i<n;i++){
    if (arr[i]>max) {
        max=arr[i];
        index_month=i;
        }
}

arr[index_month]=arr[0];
arr[0]=max;


for (int i=0;i<n;i++){
    printf("%d ",*(arr+i));
}



return 0;

}