from random import randint

parent_cells = []
parent_cells_length = 50
cellss = []

generations = 1000

# Apply Wolfram's Rule 110
def rule_110(cell, left, right):
    if(left == 1 and cell == 1 and right == 1):
        return 0
    elif(left == 1 and cell == 1 and right == 0):
        return 1
    elif(left == 1 and cell == 0 and right == 1):
        return 1
    elif(left == 1 and cell == 0 and right == 0):
        return 0
    elif(left == 0 and cell == 1 and right == 1):
        return 1
    elif(left == 0 and cell == 1 and right == 0):
        return 1
    elif(left == 0 and cell == 0 and right == 1):
        return 1
    elif(left == 0 and cell == 0 and right == 0):
        return 0
    else:
        return cell

# Get the next generation of cells
def get_next_gerenation(cells):
    temp_cells = []

    for x in range(0, len(cells)):
        left = cells[x -1]

        if(x < (len(cells) - 1)):
            right = cells[x + 1]
        else:
            right = cells[x]

        temp_cells.append(rule_110(cells[x], left, right))

    return temp_cells

# Set Initial Random Numbers
def set_random():
    temp_cells = []

    for x in range(0, parent_cells_length):
        temp_cells.append(randint(0,1))

    return temp_cells

#Print line in a beautiful way
def print_line(cells):

    line = ""

    for cell in cells:
        if cell == 1:
            line += " # "
        else:
            line += "   "

    print line


# Let the game begin
def begin():
    parent_cells = set_random()

    for g in range(0, generations):
        cells = get_next_gerenation(parent_cells)
        print_line(cells)
        parent_cells = cells

# Begin
begin()
