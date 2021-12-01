#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main()
{
    std::string line;
    std::vector<std::string> DataArray;
    std::vector<int> NumArrary;

    std::ifstream myfile("input1.txt");

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
    for(int i = 0; i < DataArray.size(); i++)
    {
        std::stringstream word(DataArray[i]);
        int temp = 0;
        word >> temp;
        NumArrary.push_back(temp);
    }
    int prev = NumArrary[0];
    int howMany = 0;
    for(int i = 1; i < NumArrary.size(); i++)
    {
        if(NumArrary[i] > prev ){
            howMany++;
        }
        prev = NumArrary[i];
    }
        std::cout <<howMany << std::endl;
}