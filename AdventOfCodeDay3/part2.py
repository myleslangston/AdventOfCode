from main import *

total = 0
total += moving_through_trees(1, 1)
total *= moving_through_trees(3, 1)
total *= moving_through_trees(5, 1)
total *= moving_through_trees(7, 1)
total *= moving_through_trees(1, 2)
print(total)