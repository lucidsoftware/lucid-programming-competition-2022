#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

const bool useLongNames = true;
const string north = useLongNames ? "North" : "N";
const string east = useLongNames ? "East" : "E";
const string south = useLongNames ? "South" : "S";
const string west = useLongNames ? "West" : "W";

const string water = useLongNames ? "Water" : "W";
const string land = useLongNames ? "Land" : "L";

void printVector(vector<vector<string>> fullVector){
    for(int row = 0; row < fullVector.size(); row++){
        for(int col = 0; col < fullVector.at(0).size(); col++){
            cout << fullVector.at(row).at(col);
        }
        cout << "\n";
    }
    cout << "\n";
}

string getCurrent(){
    int direction = rand() % 4;
                if(direction == 0){
                    return north;
                } else if(direction == 1){
                    return east;
                } else if(direction == 2){
                    return south;
                } else if(direction == 3){
                    return west;
                }
                return "ERROR";
}

int main() {
    int width = 49;
    int height = 49;
    int hours = 60;
    int centerWidth = width / 2;
    int centerHeight = height / 2;
    int landFrequencyPercent = 2;
    vector<vector<string>> types;
    vector<vector<string>> currents;
    for(int row = 0; row < height; row++){
        vector<string> typeRow;
        vector<string> currentRow;
        for(int col = 0; col < width; col++){
            if(rand() % 100 < landFrequencyPercent){
                typeRow.push_back(land);
                currentRow.push_back(" ");
            } else {
                typeRow.push_back(water);
                currentRow.push_back(getCurrent());
            }
        }
        types.push_back(typeRow);
        currents.push_back(currentRow);
    }
    types.at(centerHeight).at(centerWidth) = water;
    currents.at(centerHeight).at(centerWidth) = getCurrent();
    //printVector(types);
    //printVector(currents);
    cout << hours << "\n" << width << " " << height << "\n";
    for(int row = 0; row < height; row++){
        for(int col = 0; col < width; col++){
            cout << types.at(row).at(col) << " " << currents.at(row).at(col) << "\n";
        }
    }
    return 0;
}
