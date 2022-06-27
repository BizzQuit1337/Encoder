###imports
import os, sys, random, hashlib, sympy

user_input = str(input('what file would you like to encode: '))

###variables
counter = 0

shift = (sympy.randprime(1, 9)) * (sympy.randprime(1, 9))


###functions
def gwl(file, shift):
    gwl.chr_list = []
    with open(file, 'r') as f:
        for line in f:
            for charecter in line:
                gwl.chr_list.append(chr(ord(charecter) + shift))


def shift_save(shift):
    with open('key.txt', 'w', encoding="utf-8") as f:
      f.write(chr(shift))

def str_save(file, list):
    with open(file, 'w', encoding="utf-8") as f:
        f.write('')
    with open(file, 'a', encoding="utf-8") as f:
        for charecter in list:
            f.write(charecter)


###main event

while True:
    
    gwl(user_input, shift)
    shift_save(shift)
    str_save(user_input, gwl.chr_list)
    counter = counter + 1

    if counter == 1:
        break
