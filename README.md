# game-of-life
A pygame implimentation of conway's game of life

Must have python and pygame installed to run

Initially starts frozen, use spacebar to unfreeze and freeze.
Click on cells to kill or revive them.
Sarts a simple pattern that spawns some cool chaotic behavior. 

2/3 live neighbors: cell survives. 
<2 or >3 live neighbors: cell dies. 
dead cells with == 3 live neighbors will come alive. 

board is not infinite and there is some interesting edge behavior. 

Press q to clear the board. 
change line 23 and uncomment 23-35 to load patterns from https://conwaylife.com/wiki/.
All credit for these patterns goes to original creaters

press 'c' to save a pattern.
saved patterns must be opened with lines 18/19.
Must close and reopen program to load your own saved patterns.

comment/uncomment 18/19 and 23-35 to switch between your own saved patterns 
and patterns from https://conwaylife.com/wiki/.