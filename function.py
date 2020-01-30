#function.py





from utils import *

# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
     dict1 = { }

    i = 0

    for x in boxes :
        if grid[i]=="." :
            dict1[x]="123456789"
        else :
            dict1 [x]= grid[i]
        i +=1

    return dict1





def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    


    for x in boxes :

        if len(values[x])= 1:



    
    return values






def diagonalSudoku():

    """
    solves the diagonal sudoku using constraint propagation 
    by adding the new constraint of the diagonal sudoku.
    """
    
    pass