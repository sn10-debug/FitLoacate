// #include <iostream>
// #include <vector>
// #include <string>

// using namespace std;

// class Sales_Person{


// public:
// string Name;
// string ID;
// double Sales;
// double bonus;
// int floor_number;

// Sales_Person(string Name="New User",int floor=1,double Sales=0):floor_number{floor}{
//     static int floor1 {},floor2{},floor3{},floor4{},floor5{};
//     this->Name=Name;
//     this->Sales=Sales;
//     int j=0;
    
//     if (floor==1) {floor1++;
//     j=floor1;
//     }
//     else if (floor==2){ floor2++;
//     j=floor2;
//     }
//     else if (floor==3) {floor3++;
//     j=floor3;
//     }
//     else if (floor==4) {floor4++;
//     j=floor4;
//     }
//     else {floor5++;
//     j=floor5;
//     }

//     this->ID="F-"+to_string(floor) +' '+to_string(j);


//     if (Sales>=300000) this->bonus=10000;
//     else if (Sales>=100000) this->bonus=5000;
//     else if (Sales>=50000) this->bonus=2000;


// // cout<<floor1<<" "<<floor2<<" "<<floor3<<" "<<floor4<<" "<<floor5<<endl;

// }

// // Copy Constructor

// Sales_Person(const Sales_Person &source):Name {source.Name} ,ID {source.ID},bonus {source.bonus},Sales {source.Sales},floor_number{source.floor_number}{}

// // Move Constructor
// Sales_Person(const Sales_Person &&source):Name {source.Name} ,ID {source.ID},bonus {source.bonus},Sales {source.Sales},floor_number{source.floor_number}{}

// ~Sales_Person(){


//     // cout<<"Object is Destroyed"<<endl;
// }


// double get_bonus(){
//     return bonus;
// }


// };


// vector <Sales_Person> Person_info{};

// void get_Max(int floor);

// int main(){



// Person_info.push_back(Sales_Person {"ABC",1,100000});
// Person_info.push_back(Sales_Person {"XYZ",1,300000});
// Person_info.push_back(Sales_Person {"LMN",3,2000});
// Person_info.push_back(Sales_Person {"PQR",5,200000});
// Person_info.push_back(Sales_Person {"TUV",5,2000000});





// for(int i=1;i<=5;i++){
//     cout<<"Person showed Maximum Sales in floor Number "<<i<<" : ";
//     get_Max(i);
// }


// int max=-20;
// string Name{"No User"};

// cout<<"Person showed Maximum Sales among All the Sales People : ";
// for(Sales_Person &c:Person_info){
    
//         if (c.Sales>max){
//             max=c.Sales;
//             Name=c.Name;
//         }
    
// }

// cout<<Name<<endl;



//     return 0;
// }


// void get_Max(int floor){
// int max=-20;
// string Name{"No Sales Person"};
// for(auto c:Person_info){
//     if (c.floor_number==floor){
//         if (c.Sales>max){
//             max=c.Sales;
//             Name=c.Name;
//         }
//     }
// }

// cout<<Name<<endl;



// }


// Shakti Santosh Nayak 21BRS1490


#include <iostream>
#include <math.h>
#include "Movies.h"
using namespace std;

// int main() {
// 	// your code goes here
	
// 	int testcases {};
// 	cin>>testcases;
	
// 	for (int l=0;l<testcases;l++){
	    
// 	    int n;
// 	    cin>>n;
// 	    int num_1=0;
// 	    int num_negative_1=0;
	    
// 	    int *arr=new int[n];
	    
// 	    for(int i=0;i<n;i++){ 
// 	        int y;
// 	        cin>>y;
// 	        arr[i]=y;
	        
// 	        if(y==1) num_1++;
// 	        else num_negative_1++;
	        
// 	       }
	       
	       
// 	       if(num_1%2==0 or num_negative_1%2==0){
// 	           if (abs(ceil(num_1/2.0)-ceil(num_negative_1/2.0))<=1) cout<<"Yes";
// 	           else cout<<"No";
// 	       }
// 	       else cout<<"No";
	       
// 	       cout<<endl;
	    
	    
// 	}
	
// 	return 0;
// }

// 1
// 5
// 1 1 1 -1 -1



class Time{
	public:
	int hour;
	int minutes;
	int seconds;

	Time(int hour_=0,int minutes_=0,int seconds_=0):hour{hour_},minutes{minutes_},seconds{seconds_}{}

	void getTime(){
		cin>>hour>>minutes>>seconds;

	}


	void findnexttime(const Time &source){

		int seconds_1=hour*3600+minutes*60+seconds;

		int seconds_2=source.hour*3600+source.minutes*60+source.seconds;

		int seconds_3=seconds_1+seconds_2;

	int hours_1=seconds_3/3600;
	seconds_3-=3600*hours_1;
	if(hours_1>=24) hours_1-=24;
	int minutes_1=seconds_3/60;

	seconds_3-=60*minutes_1;
	if(hours_1<10) cout<<0;
	cout<<hours_1<<" ";
	if (minutes_1<10) cout<<0;
	cout<<minutes_1<<" ";
	if (seconds_3<10) cout<<0;
	cout<<seconds_3<<endl;


	
		



	}


};



class Nums{

private:
Nums(int num1){
	cout<<num1;

}

	protected:
	int y;
	public:
	int x;

	Nums():y{20} {
	}

	friend int main();
	// This will make all the private and protected members public in main function

};


int main(){


	// Movies Movie_list_1{};

	// cout<<Movie_list_1.add_Movie("Sigma")<<endl;

	// Movie_list_1.disp_Movies();

	// Movie_list_1.add_Movie("ABC","PG");
	// Movie_list_1.add_Movie("LMN","G");

	// Movie_list_1.disp_Movies();
	

// Deep Copy

	// Movies Movie_list_2 {Movie_list_1};

	// Movie_list_2.add_Movie("GHI","JSJS");
	// Movie_list_2.disp_Movies();



// int &a;

int testcases{0};

// cout<<"Enter the Number of testcases : ";
// cin>>testcases;



for (int l=0;l<testcases;l++){

Time Time_1{0,0,1};

Time Time_2;
cout<<"Enter the Time in HH:MM:SS format after which the time has to be found separated with space : ";
Time_2.getTime();

cout<<"Time in format HH:MM:SS is : ";

Time_1.findnexttime(Time_2);


}



// union Options{
// int num1;
// char num2;
// int num3;
// };

// Options Option1 {};
// Option1.num1=20;

// cout<<Option1.num1<<endl;

// cout<<Option1.num2<<endl;

// cout<<Option1.num3<<endl;

// Option1.num2=20;

// cout<<Option1.num1<<endl;

Nums num1 {};

num1.x=20;
num1.y=30;


cout<<num1.y<<endl;

// Nums num2{10};














	return 0;
}
