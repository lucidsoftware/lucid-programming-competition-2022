# Follow the Current
## Description
You and a team of researchers have been tasked with assessing the risk of sailing through the infamous Shipwreck Sea. As part of this risk assessment, you want to determine the passenger’s likelihood of surviving in the event of a sunk ship. If a ship sinks, the passengers will have to wait in life rafts until they wash up on a nearby island. The life rafts have no means of steering or propulsion, so they will be at the mercy of the current.
Your team has prepared a map of the sea for you. This map will include the locations of islands, as well as the direction of the currents. The map is a grid, with each cell in the grid being either land or water. Using this map, you must determine how likely it is that a life raft will wash up on land within the given number of hours.
Each hour, a life raft will move one space on the map. Each time a raft reaches a new space of water, it has a 50% chance of continuing in the direction it was already going, and a 50% chance of turning to follow the direction of the current in that space. In the very first hour, the raft does not yet have a direction, so it will always go in the direction of the current. Because of an ancient curse placed upon this sea, no traveler can escape without a true ship. Therefore, any raft that goes off the edge of the map will wrap around to the other side. The raft will always start in the exact center of the map. This location will always be water. Once a raft reaches land, it will stop there.
## Input
```
Hours
Width Height
Type <CurrentDirection?>
Type <CurrentDirection?>
Type <CurrentDirection?>
Type <CurrentDirection?>
…
```

### Where
Hours = number of hours before the rafts need to reach land
Width = the width of the map
Height = the height of the map
Type = land or water. The number of `Type` inputs will be equal to Width * Height. The cell types are given in reading order: from left to right, and then top to bottom
CurrentDirection = North, East, South, or West. CurrentDirection will only be given if the type is Water

## Output
A single integer showing the probability that a life raft will reach land within the specified number of hours. This should be rounded to the nearest whole percentage point, or rounded up if it’s halfway between two percentage points.

## Constraints
0 < Hours < 100
0 < Width < 100, Width will always be an odd number (so there is a definite center)
0 < Height < 100, Height will always be an odd number (so there is a definite center)

## Examples
### Input 1
1
3 3
Land
Land
Land
Water East
Water North
Water West
Land
Land
Land

Visualization (not included in input):

| Ѧ | Ѧ | Ѧ |
| - | - | - |
| → | ↑ | ← |
| Ѧ | Ѧ | Ѧ |


Output 1

100

Input 2

lexiyorgason@gmail.com

Visualization (not included in input):

| Ѧ | ← | → | Ѧ | Ѧ |
| - | - | - | - | - |
| Ѧ | ↑ | ← | Ѧ | ↓ |
| Ѧ | ← | ↓ | ↑ | → |


Output 2

75
