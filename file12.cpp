#include <iostream>
#include <string>
#include <list>
#include <iterator>
#include <algorithm>

using namespace std;

class Song
{

public:
    string Name;
    string Author;
    double Rating;

    Song(string n = "Unknown Song", string a = "XYZ", double r = 0) : Name{n}, Author{a}, Rating{r}
    {
    }

    bool operator==(const Song &rhs)
    {
        return (Name == rhs.Name and Author == rhs.Author and Rating == rhs.Rating);
    }
};

ostream &operator<<(ostream &os, const Song music)
{

    os << "Song Name : " << music.Name << endl;
    os << "Author : " << music.Author << endl;
    return os;
}

void disp_songs(list<Song> &source)
{
    for (auto c : source)
    {
        cout << c;
    }
}

int main()
{

    list<Song> Song_list{{"Song 1", "ABC", 4}, {"Song 2", "DEF", 4}, {"Song 3", "GHI", 4}};

    char status = 'P';
    auto current_song = Song_list.begin();

    cout << "List of Songs \n";

    disp_songs(Song_list);

    while (status != 'Q')
    {
        char option{};
        cout << "Current song : " << (*current_song).Name << endl;
        cout << "This are the options Available and Select any one of them \n";
        cout << "P -> Play\nS -> Stop \nN -> Next\nX -> Previous\nQ -> Quit\nI -> Insert a song immediately after this song\nL -> Insert the song to the Queue\n";
        cout << "Select any of the option : ";
        cin >> option;
        option = toupper(option);

        if (option == status and (status == 'P' or status == 'S'))
        {
            if (status == 'P')
            {
                cout << "The Song is already in Play Mode\n";
            }
            else
            {
                cout << "The Song is already in Pause Mode\n";
            }

            continue;
        }

        if (option == 'P' or option == 'S')
        {
            if (option == 'P')
                cout << (*current_song).Name << " is playing now\n";
            else
                cout << (*current_song).Name << " is paused now\n";

            status = option;
        }
        else if (option == 'N')
        {
            current_song++;
            if (current_song == Song_list.end())
                current_song = Song_list.begin();
            status = 'P';
        }
        else if (option == 'X')
        {
            if (current_song == Song_list.begin())
            {
                current_song = Song_list.end();
            }
            current_song--;
            status = 'P';
        }
        else if (option == 'I' or option == 'L')
        {
            string Name{};
            string Author{};
            double rate{};

            cout << "Enter the Name of the song :";
            getline(cin, Name);
            cout << "Enter the Author of the song :";
            getline(cin, Author);
            cout << "Enter the Rating of the song : ";
            cin >> rate;

            if (option == 'I')
            {
                auto itr = current_song;
                itr++;
                Song_list.insert(itr, Song{Name, Author, rate});
            }
            else
            {
                Song_list.emplace_back(Name, Author, rate);
            }
        }
        else if (option == 'Q')
            status = option;
        else
        {
            cout << "Invalid Option Entered\n";
        }
    }

    return 0;
}