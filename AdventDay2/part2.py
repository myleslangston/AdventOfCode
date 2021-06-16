with open("/Users/myleslangston/Documents/Sparta Global /day2.txt", "r") as fp:
    num = fp.readlines()

count = 0
valid_passwords = 0
for line in num:  # break list up into further lists
    data = line.split(", ")  # "1-3 f: gvfghfdgsgs"

    for char in data:
        data = char.replace('\n', '')
        letter = (data[data.index(":") - 1])
        password = data.split(" ")[2]
        numbers = data.split(" ")[0]
        location2 = int(numbers.split("-")[1])
        location1 = int(numbers.split("-")[0])
        letter1 = password[location1-1]
        letter2 = password[location2-1]
        if letter == letter1 and letter != letter2:
            valid_passwords += 1
        elif letter != letter1 and letter == letter2:
            valid_passwords += 1

print(valid_passwords)