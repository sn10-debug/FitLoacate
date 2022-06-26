#include <iostream>
#include <string>
#include <math.h>



using namespace std;


class Number{
    public:
    double num;
    Number(double num_=0):num{num_}{}

    Number(const Number &source):num{source.num}{}

    Number(const Number &&source):num{source.num}{}


    Number operator=(const Number &source){
        return Number{source.num};
    }

    
    Number operator++(int){
        num++;
        return Number{num-1};

    }

    Number operator++(){
        num++;
        return Number{num};
    }

    Number operator+(const Number &source){
        return Number{num+source.num};
    }

    Number operator-(const Number &source){
        return Number{num-source.num};
    }

    Number operator*(const Number &source){
        return Number{num*source.num};
    }


    ~Number(){}



};



Number operator+(int lhs,const Number &rhs){
    return Number{lhs+rhs.num};
}

Number operator+(const Number &lhs,int rhs){
    return Number{rhs+lhs.num};
}


Number operator-(int lhs,const Number &rhs){
    return Number{lhs-rhs.num};
}

Number operator-(const Number &lhs,int rhs){
    return Number{lhs.num-rhs};
}


Number operator*(int lhs,const Number &rhs){
    return Number{lhs*rhs.num};
}

Number operator*(const Number &lhs,int rhs){
    return Number{rhs*lhs.num};
}

Number operator/(int lhs,const Number &rhs){
    return Number{(float)lhs/rhs.num};

}

Number operator/(const Number &lhs,int rhs){
    return Number{(float)lhs.num/rhs};
    
}






ostream & operator<<(ostream &os,const Number &rhs){

    os<<rhs.num;
    return os;


}





class Word{

    public:
    string letters;

    Word(string initial=""):letters{initial}{
        cout<<initial<<endl;


        }


    int length(){
        return letters.size();
    }

    Word operator+(const Word &source){
        return Word{letters+source.letters};
    }

    // Word& operator*(int num){
    //     Word word_1 {letters};
    //     for (int i=1;i<num;i++){
    //         word_1.letters+=letters;
    //     }
    //     return word_1;
    // }


    bool startswith(string characters){
        bool equal=1;
        for (int i=0;i<characters.size();i++){
            if(letters.at(i)!=characters.at(i)){
                equal=0;
                break;
            } 
        }

        return equal;

    }

    bool endswith(string characters){
        bool equal=1;
        for (int i=letters.size()-characters.size()-1;i<letters.size();i++){
            if(letters.at(i)!=characters.at(i-(letters.size()-characters.size()-1))){
                equal=0;
                break;
            } 
        }

        return equal;

    }




};



int main(){


    Number num1{10};

    cout<<num1<<endl;

    num1++;
    ++num1;

    cout<<num1<<endl;

    cout<<num1++<<endl;

    cout<<++num1<<endl;


    Number num2 {10};
    Number num3 {10};
    cout<<num2+num3<<endl;


    cout<<num2-num3<<endl;


    Word word_1 {"Shakti"};

    cout<<boolalpha;

    cout<<word_1.letters<<endl;
    cout<<word_1.startswith("Sha")<<endl;








    


    
    return 0;
}