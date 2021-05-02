# You are given an integer, n. Your task is to print an alphabet rangoli of size .
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:
# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# #size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e



def print_rangoli(n):
    l1=list(map(chr,range(97,123)))
    x=l1[n-1::-1]+l1[1:n]
    m=len('-'.join(x))
    for i in range(1,n+1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))

n=int(input("Enter number to print Rangoli:"))
print_rangoli(n)