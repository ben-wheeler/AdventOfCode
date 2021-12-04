#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct board {
    vector<int> numbers;
    vector<bool> found;

}




int main()
{
    std::string line;
    std::vector<std::string> DataArray;
    std::vector<int> NumArrary;

    std::ifstream myfile("input.txt");

    if (!myfile) //Always test the file open.
    {
        std::cout << "Error opening output file" << std::endl;
        system("pause");
        return -1;
    }
    while (std::getline(myfile, line))
    {
        DataArray.push_back(line);
    }
    std::vector<int> callOutNumbers;

    std::stringstream ss(DataArray[0]);

    for (int i; ss >> i;)
    {
        callOutNumbers.push_back(i);
        if (ss.peek() == ',')
            ss.ignore();
    }

    vector<vector<string> > boards;
    vector<string> board;
    string temp;
    for (int i = 2; i <= DataArray.size(); i++)
    {
        if (DataArray[i] == "")
        {
            boards.push_back(board);
            board.clear();
        }
        else
        {
            string temp = DataArray[i];
            board.push_back(temp);
        }
    }


    for (int i = 0; i < callOutNumbers.size(); i++)
    {
        string currentNum = to_string(callOutNumbers[i]);
        for (int i = 0; i < boards.size(); i++)
        {
            for (int j = 0; j < boards[0].size(); j++)
            {
                if (boards[i][j].find(currentNum) != string::npos)
                {
                    int start_position_to_erase = boards[i][j].find(currentNum);
                    int number_of_symbols = currentNum.size();
                    boards[i][j].erase(start_position_to_erase, number_of_symbols);
                }
                if(boards[i][j] == "    "){
                        cout << "lol";
                }
            }
        }
    }

        for (int i = 0; i < boards.size(); i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << boards[i][j] << endl;
        }
    }

    cout << boards[0].size() << endl;
}