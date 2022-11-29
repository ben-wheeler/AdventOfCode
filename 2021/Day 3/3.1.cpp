#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main()
{
    std::string line;
    std::vector<std::string> DataArray;
    std::vector<int> gamma;
    std::vector<int> epsilon;
    int zCount, oCount;

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

    for (int i = 0; i < DataArray[0].size(); i++)
    {
        zCount = 0;
        oCount = 0;
        for (int j = 0; j < DataArray.size(); j++)
        {
            std::cout << DataArray.size() << std::endl;

            if (DataArray[j][i] == '0')
            {
                zCount++;
            }
            else if (DataArray[j][i] == '1')
            {
                oCount++;
            }
        }
                std::cout << zCount << " 0 | 1 " << oCount << std::endl;

        if (zCount > oCount)
        {
            gamma.push_back(0);
            epsilon.push_back(1);
        }
        else
        {
            gamma.push_back(1);
            epsilon.push_back(0);
        }
    }
    std::cout << "Gamma: ";
    for (int i = 0; i < gamma.size(); i++)
    {
        std::cout << gamma.at(i);
    }
    std::cout << std::endl
              << "Ep: ";
    for (int i = 0; i < epsilon.size(); i++)
    {
        std::cout << epsilon.at(i);
    }
}
