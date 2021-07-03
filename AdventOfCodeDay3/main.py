with open("/Users/myleslangston/Documents/Sparta Global /AdventOfCode/AdventOfCodeDay3/day3.txt", 'r') as day3:
    file = day3.readlines()

# count 3 spaces right on each line
# count 1 space down for each line
# if a hash is in the place, add to tree counter


def moving_through_trees(right, down):
    right_coord = 0
    down_coord = 0
    tree_counter = 0

    while down_coord < len(file):
        if tree_at_coordinate(right_coord, down_coord):
            tree_counter += 1
        right_coord += right
        down_coord += down
    return tree_counter


def tree_at_coordinate(tree_x, tree_y):
    total_x = tree_x % 31
    return file[tree_y][total_x] == '#'

