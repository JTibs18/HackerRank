# Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?
# Input format: The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.
# Grid is indexed using Matrix Convention
# Output format: Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.
# Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. The goal is to reach the princess in as few moves as possible.
# The above sample input is just to help you understand the format. The princess ('p') can be in any one of the four corners.

def displayPathToPrincess1(n, grid):
    for indxY, row in enumerate(grid):
        for indxX, val in enumerate(row):
            if val == "m":
                botPosition = (indxY, indxX)
            if val == "p":
                princessPosition = (indxY, indxX)

    if botPosition[0] < princessPosition[0]:
        for _ in range(princessPosition[0] - botPosition[0]):
            print("DOWN")
    else:
        for _ in range(botPosition[0] - princessPosition[0]):
            print("UP")

    if botPosition[1] < princessPosition[1]:
        for _ in range(princessPosition[1] - botPosition[1]):
            print("RIGHT")
    else:
        for _ in range(botPosition[1] - princessPosition[1]):
            print("LEFT")

def displayPathToPrincess(n, grid):
    botPosition = (n // 2, n // 2)
    possiblePrincessPositions = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]

    for coord in possiblePrincessPositions:
        if grid[coord[0]][coord[1]] == "p":
            princessPosition = coord 
            break 

    if botPosition[0] < princessPosition[0]:
        for _ in range(princessPosition[0] - botPosition[0]):
            print("DOWN")
    else:
        for _ in range(botPosition[0] - princessPosition[0]):
            print("UP")

    if botPosition[1] < princessPosition[1]:
        for _ in range(princessPosition[1] - botPosition[1]):
            print("RIGHT")
    else:
        for _ in range(botPosition[1] - princessPosition[1]):
            print("LEFT")

# Test cases
n = 3
grid = [["-", "-" ,"-"], ["-", "m", "-"], ["p", "-", "-"]]
displayPathToPrincess(n, grid)

n = 3
grid = [["-", "-" ,"-"], ["-", "m", "-"], ["-", "-", "p"]]
displayPathToPrincess(n, grid)
