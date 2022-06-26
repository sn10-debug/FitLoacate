#include <iostream>
#include <vector>
#include <string>

using namespace std;
#ifndef _MOVIE_H
#define _MOVIE_H

class Movie{

private:
    string Name;
    string Rating;
    int watched_times;

public:

    Movie(string name="New Movie" ,string rating="R"):Name{name},watched_times{0}{

        vector <string> Ratings {"G","PG","PG-13","R"};
        bool present=0;
        for (auto c:Ratings){
            if (c==rating){ present=1;
            break;
            }
        }

        if (!present) Rating="R";
        else Rating=rating;


        
    }
    
    string get_Name() const{
        return Name;
    }
    string get_Rating() const{
        return Rating;
    }
    int get_watch_time() const{
        return watched_times;
    }

    


    void watch(){
        watched_times++;
    }

    Movie(const Movie &source):Name{source.get_Name()},Rating{source.get_Rating()},watched_times{source.get_watch_time()}{}
    // Movie(Movie &&source):Name{source.Name},Rating{source.Rating},watched_times{source.watched_times}{}

    ~Movie(){
        // cout<<"Movie Destroyed"<<endl;
    }



};


#endif