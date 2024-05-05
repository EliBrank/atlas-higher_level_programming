#!/usr/bin/python3

def roman_to_int(roman_string):
    numerals = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }
    roman_string_rev = reversed(roman_string)
    total = 0

    # print(list(numerals.values())[3])

    for i in roman_str_rev:
        if i is in numerals:
            total += 



roman_to_int("VI")

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
