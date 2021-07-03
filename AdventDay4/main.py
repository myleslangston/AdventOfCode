from data import pass_list

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


def valid_passport(passport):
    has_byr = 'byr' in passport
    has_iyr = 'iyr' in passport
    has_eyr = 'eyr' in passport
    has_hgt = 'hgt' in passport
    has_hcl = 'hcl' in passport
    has_ecl = 'ecl' in passport
    has_pid = 'pid' in passport
    return (has_byr and has_iyr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid)


valid_passports = [passport for passport in passports if valid_passport(passport)]
print(len(valid_passports))