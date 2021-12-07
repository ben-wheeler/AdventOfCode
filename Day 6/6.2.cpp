
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
    long zero = 0;
    long one = 0;
    long two = 0;
    long three = 0;
    long four = 0;
    long five = 0;
    long six = 0;
    long seven = 0;
    long eight = 0;

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
            std::cout << "SDSADA";
            break;
        }
    }
    for (size_t i = 0; i < 256; i++)
    {
        long temp = zero;
        zero = one;
        one = two;
        two = three;
        three = four;
        four = five;
        five = six;
        six = seven + temp;
        seven = eight;
        eight = temp;
    }
    std::cout << zero + one + two + three + four + five + six + seven + eight << " -- Worked" << std::endl;
}