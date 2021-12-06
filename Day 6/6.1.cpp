#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void print(vector<int> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        cout << input[i] << ",";
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
    cout << "Inital State: ";
    print(input);
    cout << endl;
    int currentSize = 5;
    for(int i = 0; i < 11; i++){
        for(int j = 0; j < input.size(); j++){
            input[j]--;
            if(input[j] == -1){
                input[j] = 6;
                input.push_back(9);
            }
        }
        cout << "After " << i+1 << " Days: ";
        print(input);
        cout << endl;
        currentSize = input.size();
    }

    cout << input.size();
}