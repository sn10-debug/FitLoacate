#include <iostream>
#include <string>
#include <vector>
#include "Movie.h"

using namespace std;


#ifndef _MOVIES_H_
#define _MOVIES_H_

class Movies{


private:

public:
vector <Movie> Movie_List;

string add_Movie(string Name="New Movie",string Rating="R"){


        bool present=0;
            for (auto &c:Movie_List){
                if (c.get_Name()==Name) {present=1;
                break;
                }
            }

        if(!present){
            Movie_List.push_back(Movie {Name,Rating});
            return "Movie Added Successfully";
            }

        else {
            return "Movie Already Exists";
        }


}


void Watch_Movie(string Movie_Name){
    bool present=0;

    for (auto &c:Movie_List){
        if (c.get_Name()==Movie_Name) {
        c.watch();
        present=1;
        break;

        }
    }

    if(present) cout<<"Enjoy Watching "<<Movie_Name<<endl;
    else cout<<"The Entered Movie "<<Movie_Name<<" is not Present in the Movies list";
    

}


Movies ():Movie_List {}{}

Movies(const Movies &source):Movie_List{source.Movie_List}{}


void disp_Movies(){
    for(auto &c:Movie_List){
        cout<<"The Name of the movie is "<<c.get_Name()<<endl;
        cout<<"The Rating of the movie is "<<c.get_Rating()<<endl;

        cout<<"\n\n";

    }
}

~Movies(){
    // cout<<"Movies List is Destroyed"<<endl;
}

};

#endif