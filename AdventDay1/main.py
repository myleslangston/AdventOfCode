with open("/Users/myleslangston/Documents/Sparta Global /input.txt", "r") as fp:
    num = fp.readlines(int())
    num = [int(i) for i in num]

for x in num:
    if 2020 - x in num:
        print(x*(2020-x))

for x in num:
    for y in num:
        if 2020 - (x+y) in num:
            print(x*(2020-(x+y))*y)







