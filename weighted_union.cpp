#include <iostream>

using namespace std;

int remove_parent(int arr[], int index)
{

    if (arr[index] >= 0)
    {
        return remove_parent(arr, arr[index]);
    }
    else
    {
        return index;
    }
}

int main()
{
    int num_vertices{}, num_edges{};
    cout << "Enter the number of Vertices : ";
    cin >> num_vertices;

    int arr1[num_vertices]{};

    for (int i = 0; i < num_vertices; i++)
        arr1[i] = -1;

    cout << "Enter the number of edges : ";
    cin >> num_edges;

    int arr2[num_edges][2];

    for (int i = 0; i < num_edges; i++)
    {

        cout << "Enter the vertices for the edge-" << i + 1 << " separated with space : ";
        cin >> arr2[i][0] >> arr2[i][1];
        arr2[i][0] -= 1;
        arr2[i][1] -= 1;
    }

    int count = 0;

    int num_cycles = 0;

    while (count != num_edges)
    {
        int index1 = arr2[count][0];
        int index2 = arr2[count][1];
        int parent1 = remove_parent(arr1, index1);
        int parent2 = remove_parent(arr1, index2);

        if (parent1 == parent2)
            num_cycles++;
        else
        {
            if (abs(arr1[parent1]) >= abs(arr1[parent2]))
            {
                arr1[parent1] = (arr1[parent1] + arr1[parent2]);
                arr1[parent2] = parent1;
            }
            else
            {
                arr1[parent2] = (arr1[parent1] + arr1[parent2]);
                arr1[parent1] = parent2;
            }
        }

        count++;
    }

    cout << "[ ";
    for (auto &c : arr1)
        cout << c << " ";
    cout << " ]" << endl;
    cout << num_cycles << endl;

    return 0;
}
