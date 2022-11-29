#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> oxyCal(int zeros, int ones, int colNum, std::vector<std::string> inVec)
{
    if (inVec.size() == 1)
    {
        return inVec;
    }
    else
    {
        std::vector<std::string> returnVec;
        if (zeros > ones)
        {
            for (int row = 0; row < inVec.size(); row++)
            {
                if (inVec[row][colNum] == '0')
                {
                    returnVec.push_back(inVec[row]);
                }
            }
        }
        else
        {
            for (int row = 0; row < inVec.size(); row++)
            {
                if (inVec[row][colNum] == '1')
                {
                    returnVec.push_back(inVec[row]);
                }
            }
        }
        return returnVec;
    }
}

std::vector<std::string> coCal(int zeros, int ones, int colNum, std::vector<std::string> inVec)
{
    if (inVec.size() == 1)
    {
        return inVec;
    }
    else
    {
        std::vector<std::string> returnVec;
        if (zeros > ones)
        {
            for (int row = 0; row < inVec.size(); row++)
            {
                if (inVec[row][colNum] == '1')
                {
                    returnVec.push_back(inVec[row]);
                }
            }
        }
        else
        {
            for (int row = 0; row < inVec.size(); row++)
            {
                if (inVec[row][colNum] == '0')
                {
                    returnVec.push_back(inVec[row]);
                }
            }
        }
        return returnVec;
    }
}

int main()
{
    std::string line;
    std::vector<std::string> DataArray;
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
    std::vector<std::string> ox = DataArray;
    std::vector<std::string> co = DataArray;

    for (int i = 0; i < DataArray[0].size(); i++)
    {
        zCount = 0;
        oCount = 0;
        for (int j = 0; j < ox.size(); j++)
        {
            if (ox[j][i] == '0')
            {
                zCount++;
            }
            else if (ox[j][i] == '1')
            {
                oCount++;
            }
        }
        std::vector<std::string> tempOX = ox;
        ox = oxyCal(zCount, oCount, i, tempOX);
        zCount = 0;
        oCount = 0;
        for (int j = 0; j < co.size(); j++)
        {
            if (co[j][i] == '0')
            {
                zCount++;
            }
            else if (co[j][i] == '1')
            {
                oCount++;
            }
        }
        std::vector<std::string> tempCO = co;
        co = coCal(zCount, oCount, i, tempCO);
    }
    std::cout << "ox: ";
    for (int i = 0; i < ox.size(); i++)
    {
        std::cout << ox.at(i);
    }
    std::cout << std::endl
              << "co2: ";
    for (int i = 0; i < co.size(); i++)
    {
        std::cout << co.at(i);
    }
}
