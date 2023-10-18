import random

# Define grid layout
grid = [
    "########",
    "#......#",
    "#.###..#",
    "#...#.##",
    "#x#....#",
    "########"
]

# Define player's starting position 'x'
playerX = None
playerY = None
for row in range(len(grid)):
    if 'x' in grid[row]:
        playerX = grid[row].index('x')
        playerY = row
        break

# Define the item's position (hidden in a clear path)
itemX, itemY = None, None
while True:
    itemX = random.randint(1, len(grid[0]) - 2)
    itemY = random.randint(1, len(grid) - 2)
    if grid[itemY][itemX] != '#':
        break

# Determine probable item locations (Up, Right, Down)
probableLocations = []

# Up/North
for step in range(playerY - 1, 0, -1):
    probableLocations.append([playerX, step])

# Right/East
for step in range(playerX + 1, len(grid[0])):
    probableLocations.append([step, playerY])

# Down/South
for step in range(playerY + 1, len(grid) - 1):
    probableLocations.append([playerX, step])

# Remove duplicates
uniqueProbableLocations = []
for loc in probableLocations:
    if loc not in uniqueProbableLocations:
        uniqueProbableLocations.append(loc)

# Mark probable item locations in the grid
for x, y in uniqueProbableLocations:
    grid[y] = grid[y][:x] + '$' + grid[y][x + 1:]

# Print the grid with probable item locations
for row in grid:
    print(row)

# Main game loop
while True:
    # Check if the player has found the item
    if playerX == itemX and playerY == itemY:
        print('Selamat! Anda menemukan item tersembunyi.')
        break

    # Get user input for movement
    move = input('Masukkan "W" untuk naik, "S" untuk turun, "A" untuk kiri, "D" untuk kanan, atau "Q" untuk keluar: ')

    # Update player's position based on user input
    if move.upper() == 'W':
        playerY -= 1
    elif move.upper() == 'S':
        playerY += 1
    elif move.upper() == 'A':
        playerX -= 1
    elif move.upper() == 'D':
        playerX += 1
    elif move.upper() == 'Q':
        print('Anda keluar dari permainan.')
        break
    else:
        print('Gerakan tidak valid. Coba lagi.')

    # Ensure the player doesn't move out of bounds
    playerX = max(1, min(playerX, len(grid[0]) - 2))
    playerY = max(1, min(playerY, len(grid) - 2))
