#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void print(vector<vector<int> > input)
{
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 0; j < input.size(); j++)
        {
            if (input[j][i] == 0)
            {
                cout << ".";
            }
            else
            {
                cout << input[j][i];
            }
            cout << " ";
        }
        cout << endl;
    }
}

int main()
{
    string line;

    vector<int> input;
    getline(cin, line);
    replace(line.begin(), line.end(), ',', ' ');
    istringstream first_line(line);
    string first_a;
    while (first_line >> first_a)
    {
        if (!first_a.empty())
        {
            input.push_back(stoi(first_a));
        }
    }

    sort(input.begin(), input.end());

    // print(input);
    // cout << endl;
    cout << input[input.size()/2] << " ";
    int fuelCount = 0;

    for(int i = 0; i < input.size(); i++){

    }
}