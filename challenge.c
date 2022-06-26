#include <stdio.h>
#include <math.h>
#include <string.h>

#include <stdlib.h>


// double average(double num1,double num2) {
//     double avg=0;
// avg=(num1+num2)/2;

//     return avg;
// }

int sum(int length,int nums[length]){
for (int i=0;i<length;i++) printf("%d\n",nums[i]);
}


int token(){
    static int token_number=0;
    token_number++;
    return token_number;

}


int main(void){

    

// float marks1,marks2,marks3;

// scanf("%f\n",&marks1);
// scanf("%f\n",&marks2);
// scanf("%f",&marks3);

// float percent1,percent2,percent3;
// percent1=marks1/50;
// percent2=marks2/50;
// percent3=marks3/100;

// float result;

// result=percent1*25+percent2*25+percent3*50;

// printf("%f\n",result);



// char grade;
// int roll;
// float percentage;


// scanf("%c",&grade);
// scanf("%d",&roll);
// scanf("%f",&percentage);

// printf("%c\n%d\n%f",grade,roll,percentage);

// Problem-1 


// printf("The size of short is %d\n",sizeof(short));
// printf("The size of int is %d\n",sizeof(int));
// printf("The size of long is %d\n",sizeof(long));
// printf("The size of long long is %d\n",sizeof(long long));
// printf("The size of float is %d\n",sizeof(float));
// printf("The size of double is %d\n",sizeof(double));
// printf("The size of long double is %d\n",sizeof(long double));
// printf("The size of long double is %d\n",sizeof(char));
// printf("The size of long double is %d\n",sizeof(void));



// Problem-2


// Taking salary per hour and number of hours as input

// float hour_salary,num_hours;

// printf("Enter your hourly salary : ");
// scanf("%f",&hour_salary);
// printf("Enter the number of hours worked : ");
// scanf("%f",&num_hours);
// float salary=hour_salary*num_hours;
// printf("The salary is %.2f",salary);


// Problem-3


// Miles to kilometers

// float distance;

// printf("Enter the distance in miles : ");
// scanf("%f",&distance);
// // The format specifier for double is %g
// printf("The distance is %.2f miles\n",distance);
// printf("The distance in kilometers is %.2f",distance*1.609);



// Problem-4


// Area of a circle

// float radius;

// printf("Enter the radius of the circle : ");
// scanf("%f",&radius);

// printf("The area of the circle is %.2f",M_PI*radius*radius);



// Problem-5

// float distance,miles_per_gallon,price_gallon;

// printf("Enter the distance in miles : ");
// scanf("%f",&distance);
// printf("Enter the miles per gallon with the vehicle : ");
// scanf("%f",&miles_per_gallon);
// printf("Enter the current price of gallon : ");
// scanf("%f",&price_gallon);

// float gallons=distance/miles_per_gallon;
// printf("The number of galons of fuel required : %f\n",gallons);
// printf("The price for the fuel is : %f\n",price_gallon*gallons);




// Problem-6


// float principal,rate,time_period;


// printf("Enter the principal amount : ");
// scanf("%f",&principal);

// printf("Enter the rate (percent): ");
// scanf("%f",&rate);

// printf("Enter the lock in period (years): ");
// scanf("%f",&time_period);
// float simple_interest=(principal*rate*time_period)/100;
// printf("The simple interest on %.2f for %.2f years with rate %.2f percent is %.2f\n",principal,time_period,rate,simple_interest);
// printf("The simple interest is %f",simple_interest);




// Problem-7



// Get quotient and remainder


// int numerator,denominator;

// printf("Enter the numerator : ");
// scanf("%d",&numerator);
// printf("Enter the denominator : ");
// scanf("%d",&denominator);


// int quotient=numerator/denominator;

// int remainder=numerator%denominator;

// // Modulo can be used with integers only


// printf("The quotient is %d\n",quotient);
// printf("The remainder is %d",remainder);




// Problem-8

// Getting the rightmost character of a number


// int number;

// printf("Enter the number : ");
// scanf("%d",&number);

// printf("The rightmost character of the number is %d",number%10);



// Problem-9


// Total amount for a sale


// float unit_price,discount_rate,tax_rate;
// int quantity;

// printf("Enter the unit price of the product : ");
// scanf("%f",&unit_price);
// printf("Enter the quantity of the product : ");
// scanf("%d",&quantity);
// printf("Enter the discount percentage : ");
// scanf("%f",&discount_rate);
// printf("Enter the rate of tax to be levied on the product : ");
// scanf("%f",&tax_rate);

// float discount=unit_price*quantity*discount_rate/100;
// float tax=(unit_price*quantity-discount)*tax_rate/100;

// float total_amount=unit_price*quantity-discount+tax;

// printf("The sale amount is %.2f",total_amount);




// Problem-10


// Number of dots required


// int num_rows_1;

// printf("Enter the number of rows : ");
// scanf("%d",&num_rows_1);
// int num_dots=(num_rows_1*(num_rows_1+1))/2;

// printf("The number of dots required is %d",num_dots);





// int i,j;
// scanf("%d%d",&i,&j);
// int num_add=j-i%j;
// printf("%d",num_add+i);






// float mark1,mark2,mark3;

// scanf("%f%f%f",&mark1,&mark2,&mark3);
// float percent1=mark1/50;
// float percent2=mark2/50;
// float percent3=mark3/100;


// float total_marks=percent1*25+percent2*25+percent3*50;


// if(total_marks>50) printf("Passed with %f",total_marks);
// else printf("Failed");



// Calculator


// int value1,value2;
// char operator;
// printf("Enter the first number <space> operator <space> second number : ");
// scanf("%d %c %d",&value1,&operator,&value2);

// if(operator=='+') printf("%d",value1+value2);
// else if (operator=='-') printf("%d",value1-value2);
// else if (operator=='*') printf("%d",value1*value2);
// else if (operator=='/') printf("%d",value1/value2);
// else if (operator=='%') printf("%d",value1%value2);
// else if (operator=='=') value1==value2 ? printf("True") : printf("False");
// else printf("Invalid operator");



// for(int i=1;i<=10;i++){
//     printf("%d Hello\n",i);
// }



// int a,b;
// scanf("%d%d",&a,&b);
// int pairs=0;

// for (int i=1;i<=a;i++){

//     for (int j=1;j<=b;j++) {
//         if ((i+j)%2==0) pairs+=1;
//     }
// }

// printf("%d",pairs);


// char name[20];
// gets(name);
// // scanf("%s",name);
// printf("%s\n",name);

// strcpy(name,"Shakti");
// printf("%s",name);

// int num1,num2;
// num1=1;
// num2=2;
// average(1,2);

// printf("The average of %d and %d is %.2f",num1,num2,average(1,2));


// int num1;

// num1=10;

// printf("%d",num1);



    
// int n,k;
// scanf("%d",&n);
// int nums[n];




// for (int i=0;i<n;i++) scanf("%d",&nums[i]);

// scanf("%d",&k);

// int i=0;

// int m=1;

// while (m==1){
    
    
//     int sum=0;
//     if (k+i<n){
//     for (int j=i;j<i+k;j++) sum+=nums[j];
    
    
//     printf("%d ",sum);
    
//     i=k+i;
//     k=k+1;
//     }
//     else{
        
//         for (int j=i;j<n;j++) sum+=nums[j];
//         printf("%d",sum);
//         break;
//     }
    
    
// }

    
// int  numbers[4]={1,2,3,4};

// sum(4,numbers);




// Problem 1

// int n;
// printf("Enter the number of integers : ");
// scanf("%d",&n);

// int arr[n];

// for(int i=0;i<n;i++) scanf("%d",(arr+i));

// int max=arr[0];
// int index_month=0;
// for (int i=0;i<n;i++){
//     if (arr[i]>max) {
//         max=arr[i];
//         index_month=i;
//         }
// }

// arr[index_month]=arr[0];
// arr[0]=max;


// for (int i=0;i<n;i++){
//     printf("%d ",*(arr+i));
// }







// Problem 2


// int num_days_ahead;

// printf("Enter the number of days ahead : ");
// scanf("%d",&num_days_ahead);

// char weekdays[][20]={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
// char months[][20]={"January","February","March","April","May","June","July","August","September","October","November","December"};
// int monthdays[]={31,28,31,30,31,30,31,31,30,31,30,31};
// int date=0;

// char entered_day[20];

// printf("Enter the first day of the Year : ");
// scanf("%s",entered_day);

// int sum=0;
// int index_month=0;
// for (int i=0;i<12;i++){
//     index_month++;
//     if (sum+monthdays[i]<num_days_ahead){
//         sum+=monthdays[i];
//     }
//     else{

//         date=num_days_ahead-sum;
//         break;
//     }
// }



// printf("%d %s",date,months[index_month-1]);


// int index_day=0;

// for (int i=0;i<7;i++){
// if (strcmp(weekdays[i],entered_day)==0) {
// index_day=i;
// break;
// }  

// }

// int rem_days=num_days_ahead%7;


// while (rem_days>0){
//     if (index_day>6) index_day=0;
//     else index_day++;
   
//     rem_days--;
// }


// printf(" %s",weekdays[index_day]);






// Problem -3 


// int n;

// printf("Enter the order of the square matrix ");
// scanf("%d",&n);


// int matrix[n][n];

// printf("Enter the elements of the matrix rowwise : \n");

// for (int i=0;i<n;i++){
//     for (int j=0;j<n;j++) scanf("%d",&matrix[i][j]);
// }


// int upper_triangle_sum=0,lower_triangle_sum=0;


// for (int i=0;i<n-1;i++){
//     for (int j;j<n;j++){
//         if (j>i) upper_triangle_sum+=matrix[i][j];
//     }
// }

// for (int i=1;i<n;i++){
//     for (int j;j<n;j++){
//         if (j<i) lower_triangle_sum+=matrix[i][j];
//     }
// }

// int left_diagonal_sum=0,right_diagonal_sum=0;


// for (int i=0;i<n;i++){
//     left_diagonal_sum+=matrix[i][i];
// }


// for (int i=0;i<n;i++){
//     right_diagonal_sum+=matrix[i][n-1-i];
// }



// printf("The lower tringle sum : %d\n The upper triangle sum : %d\n The left diagonal sum : %d\n The right diagonal sum :  %d\n",lower_triangle_sum,upper_triangle_sum,left_diagonal_sum,right_diagonal_sum);





// Problem-4


// double salary;
// printf("Enter the salary of the employee : ");
// scanf("%lf",&salary);

// double tax_percent;

// printf("Enter the tax percent : ");

// scanf("%lf",&tax_percent);


// double gross_salary=salary*(1-(tax_percent/100));

// printf("The gross salary after tax is %.2lf",gross_salary);


    // double basic,hra,da;
    // printf("Enter your basic salary : ");
    // scanf("%lf",&basic);
    // printf("Enter HRA and DA in percentage separated with space : ");
    // scanf("%lf %lf",&hra,&da);

    // double gross_salary=basic*(1+hra/100+da/100);

    // printf("Gross salary : %lg",gross_salary);




// Problem -5 


// int n;

// printf("Enter the Number of people : ");
// scanf("%d",&n);

// for (int i=0;i<n;i++) {
//     printf("Customer No. %d Token Number : %d\n",i+1,token());
// }





// Problem -6 

// int a;
// a=(int)(2.00299);


// printf("%d",a);

// int *ptr;

// ptr=(int*) malloc(10*sizeof(int));

// *(ptr+1)=10;
// printf("\n%d",*(ptr+1));




// in malloc the elements are not intialized but you can intialize using calloc function



// Matrix Multiplication



// int num_rows_1=0, num_columns_1=0,num_rows_2=0,num_columns_2=0;

// printf("Enter the number of rows and columns separated with space for matrix 1 : ");

// scanf("%d%d",&num_rows_1,&num_columns_1);

// printf("Enter the number of rows and columns separated with space for matrix 2 : ");

// scanf("%d%d",&num_rows_2,&num_columns_2);

// if (num_columns_1==num_rows_2){

// int *matrix1,*matrix2;
// matrix1=(int*) calloc(num_rows_1*num_columns_1,sizeof(int));
// matrix2=(int*) calloc(num_rows_2*num_columns_2,sizeof(int));


// for (int i=0;i<num_rows_1*num_columns_1;i+=num_columns_1){
//     printf("Enter the row %d elements for matrix 1 separated with space : ",i/num_columns_1+1);
//     for (int j=0;j<num_columns_1;j++){
//         scanf("%d" ,(matrix1+i+j));
//     }
// }
// for (int i=0;i<num_rows_2*num_columns_2;i+=num_rows_2){
//     printf("Enter the column %d elements for matrix 2 separated with space : ",i/num_rows_2+1);
//     for (int j=0;j<num_rows_2;j++){
//         scanf("%d" ,(matrix2+i+j));
//     }
// }


// int matrix3 [num_rows_1][num_columns_2];

// int row=0;

// for (int i=0;i<num_rows_1*num_columns_1;i+=num_columns_1){
// int row_elements[num_columns_1];
// int *nums,length=0;
// nums=(int*) calloc(length,sizeof(int));
// for(int j=0;j<num_columns_1;j++){
//     *(row_elements+j)=matrix1[i+j];
// }

// for (int j=0;j<num_rows_2*num_columns_2;j+=num_rows_2){
//     int sum=0;
// for(int k=0;k<num_columns_1;k++){
// sum+=row_elements[k]*matrix2[j+k];
// }
// length+=1;
// nums=(int*) realloc(nums,length*sizeof(int));
// nums[length-1]=sum;
// }

// for (int z=0;z<length;z++){
//     matrix3[row][z]=nums[z];
// }

// row+=1;


// }


// for (int row=0;row<num_rows_1;row+=1){
//     for (int column=0;column<num_columns_2;column+=1){
//         printf("%d ",matrix3[row][column]);
//     }
//     printf("\n");
// }


// }

// else{
//     printf("Matrix multiplication not possible");
// }







// Structures

struct person
{
    int name[40];
    int age;
    char gender;

};


// struct  person person1;

// scanf("%[^\n]%*c",&person1.name);
// scanf("%d\n",&person1.age);
// scanf("%c",&person1.gender);


// printf("Your name is %s\n",person1.name);
// printf("Your age is : %d\n",person1.age);
// printf("Your gender is : %c\n",person1.gender);




// int n,*ptr;

// scanf("%d",&n);
// ptr=(int*) calloc(n,sizeof(int));

// for(int i=0;i<n;i++) scanf("%d",ptr+i);
// int mark_frequency[n];
// for (int i=0;i<n;i++){
// int num=0;
//     for(int j=0;j<n;j++){
// if (*(ptr+j)>=*(ptr+i)) num+=1;
//     }
//     mark_frequency[i]=num;
// }

// int max_mark=0,index=0;

// for (int i=0;i<n;i++){
//     if (*(ptr+i)>max_mark && mark_frequency[i]>=0.5*n){
//         max_mark=*(ptr+i);
//         index=i;
//     }
// }

// printf("%d %d\n",max_mark,index);
// printf("%d",mark_frequency[1]);
// printf("%d",mark_frequency[9]);






// 11
// 21 30 24 32 34 26 28 36 38 31 20
// 31 9


// typedef struct member {
//     char name[20];
//     char skills[2][20];
//     char gender;
// } member;





// int *nums;

// nums=(int*) calloc(3,sizeof(int));

// nums[0]=2;
// nums[1]=3;
// printf("%d \n",*(nums));



// Problem-1

// typedef struct cooordinates{
//     int x;
//     int y;
// } cooordinates;

// printf("Enter the coordinates of point 1 (x,y) separated with space : ");
// cooordinates point_1 ;

// scanf("%d%d",&point_1.x,&point_1.y);

// printf("Enter the coordinates point2 (x,y) separated with space : ");
// cooordinates point_2;
// scanf("%d%d",&point_2.x,&point_2.y);


// double distance=sqrt(pow((point_2.x-point_1.x),2)+pow((point_2.y-point_1.y),2));


// printf("The distance between (%d,%d) and (%d,%d) is %.2lf",point_1.x,point_1.y,point_2.x,point_2.y,distance);




// Problem-2


typedef struct time {
    int hours;
    int minutes;
    int seconds;
} time_details;



time_details time_1;
time_details time_2;


printf("Enter the date 1 in format (HH:MM:SS) separated with space : ");
scanf("%d %d %d",&time_1.hours,&time_1.minutes,&time_1.seconds);

printf("Enter the date 2 in format (HH:MM:SS) separated with space : ");
scanf("%d %d %d",&time_2.hours,&time_2.minutes,&time_2.seconds);



int time1_seconds=time_1.hours*60*60+time_1.minutes*60+time_1.seconds;
int time2_seconds=time_2.hours*60*60+time_2.minutes*60+time_2.seconds;


int time_diff=abs(time2_seconds-time1_seconds);

int hours_diff=time_diff/(60*60);
time_diff-=hours_diff*60*60;
int minutes_diff=time_diff/60;
time_diff-=minutes_diff*60;


printf("The time difference is %d hours %d minutes %d seconds",hours_diff,minutes_diff,time_diff);















return 0;



}


