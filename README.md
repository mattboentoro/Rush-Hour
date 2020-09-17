# Rush-Hour
The puzzle called "Rush Hour" (c. ThinkFun, Inc., www.thinkfun.com) begins with a six-by-six grid of squares.  Little plastic cars and trucks are distributed across the grid in such a way as to preventone special car from moving off the grid, thereby escaping the traffic jam. The initial configuration of cars and trucks is preordained by a set of cards, each containing a different starting pattern. A player draws a card from the deck of cards, sets up the cars and trucks according to the pattern, and then tries to move the special car off the grid by sliding the cars and trucks up and down or left and right, depending on the starting orientation of the cars and trucks.  

Cars occupy two contiguous squares, while trucks occupy three contiguous squares. All vehicles are oriented horizontally or vertically, never on the diagonal. Vehicles that are oriented horizontally may only move horizontally; vehicles that are oriented vertically may only move vertically. Vehicles may not be lifted from the grid, and there is never any diagonal movement. Vehicles may not be partially on the grid and partially off the grid. The special car is called the X car.  We'll represent it on the grid as two contiguous squares with the letter X in them.  (We'll represent all other cars and trucks with different letters of the alphabet, but the special car will always be labeled with the letter X.) The X car is always oriented horizontally on the third row from the top; otherwise, the X car could never escape.  If it were the only car on the grid, it might look like this (although it could start anywhere on that third row)  

Your assignment is to use Python to write a program called rushhour which employs best-first search with the A* algorithm to solve a "Rush Hour" puzzle with any legal initial state.  Your rushhour program expects two arguments.  The second argument is a description of the initial-state as a list of six strings, each string containing six characters. For the initial configuration, the list of stringspassed to rushhourwould look like this:  
```
["--B---","--B---","XXB---","--AA--","------","------"]
```
The first string corresponds to the top row, the second string corresponds to the next row down, and so on. If this list were formatted nicely, it would look more like the grid above:
```
["--B---",
 "--B---",
 "XXB---",
 "--AA--",
 "------",
 "------"]
```
