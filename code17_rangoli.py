# You are given an integer, n. Your task is to print an alphabet rangoli of size .
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:
# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
# #size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

import string

def print_rangoli(size):
    characters = string.ascii_lowercase
    lst = []
    width  = 4 * size -3
    i=0
    while i<n:
        s = '-'.join(characters[i:size])
        lst.append((s[::-1] + s[1:]).center(width,'-'))
        i=i+1
    print('\n'.join(lst[:0:-1] + lst))

n = int(input("Enter number to print Rangoli:"))
print_rangoli(n)