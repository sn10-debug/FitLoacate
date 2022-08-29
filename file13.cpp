#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

template <class T>
void disp_container(T container)
{
    cout << "[ ";
    for (auto itr = container.begin(); itr != container.end(); itr++)
    {
        cout << *itr << " ";
    }
    cout << "]" << endl;
}

vector<int> &heap_insert(vector<int> &nums, int val)
{
    nums.push_back(val);
    int index = nums.size();

    while (index > 1)
    {
        int parent = index / 2;
        if (nums.at(parent - 1) < nums.at(index - 1))
        {
            int temp = nums.at(index - 1);
            nums.at(index - 1) = nums.at(parent - 1);
            nums.at(parent - 1) = temp;
            index = parent;
            continue;
        }
        break;
    }

    return nums;
}

vector<int> create_heap(vector<int> nums)

{
    vector<int> num2{};
    for (auto c : nums)
    {
        heap_insert(num2, c);
    }

    return num2;
}

vector<int> &heap_delete(vector<int> &nums)
{

    int temp = nums.at(0);
    nums.at(0) = nums.at(nums.size() - 1);
    nums.at(nums.size() - 1) = temp;

    nums.pop_back();

    nums = create_heap(nums);

    // int index = 1;

    // while (index < nums.size())
    // {

    //     int child_1 = 2 * index;
    //     int child_2 = 2 * index + 1;

    //     if (child_1 - 1 < nums.size() and  nums.at(child_1 - 1) > nums.at(index - 1))
    //     {
    //         int temp = nums.at(index - 1);
    //         nums.at(index - 1) = nums.at(child_1 - 1);
    //         nums.at(child_1 - 1) = temp;

    //         index = child_1;

    //         continue;
    //     }

    //     if (child_2 - 1 < nums.size() and nums.at(child_2 - 1) > nums.at(index - 1))
    //     {
    //         int temp = nums.at(index - 1);
    //         nums.at(index - 1) = nums.at(child_2 - 1);
    //         nums.at(child_2 - 1) = temp;

    //         index = child_2;

    //         continue;
    //     }

    //     break;
    // }

    return nums;
}

vector<int> heap_sort(vector<int> nums)
{
    vector<int> num2;
    nums = create_heap(nums);

    while (!nums.empty())
    {
        num2.push_back(nums.at(0));
        heap_delete(nums);
    }

    reverse(num2.begin(), num2.end());

    return num2;
}

void disp_map(map<string, int> &m)
{
    cout << "[ ";
    for (auto c : m)
    {
        cout << c.first << " : " << c.second << " , ";
    }
    cout << " ]" << endl;
}

void disp_map(map<string, set<int>> &m)
{

    cout << "[ ";
    for (auto c : m)
    {
        cout << c.first << " : "
             << "[ ";

        for (auto d : c.second)
        {
            cout << d << " , ";
        }
        cout << " ] , " << endl;
    }
    cout << " ]" << endl;
}

template <class T>
void bubble_sort(T *arr, int size)
{

    int turns = 0;
    for (int i = 0; i < size - 1; i++)
    {
        bool got = 1;
        for (int j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                T temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
                if (got)
                    got = 0;
            }
            turns++;
        }

        if (got)
            break;
    }

    cout << "Number of turns : " << turns << endl;
}

template <class T>
void insert_sort(T *arr, int n)
{

    for (int i = 1; i < n; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                T temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
                continue;
            }
            break;
        }
    }
}

template <class T>
void select_sort(T *arr, int n)
{

    for (int i = 0; i < n - 1; i++)
    {

        int min = arr[i];
        int index = i;

        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < min)
            {
                min = arr[j];
                index = j;
            }
        }
        int temp = arr[i];
        arr[i] = min;
        arr[index] = temp;
    }
}

template <class T>
void disp_arr(T *arr, int n)
{
    cout << "[ ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "]" << endl;
}

template <class T>

vector<T> merge(vector<T> vec1, vector<T> vec2)
{
    int size1 = vec1.size();
    int size2 = vec2.size();
    vector<T> vec3;

    int i = 0, j = 0;

    while (!(i == size1 or j == size2))
    {
        if (vec1.at(i) < vec2.at(j))
        {
            vec3.push_back(vec1.at(i));
            i++;
        }
        else
        {
            vec3.push_back(vec2.at(j));
            j++;
        }
    }

    if (i != size1)
    {
        for (int k = i; k < size1; k++)
        {
            vec3.push_back(vec1.at(k));
        }
    }

    if (j != size2)
    {

        for (int k = j; k < size2; k++)
        {
            vec3.push_back(vec2.at(k));
        }
    }

    return vec3;
}

template <class T>
vector<T> merge_sort(vector<T> vec)
{

    if (vec.size() > 1)
    {
        int mid = (1 + vec.size()) / 2;

        vector<T> vec1{}, vec2{}, vec3{}, vec4{};
        for (int i = 0; i < mid; i++)
        {
            vec1.push_back(vec.at(i));
        }
        for (int i = mid; i < vec.size(); i++)
        {
            vec2.push_back(vec.at(i));
        }

        vec3 = merge_sort(vec1);
        vec4 = merge_sort(vec2);

        return merge(vec3, vec4);
    }

    return vec;
}

int main()
{

    // Heap Sort with the help of max heap

    vector<int> nums_1{50, 30, 20, 15, 10, 8, 12};

    disp_container(nums_1);

    // heap_insert(nums_1, 60);
    // disp_container(nums_1);
    // heap_delete(nums_1);

    // disp_container(nums_1);
    nums_1 = heap_sort(nums_1);

    disp_container(nums_1);

    vector<int> nums_2{10, 20, 15, 30, 40};

    // disp_container(nums_2);
    // nums_2 = create_heap(nums_2);
    // disp_container(nums_2);

    // heap_delete(nums_2);

    // disp_container(nums_2);

    nums_2 = heap_sort(nums_2);

    disp_container(nums_2);

    // Bubble sort

    int arr1[]{20, 1, 4, 2, 6};
    int arr2[]{1, 2, 3, 4, 5, 6};

    int arr3[]{100, 90, 80, 70, 60};

    int arr4[]{5, 4, 10, 1, 6, 2};

    // bubble_sort(arr1, 5);
    insert_sort(arr3, 5);
    bubble_sort(arr2, 6);
    bubble_sort(arr4, 6);

    cout << "[ ";
    for (auto c : arr4)
    {
        cout << c << " ";
    }
    cout << "]" << endl;

    //--------------------
    //--------------------
    //--------------------
    //--------------------
    //--------------------

    // Insertion Sort Algorithm

    // insert_sort(arr3, 5);

    // Selection Sort Algorithm

    int arr5[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    disp_arr(arr5, 10);
    select_sort(arr5, 10);
    disp_arr(arr5, 10);

    // Merge Sort

    vector<int> nums_3{1, 2, 5, 6, 8, 9, 13, 14};
    vector<int> nums_4{3, 4, 7, 10, 11, 12};

    nums_4 = merge(nums_3, nums_4);

    vector<int> nums_5{10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    //

    disp_container(nums_4);

    disp_container(nums_5);

    nums_5 = merge_sort(nums_5);

    disp_container(nums_5);

    return 0;
}

// Course Challenge

// ofstream file_1{"challenge_text.txt", ios::trunc};

// string lines{
//     "Lorem ipsum , dolor sit amet consectetur adipisicing elit . Accusamus , odio excepturi in totam porro aut repellat labore iste solutqua Officiis quibusdam odit omnis similique qui reiciendis voluptatem voluptatibus consequuntur ? \n"};

// if (file_1)
// {

//     for (int i = 0; i < 100; i++)
//     {

//         file_1 << lines;
//     }

//     file_1.close();
// }

// ifstream file_2{"challenge_text.txt"};
// ifstream file_3{"challenge_text.txt"};

// map<string, int> word_count{};

// map<string, set<int>> word_line_data{};

// if (file_2)
// {
//     string word;
//     while (file_2 >> word)
//     {
//         if (word.size() < 2)
//             continue;

//         if (word_count.count(word) < 1)
//         {
//             word_count[word] = 1;
//         }
//         else
//         {
//             word_count[word] += 1;
//         }
//     }
// }

// int line_count = 1;
// if (file_3)
// {
//     string line;
//     while (getline(file_3, line))
//     {
//         istringstream string_1{line};
//         string word;
//         while (string_1 >> word)
//         {
//             if (word.size() < 2)
//                 continue;
//             if (word_line_data.count(word) < 1)
//             {
//                 word_line_data[word] = {line_count};
//             }
//             else
//             {
//                 word_line_data[word].insert(line_count);
//             }
//         }
//         line_count++;
//     }
// }

// cout << "Word Count in the challenge_text file " << endl;
// disp_map(word_count);
// cout << endl;
// cout << "Lines in which these words occur : " << endl;

// disp_map(word_line_data);

// cout << "Hello World" << endl;
