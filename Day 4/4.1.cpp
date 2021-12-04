#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

struct Number
{
    int value;
    bool found;
    Number(int inp_value)
    {
        value = inp_value;
        found = false;
    }

    void set_found()
    {
        found = true;
    }
};

struct Board
{
    std::vector<std::vector<Number> > numbers;

    void clear()
    {
        numbers.clear();
    }
    void add(std::vector<Number> row)
    {
        numbers.push_back(row);
    }
    size_t get_size()
    {
        return numbers.size();
    }

    void print_board()
    {
        for (size_t j = 0; j < this->get_size(); j++)
        {
            for (size_t k = 0; k < this->numbers[j].size(); k++)
            {
                std::cout << this->numbers[j][k].value;
                if (k != 4)
                {
                    std::cout << ", ";
                }
                else
                {
                    std::cout << std::endl;
                }
            }
        }
    }
};

void print_all_boards(std::vector<Board> inp)
{
    std::cout << "----------" << std::endl;
    for (size_t i = 0; i < inp.size(); i++)
    {
        inp[i].print_board();

        std::cout << "----------" << std::endl;
    }
}

int main()
{
    std::vector<Board> boards;
    std::string line;

    std::getline(std::cin, line);
    std::replace( line.begin(), line.end(), ',', ' ');
    std::istringstream first_line(line);
    std::vector<int> number_call_outs;
    std::string first_a;
    while (first_line >> first_a)
    {
        if (!first_a.empty())
        {
            number_call_outs.push_back(std::stoi(first_a));
        }
    }
    for (size_t i = 0; i < number_call_outs.size(); i++)
    {
        std::cout << number_call_outs[i] << ", ";
    }
    return 0;

    Board current_board;
    while (std::getline(std::cin, line))
    {
        std::istringstream temp(line);
        std::string a;
        std::vector<Number> row;
        while (temp >> a)
        {
            if (!a.empty() && (a.find_first_not_of(' ') != std::string::npos) && a != "\n")
            {
                Number spot(std::stoi(a));
                row.push_back(spot);
            }
        }
        current_board.add(row);
        if (current_board.get_size() == 6)
        {
            boards.push_back(current_board);
            current_board.clear();
        }
    }
    print_all_boards(boards);
};