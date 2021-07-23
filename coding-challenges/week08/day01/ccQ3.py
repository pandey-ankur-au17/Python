# If we have a string, write a function that prints reverse of that string, using
# recursion.
# Sample Input:
# ABCD
# Sample Output:
# DCBA


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
  
s = input("Enter String:")
print (reverse(s))