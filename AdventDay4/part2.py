from data import pass_list
from main import valid_passports

pass_list_split = pass_list.split('\n\n')
pass_list_replace = [item.replace('\n', " ") for item in pass_list_split]
pass_list_split2 = [item.split() for item in pass_list_replace]


def list_to_dict(password_list):
    pass_dict = {}
    for item in password_list:
        parts = item.split(':')
        key, value = parts[0], parts[1]
        pass_dict[key] = value

    return pass_dict


passports = [list_to_dict(item) for item in pass_list_split2]


def valid_values(passport):
    has_valid_byr = 1920 <= int(passport["byr"]) <= 2002
    has_valid_iyr = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_eyr = 2020 <= int(passport["eyr"]) <= 2030

    has_valid_hgt = False
    hgt_units = passport["hgt"][-2:]
    if hgt_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_hgt = 150 <= height <= 193
    elif hgt_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_hgt = 59 <= height <= 76

    def is_valid_hex_string(string):
        test_value = string.lower()
        is_valid = True
        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break

        return is_valid

    has_valid_hcl = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hcl = is_valid_hex_string(digits)

    has_valid_ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid_pid(value):
        is_valid = False
        if len(value) == 9:
            is_valid = True
            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break

        return is_valid

    has_valid_pid = is_valid_pid(passport["pid"])

    return (
            has_valid_byr and
            has_valid_iyr and
            has_valid_eyr and
            has_valid_hgt and
            has_valid_hcl and
            has_valid_ecl and
            has_valid_pid
    )


truly_valid_passports = [passport for passport in valid_passports if valid_values(passport)]
print(len(truly_valid_passports))



