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
    for (int i = 0; i < DataArray.size(); i++)
    {
        std::stringstream word(DataArray[i]);
        int temp = 0;
        word >> temp;
        NumArrary.push_back(temp);
    }
    int prev = NumArrary[0];
    int howMany = 0;
    int a = 0, b = 0, c = 0, d = 0;
    int aCounter = 1;
    int bCounter = 0;
    int cCounter = -1;
    int dCounter = -2;
    int compCheck = -2;

    for (int i = 0; i < NumArrary.size(); i++)
    {
        if (aCounter > 0)
        {
            a = a + NumArrary[i];
        }
        if (bCounter > 0)
        {
            b = b + NumArrary[i];
        }
        if (cCounter > 0)
        {
            c = c + NumArrary[i];
        }
        if (dCounter > 0)
        {
            d = d + NumArrary[i];
        }        if (aCounter == 3)
        {
            aCounter = -1;
        }
        if (bCounter == 3)
        {
            bCounter = -1;
        }
        if (cCounter == 3)
        {
            cCounter = -1;
        }
        if (dCounter == 3)
        {
            dCounter = -1;
        }

        if (compCheck > 0)
        {
            switch (compCheck)
            {
            case 1:
                if (b > a)
                {
                    howMany++;
                }
                a = 0;
                break;
            case 2:
                if (c > b)
                {
                    howMany++;
                }
                b = 0;
                break;
            case 3:
                if (d > c)
                {
                    howMany++;
                }
                c = 0;
                break;
            case 4:
                if (a > d)
                {
                    howMany++;
                }
                d = 0;
                compCheck = 0;
                break;

            case 5:
                compCheck = 0;
                break;
            }
        }

        if (aCounter == 3)
        {
            aCounter = -1;
        }
        if (bCounter == 3)
        {
            bCounter = -1;
        }
        if (cCounter == 3)
        {
            cCounter = -1;
        }
        if (dCounter == 3)
        {
            dCounter = -1;
        }

        aCounter++;
        bCounter++;
        cCounter++;
        dCounter++;
        compCheck++;
    }
    std::cout << howMany << std::endl;
}