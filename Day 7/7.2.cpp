#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

void print(vector<int> input)
{
    for (int i = 0; i < input.size(); i++)
    {
        cout << input[i] << ",";
    }
}

int calc(int input){
    int temp = input;
    for(int i = 0; i < input; i++){
        temp += i;
    }
    // cout << temp << "temp";
    return temp;
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
    long fuelCount = 0;

    double average = 0;

for(int i = 0; i < input.size(); i++){
    average += input[i];
}
    average = round(average/input.size());
    int avg = average - 1;
    cout << avg << " ";

    for(int i = 0; i < input.size(); i++){
        if(input[i] > avg){
            fuelCount += calc(abs(input[i] - avg));
        }
        else if(input[i] < avg){
            fuelCount += calc(abs(avg - input[i]));
        }
    }
    cout << fuelCount;

    cout << endl;
    // calc(11);
}