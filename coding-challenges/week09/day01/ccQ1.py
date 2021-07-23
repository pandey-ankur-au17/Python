def findPalindrome(n, temp):

    if (n == 0):

        return temp;
    temp = (temp * 10) + (n % 10);
    return findPalindrome(n / 10, temp);



if __name__ == "__main__":

    n = 121;
    temp = findPalindrome(n, 0);

    if (temp != n):
        print("Palindrome");
    else:  
        print("Not Palindrome");