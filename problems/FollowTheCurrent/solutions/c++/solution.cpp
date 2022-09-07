#include <iostream>
#include <vector>
using namespace std;

enum direction 
{   north = 0, 
    east = 1, 
    south = 2,
    west = 3
};

vector<vector<string>> createVector(int height, int width){
   vector<vector<string>> fullVector;
   for(int row = 0; row < height; row++){
       vector<string> vectorRow;
        for(int col = 0; col < width; col++){
            vectorRow.push_back(" ");
        }
        fullVector.push_back(vectorRow);
    } 
    return fullVector;
}

vector<vector<vector<long>>> createRaftVector(int height, int width){
   vector<vector<vector<long>>> fullVector;
   for(int row = 0; row < height; row++){
       vector<vector<long>> vectorRow;
        for(int col = 0; col < width; col++){
            vector<long> vectorCol;
            for(int i = north; i <= west; i++){
                vectorCol.push_back(0);
            }
            vectorRow.push_back(vectorCol);
        }
        fullVector.push_back(vectorRow);
    }
    return fullVector;
}

string shortenCurrent(string original){
    if(original == "North") {
        return "N";
    }
    if(original == "East") {
        return "E";
    }
    if(original == "South") {
        return "S";
    }
    if(original == "West") {
        return "W";
    }
    return "?";
}

direction stringToDirection(string original){
    if(original == "N") {
        return north;
    }
    if(original == "E") {
        return east;
    }
    if(original == "S") {
        return south;
    }
    return west;
}

void stepInDirection(int& originalX, int& originalY, int dir, int height, int width){
    if(dir == north){
        originalY = (originalY - 1);
        if(originalY < 0){ originalY += height;}
    } else if(dir == east){
        originalX = (originalX + 1) % width;
    } else if(dir == south){
        originalY = (originalY + 1) % height;
    } else if(dir == west){
        originalX = (originalX - 1);
        if(originalX < 0){ originalX += width;}
    } else {
        cout << "direction error\n";
    }
}

vector<vector<vector<long>>> passOneHour(vector<vector<vector<long>>> currentLocations, vector<vector<string>> currents, vector<vector<string>> types, int height, int width){
    vector<vector<vector<long>>> newLocations = createRaftVector(height, width);
    for(int row = 0; row < height; row++){
        for(int col = 0; col < width; col++){
            string type = types.at(row).at(col);
            if(type == "L") {
                newLocations.at(row).at(col).at(0) += currentLocations.at(row).at(col).at(0) * 2;
                newLocations.at(row).at(col).at(1) += currentLocations.at(row).at(col).at(1) * 2;
                newLocations.at(row).at(col).at(2) += currentLocations.at(row).at(col).at(2) * 2;
                newLocations.at(row).at(col).at(3) += currentLocations.at(row).at(col).at(3) * 2;
            }
            else{
                direction current = stringToDirection(currents.at(row).at(col));
                for(int dir = north; dir <= west; dir++){
                    int x = col;
                    int y = row;
                    stepInDirection(x, y, dir, height, width);
                    newLocations.at(y).at(x).at(dir) += currentLocations.at(row).at(col).at(dir);
                    x = col;
                    y = row;
                    stepInDirection(x, y, current, height, width);
                    newLocations.at(y).at(x).at(current) += currentLocations.at(row).at(col).at(dir);
                } 
            }
        }
    }
    return newLocations;
}

int countLand(vector<vector<vector<long>>> rafts, vector<vector<string>> types, int height, int width) {
    long total = 0;
    long land = 0;
    for(int row = 0; row < height; row++){
        for(int col = 0; col < width; col++){
            for(int dir = north; dir <= west; dir++){
                if(types.at(row).at(col) == "L") {
                    land += rafts.at(row).at(col).at(dir);
                }
                total += rafts.at(row).at(col).at(dir);
            }
        }
    }
    long decimalCorrection = total / 2;
    return ((land * 100) + decimalCorrection) / total;
}

int main() {
    int width;
    int height;
    int hours;
    string type;
    string current;
    cin >> hours >> width >> height;
    vector<vector<string>> types = createVector(height, width);
    vector<vector<string>> currents = createVector(height, width);
    vector<vector<vector<long>>> rafts = createRaftVector(height, width);
    int centerHeight = height /2;
    int centerWidth = width / 2;
    for(int row = 0; row < height; row++){
        for(int col = 0; col < width; col++){
            cin >> type;
            types.at(row).at(col) = type == "Water" ? "W" : "L";
            if(type == "Water"){
                cin >> current;
                currents.at(row).at(col) = shortenCurrent(current);
            }
        }
    }
    direction startingDirection = stringToDirection(currents.at(centerHeight).at(centerWidth));
    rafts.at(centerHeight).at(centerWidth).at(startingDirection) = 1;
    for(int hour = 1; hour <= hours; hour++){
        rafts = passOneHour(rafts, currents, types, height, width);
    }
    cout << countLand(rafts, types, height, width);

    return 0;
}
