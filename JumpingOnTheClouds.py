# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.
# For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

def jumpingOnClouds(c):
    curIndx = 0 
    steps = -1 

    while curIndx < len(c):
        if curIndx + 2 < len(c) and c[curIndx + 2] == 0:
            curIndx += 2 
        else: 
            curIndx += 1 
        
        steps += 1 

    return steps

# Test cases
c = [0, 1, 0, 0, 0, 1, 0]
print(jumpingOnClouds(c))

c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))
