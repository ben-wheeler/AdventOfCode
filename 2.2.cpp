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
    int forwardCount = 0;
    int depthCount = 0;
    int aim = 0;

    std::ifstream myfile("input2.txt");

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
        switch (DataArray[i][0])
        {
        case 'f':
            forwardCount += (DataArray[i][DataArray[i].size() - 1]) - '0';
            if (aim != 0)
            {
                int temp = (DataArray[i][DataArray[i].size() - 1]) - '0';
                depthCount += temp * aim;
            }
            break;
        case 'd':
            aim += (DataArray[i][DataArray[i].size() - 1]) - '0';
            break;
        case 'u':
            aim -= (DataArray[i][DataArray[i].size() - 1]) - '0';
            break;

        default:
            break;
        }
    }
    std::cout << "forward: " << forwardCount << std::endl;
    std::cout << "depth: " << depthCount << std::endl;
    std::cout << "depth x forward: " << forwardCount * depthCount << std::endl;
}