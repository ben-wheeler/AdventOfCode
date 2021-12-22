#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct 
 display{
    string wires;
    string output;
    display(string one, string two){
        wires = one;
        output = two;
    }
};


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

    getline(cin, line);
    replace(line.begin(), line.end(), ',', ' ');
    istringstream first_line(line);
    string first_a;

    string delimiter = "|";
    vector<display> input;

    while (first_line >> first_a)
    {
        display temp((first_a.substr(0, first_a.find(delimiter))),(first_a.substr(first_a.find(delimiter),0)));
       
    }

    sort(input.begin(), input.end());

    // print(input);
    // cout << endl;
    // cout << input[input.size()/2] << " ";
    // int fuelCount = 0;

    for(int i = 0; i < input.size(); i++){

    }
}