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
    for (int i = 0; i < DataArray.size(); i++)
    {
        
    }
}