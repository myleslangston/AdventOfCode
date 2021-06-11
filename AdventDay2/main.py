with open("/Users/myleslangston/Documents/Sparta Global /day2.txt", "r") as fp:
    num = fp.readlines()


valid_passwords = 0
for line in num:  # break list up into further lists
    data = line.split(", ")  # "1-3 f: gvfghfdgsgs"
    count = 0
    for char in data:
        data = char.replace('\n', '')
        data = list(data)
        letter = (data[data.index(":") - 1])
        password = data[-1:data.index(':'):-1]


        if '-' == data[1]:
            minimum = int(data[0])

            if ' ' == data[3]:
                maximum = int(data[2])
                for i in password:
                    if i == letter:
                        count += 1
                if count in range(minimum, maximum+1):
                    valid_passwords += 1

            elif ' ' == data[4]:
                maximum = int(data[2] + data[3])
                for i in password:
                    if i == letter:
                        count += 1
                if count in range(minimum, maximum+1):
                    valid_passwords += 1

        elif '-' == data[2]:
            minimum = int(data[0] + data[1])

            if ' ' == data[5]:
                maximum = int(data[3] + data[4])
                for i in password:
                    if i == letter:
                        count += 1
                if count in range(minimum, maximum+1):
                    valid_passwords += 1

print(valid_passwords)

