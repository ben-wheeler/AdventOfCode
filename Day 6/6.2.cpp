
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
    int zero = 0;
    int one = 0;
    int two = 0;
    int three = 0;
    int four = 0;
    int five = 0;
    int six = 0;
    int seven = 0;
    int eight = 0;

    for (int i = 0; i < input.size(); i++)
    {
        switch (input[i])
        {
        case 0:
            zero++;
            break;
        case 1:
            one++;
            break;
        case 2:
            two++;
            break;
        case 3:
            three++;
            break;
        case 4:
            four++;
            break;
        case 5:
            five++;
            break;
        case 6:
            six++;
            break;
        case 7:
            seven++;
            break;
        case 8:
            eight++;
            break;
        default:
            break;
        }
    }
    cout << one << endl;
    cout << two << endl;
    cout << three << endl;
    cout << four << endl;
    int counter;
    for (int i = 0; i < 80; i++)
    {
            switch (i)
            {
            case 1:
                one = one * 2;
                break;
            case 2:
                two = two * 2;
                break;
            case 3:
                three = three * 2;
                break;
            case 4:
                four = four * 2;
                break;
            case 5:
                five = five * 2;
                break;
            case 6:
                six = six * 2;
                break;
            case 7:
                seven = seven * 2;
                break;
            case 8:
                eight = eight * 2;
                break;
            default:
                break;
        }
    }
    cout << one + two + three + four + five + six + seven + eight << endl;
}