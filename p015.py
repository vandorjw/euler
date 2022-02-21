"""
Lattice Paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""


# only 2 moves, down and right.
# a TWO-by-TWO grid has the following move sets
# 
# a) R, R, D, D
# b) R, D, R, D
# c) R, D, D, R
# d) D, R, R, D
# e) D, R, D, R
# f) D, D, R, R


# why is this?
# A vertice has at most 2 exit paths.
# if a vertice has no right neighbour, then it has 1 exit path.
# if a vertice has no down neighbour, then it has 1 exit path.
# if a vertice has neither a right, or down neighbour, then it has 0 exit paths.


# ONE-by-ONE [solution: 2 paths]
# 2 1      
# 1 0

# TWO-by-ONE [ solution: 3 paths]
# 2 2 1
# 1 1 0

# ONE-BY-TWO [ solution: 3 paths]
# 2 1
# 2 1
# 1 0

# TWO-by-TWO [solution: 6 paths]
# 2 2 1
# 2 2 1
# 1 1 0


# a THREE-by-THREE Matrix has the following exit paths on each vertice
# 2 2 2 1
# 2 2 2 1
# 2 2 2 1
# 1 1 1 0

# = = = = = = = = = = = = = = 
# The general pattern here is that the right most collumn is filled with 1s
# and the bottom most row is also filled with 1.

# to calculate how many paths from vertice n, add together V(i,j) == V(i+1, j) + V(i, j+1)

# 2X2

#
# * * 1         *  *   1            * (3) [1]       *   3  1            6 3 1
# * * 1   -->   * (2) [1]   -->     * [2]  1   --> (3) [2] 1    -->     3 2 1
# 1 1 0         1 [1]  0            1  1   0       [1]  1  0            1 1 0
#


## === a python solution ===

m_size = 20

m = [[None if x != m_size else 1 for x in range(m_size+1)] if y != m_size else [1 if x != m_size else 0 for x in range(m_size + 1)] for y in range(m_size + 1)]


for i in reversed(range(m_size+1)): 
    for j in reversed(range(m_size+1)):
        if m[i][j] is None:
            m[i][j] = m[i+1][j] + m[i][j+1]

print(m[0][0])



