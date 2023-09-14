# Using Mixed Integer programming to solve Sudoku.
# The Sudoku problem has four main constraints:
# 1. Each cell has exactly one value (Obvious!!).
# 2. Every value (1-9) occurs in each row exactly once.
# 3. Every value (1-9) occurs in each column exactly once.
# 4. Every value (1-9) occurs in each 3x3 sub-grid exactly one.
#
# Use binary variables x[row][column][value], which take the
# value 1 if the value at (row, column) is equal to value.
# Constraint 1 specifies that sum(x) over all values(1-9) equalso 1
# for each (row, column). This results in 81 equations.
# Similarly sum(x) over all columns and values is 1 for every row.
# This translates to 81 equations.
# Constraint 3 and 4 translate to 81 equations each.
# This gives 324 equations.
# Finally, we add constraints for already filled cells.
from mip import *

m = Model()

x = np.empty((9, 9, 9), dtype=mip.Var)

print(x)

for i in range(9):
    for j in range(9):
        for k in range(9):
            x[i][j][k] = m.add_var(var_type=INTEGER, lb=0, ub=1)


# Exactly one value per cell.
for i in range(9):
    for j in range(9):
        m += xsum(x[i][j][k] for k in range(9)) == 1

# Each value occurs once per row
for i in range(9):
    for k in range(9):
        m += xsum(x[i][j][k] for j in range(9)) == 1

# and per column
for j in range(9):
    for k in range(9):
        m += xsum(x[i][j][k] for i in range(9)) == 1

# and per sub-grid.
for k in range(9):
    for sub_row in range(3):
        for sub_col in range(3):
            m += xsum(x[sub_row * 3 + row][sub_col * 3 + col][k] for row in range(3) for col in range(3)) == 1


m.objective = minimize(x[0][0][0])


problem = [
    [
        None, 2, None, None, None, None, None, None, None,
    ],
    [
        None,None,None, 6,None, None, None, None, None,
    ],
    [
        None, 7, 4, None, 8, None, None, None, None,
    ],

    [
        None, None, None, None, None, 3, None, None, 2
    ],
    [
        None, 8, None, None, 4, None, None, 1, None,
    ],
    [
        6, None, None, 5, None, None, None, None, None,
    ],
    [
        None, None, None, None, 1, None, 7, 8, None,
    ],
    [
        5, None, None, None, None, None, 9, None, None, None,
    ],
    [
        None, None, None, None, None, None, None, 4, None,

    ],
]

for i in range(9):
    for j in range(9):
        if problem[i][j]:
            for k in range(9):
                if problem[i][j] == k + 1:
                    m += x[i][j][k] == 1
                else:
                    m += x[i][j][k] == 0

status = m.optimize(max_seconds=300)

if status == OptimizationStatus.OPTIMAL:
    print('optimal solution cost {} found'.format(m.objective_value))
elif status == OptimizationStatus.FEASIBLE:
    print('sol.cost {} found, best possible: {}'.format(m.objective_value, m.objective_bound))
elif status == OptimizationStatus.NO_SOLUTION_FOUND:
    print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))


for row in range(9):
    for col in range(9):
        for v in range(9):
            if x[row][col][v].x > 0:
                print(v + 1, end = ' ')
    print('\n')


