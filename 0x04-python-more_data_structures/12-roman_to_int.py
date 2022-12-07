#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_t = 0
    for t in range(len(roman_string)):
        if t > 0 and rom[roman_string[t]] > rom[roman_string[t - 1]]:
            rom_t += rom[roman_string[t]] - 2 * \
                        rom[roman_string[t - 1]]
        else:
            rom_t += rom[roman_string[t]]
    return rom_t
