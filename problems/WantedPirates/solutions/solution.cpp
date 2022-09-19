#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <chrono>

using namespace std;

int main()
{
    int num_lines;
    cin >> num_lines;
    vector<unordered_set<string>> all_pirates;

    int smallest_index = 0;

    for (int i = 0; i < num_lines; i++)
    {
        string line;
        cin >> line;
        stringstream ss(line);

        string country;
        getline(ss, country, ',');

        unordered_set<string> pirates;
        while (ss.good())
        {
            string name;
            getline(ss, name, ',');
            pirates.emplace(name);
        }
        all_pirates.push_back(pirates);
        if (pirates.size() < all_pirates[smallest_index].size())
        {
            smallest_index = i;
        }
    }

    unordered_set<string> smallest;
    for (string pirate : all_pirates[smallest_index])
    {
        smallest.emplace(pirate);
    }

    for (unordered_set<string> pirates : all_pirates)
    {
        vector<string> to_remove;
        for (string pirate : smallest)
        {
            if (pirates.count(pirate) == 0)
            {
                to_remove.push_back(pirate);
            }
        }
        for (string pirate : to_remove)
        {
            smallest.erase(pirate);
        }
    }

    // output
    vector<string> output;
    for (string pirate : smallest)
    {
        output.push_back(pirate);
    }

    sort(output.begin(), output.end());

    for (string pirate : output)
    {
        cout << pirate << endl;
    }
}