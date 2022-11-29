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

vector<vector<int> > updateConstantY(int constantY, int x1Val, int x2Val, vector<vector<int> > input)
{
    if (x1Val > x2Val)
    {
        for (int i = x1Val; i >= x2Val; i--)
        {
            input[i][constantY]++;
        }
    }
    else
    {
        for (int i = x1Val; i <= x2Val; i++)
        {
            input[i][constantY]++;
        }
    }
    return input;
}

vector<vector<int> > updateConstantX(int constantX, int y1Val, int y2Val, vector<vector<int> > input)
{
     if (y1Val > y2Val)
    {
        for (int i = y1Val; i >= y2Val; i--)
        {
            input[constantX][i]++;
        }
    }
    else
    {
        for (int i = y1Val; i <= y2Val; i++)
        {
            input[constantX][i]++;
        }
    }
    // print(input);
    return input;
}

int main()
{
    string line;

    vector<int> temp;
    vector<vector<int> > input;
    while (line != "~")
    {
        getline(cin, line);
        if (line == "~")
        {
            continue;
        }
        replace(line.begin(), line.end(), ',', ' ');
        replace(line.begin(), line.end(), '-', ' ');
        replace(line.begin(), line.end(), '>', ' ');
        istringstream first_line(line);
        string first_a;
        while (first_line >> first_a)
        {
            if (!first_a.empty())
            {
                temp.push_back(stoi(first_a));
            }
        }
        input.push_back(temp);
        temp.clear();
    }
    for (int i = 0; i < input.size(); i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << input[i][j] << ", ";
        }
        cout << endl;
    }

    vector<vector<int> > diagram;

    temp.clear();

    for (int i = 0; i < 1000; i++)
    {
        for (int j = 0; j < 1000; j++)
        {
            temp.push_back(0);
        }
        diagram.push_back(temp);
        temp.clear();
    }

    // diagram = updateConstantX(7, 0, 4, diagram);

    for (int i = 0; i < input.size(); i++)
    {
        if (input[i][0] == input[i][2]) // x1 = x2
        {
            diagram = updateConstantX(input[i][0],input[i][1],input[i][3],diagram);
        }
        if (input[i][1] == input[i][3]) // y1 = y2
        {
            diagram = updateConstantY(input[i][1],input[i][0],input[i][2],diagram);
        }
    }

    int maxCount = 0;
    for (int i = 0; i < diagram.size(); i++)
    {
        for (int j = 0; j < diagram.size(); j++)
        {
            if (diagram[j][i] > 1)
            {
                maxCount++;
            }
    }
    }

    // print(diagram);
    cout << maxCount;

    // x1[0] y1[1] x2[2] y2[3]
}