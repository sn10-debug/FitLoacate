#include <iostream>
#include <string>

using namespace std;


class Distance{
    public:
    double feets;
    double inches;

    Distance(double x=0,double y=0):feets{x},inches{y}{

    }




};

class DistanceSign:public Distance{
    public:
    char sign;
    DistanceSign(double x=0,double y=0,char sign_='+'):Distance(x,y),sign{sign_}{
        if(sign=='-'){
            // feets=-feets;
            inches=-inches;
        }

    }


    DistanceSign & operator+(const DistanceSign &rhs){
        double t_feets,t_inches;
        t_feets=abs(rhs.feets+feets);
        t_inches=double(abs(int(rhs.inches+inches)%12));
        t_feets+=double(abs(int(rhs.inches+inches)/12));


         DistanceSign *d1=new DistanceSign{t_feets,t_inches};
       
        return *d1;
    }

    DistanceSign & operator-(const DistanceSign &rhs){
        double t_feets,t_inches;
        t_feets=abs(rhs.feets-feets);
        t_inches=double(abs(int(rhs.inches-inches)%12));
        t_feets+=double(abs(int(rhs.inches-inches)/12));

        DistanceSign *d1=new DistanceSign{t_feets,t_inches};
       
        return *d1;

    }

    



};


int main(){


    string d1,d2;

    cout<<"Enter the Number-1 : ";
    cin>>d1;

    cout<<"Enter the Number-2 : ";
    cin>>d2;    
    

    string feet1,inches1,feet2,inches2;
    bool go_1=0,go_2=0;

    for (int i=0;i<d1.size();i++){
        if (d1.at(i)!='.'){
        if(!go_1) feet1+=d1.at(i);
        else inches1+=d1.at(i);
        }
        else go_1=1;


    }

    for (int i=0;i<d2.size();i++){
        if (d2.at(i)!='.'){
        if(!go_2) feet2+=d2.at(i);
        else inches2+=d2.at(i);
        }
        else go_2=1;


    }

    char sign_1='+',sign_2='+';


    double feet1_num,inches1_num,feet2_num,inches2_num;



    char feet1_arr[100] {};

    for (int i=0;i<feet1.size();i++){
        feet1_arr[i]=feet1.at(i);
        
    }
    char inches1_arr[100] {};

    for (int i=0;i<inches1.size();i++){
        inches1_arr[i]=inches1.at(i);
        
    }
    

    char feet2_arr[100] {};

    for (int i=0;i<feet2.size();i++){
        feet2_arr[i]=feet2.at(i);
        
    }
    char inches2_arr[100] {};

    for (int i=0;i<inches2.size();i++){
        inches2_arr[i]=inches2.at(i);
        
    }

    sscanf(feet1_arr,"%lf",&feet1_num);
    sscanf(inches1_arr,"%lf",&inches1_num);

    sscanf(feet2_arr,"%lf",&feet2_num);
    sscanf(inches2_arr,"%lf",&inches2_num);
   
    if(d1.at(0)=='-'){
        sign_1='-';
       
     }
    sscanf(feet2_arr,"%lf",&feet2_num);
    sscanf(inches2_arr,"%lf",&inches2_num);

    if(d2.at(0)=='-'){
        sign_2='-';
       
     }

     DistanceSign d_1{feet1_num,inches1_num,sign_1};
     DistanceSign d_2{feet2_num,inches2_num,sign_2};

     DistanceSign d3{d_1+d_2};
     DistanceSign d4{d_1-d_2};
    cout<<"Addition : "<<d3.feets<<" "<<d3.inches<<endl;

     cout<<"Substraction : "<<d4.feets<<" "<<d4.inches<<endl;





 





    return 0;
}