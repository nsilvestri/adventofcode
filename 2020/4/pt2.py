#!/bin/python

import re

with open('input.txt', 'r') as file:
    data = file.read()
    passports = data.split('\n\n')
    # split passports strings into lists with each data
    for n in range(0, len(passports)):
        passports[n] = passports[n].split()
    valid = 0
    for passport in passports:
        # has byr
        has_byr = False
        for field in passport:
            if 'byr' in field:
                value = field.split(':')[1]
                if 1920 <= int(value) <= 2002:
                    has_byr = True
                    break

        # has iyr
        has_iyr = False
        for field in passport:
            if 'iyr' in field:
                value = field.split(':')[1]
                if 2010 <= int(value) <= 2020:
                    has_iyr = True
                    break

        # has eyr
        has_eyr = False
        for field in passport:
            if 'eyr' in field:
                value = field.split(':')[1]
                if 2020 <= int(value) <= 2030:
                    has_eyr = True
                    break

        # has hgt
        has_hgt = False
        for field in passport:
            if 'hgt' in field:
                value = field.split(':')[1]
                if value[len(value) - 2:] == 'cm':
                    has_hgt = 150 <= int(value[0:len(value) - 2]) <= 193
                elif value[len(value) - 2:] == 'in':
                    has_hgt = 59 <= int(value[0:len(value) - 2]) <= 76
                break

        # has hcl
        has_hcl = False
        for field in passport:
            if 'hcl' in field:
                value = field.split(':')[1]
                has_hcl = re.match(r"#[0-9a-f]{6}$", value)
                break
        # has ecl
        has_ecl = False
        for field in passport:
            if 'ecl' in field:
                value = field.split(':')[1]
                has_ecl = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                break
        # has pid
        has_pid = False
        for field in passport:
            if 'pid' in field:
                value = field.split(':')[1]
                has_pid = re.match(r"[0-9]{9}$", value)
                break
        # has cid
        has_cid = False
        for field in passport:
            if 'cid' in field:
                has_cid = True
                break

        if has_byr and has_iyr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid:
            valid += 1
        
    print(valid)
    
