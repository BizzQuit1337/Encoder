import os

user_input = str(input('choose a file to decode: '))

def get_shift():
    with open('key.txt', 'r', encoding="utf-8") as f:
        for shift in f:
            get_shift.int = ord(shift)
        
def gcl(file, shift):
    gcl.str_list = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            for charecter in line:
                int_chr = (ord(charecter) - shift)
                gcl.str_list.append(chr(int_chr))
      

def l2s(list):
    l2s.string = ''
    for charecter in list:
        l2s.string += charecter 


get_shift()
shift = get_shift.int
gcl(user_input, shift)
l2s(gcl.str_list)
print(l2s.string)