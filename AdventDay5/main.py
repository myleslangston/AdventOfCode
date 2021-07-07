with open("/Users/myleslangston/Documents/Sparta Global /AdventOfCode/AdventDay5/day5.txt", 'r') as day5:
    boarding_passes = day5.readlines()
# find row for each line,
boarding_passes_remove = [item.replace('\n', "") for item in boarding_passes]
# there are rows 0 to 127, 128 in total
# F = lower half (0, 63)
# B = upper half (64, 127)
seat_ids = []
for line in boarding_passes_remove:
    start = 0
    end = 127
    rows = line[:7]
    for char in rows:
        if char == 'F':
            end = int(((start + end) + 1) / 2) - 1
        if char == 'B':
            start = int(((start + end) + 1) / 2)
    row = start

# find column for the row in each boarding pass
# R = upper half of columns (4, 7)
# L = lower half of columns (0, 3)

    start = 0
    end = 7
    rows = line[7:]
    for char in rows:
        if char == 'L':
            end = int(((start + end) + 1) / 2) - 1
        if char == 'R':
            start = int(((start + end) + 1) / 2)
    column = start
# find seat id by multiplying the row by 8 and adding the column
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

# find highest seat id
max_seat_id = max(seat_ids)

# find my seat - part 2
# for range of max and min id's, find the id that's not in the previous list
min_seat_id = min(seat_ids)

for seat in range(min_seat_id, max_seat_id):
    if seat not in seat_ids:
        print(seat)



