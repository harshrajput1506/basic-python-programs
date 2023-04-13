def isPalindrome(str):
 
    length = int(len(str)/2)
    for i in range(0, length): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
#-main-
str = input("Enter a string - ")
ans = isPalindrome(str)
 
if (ans):
    print(str, "is palindrome")
else:
    print(str, "is not palindrome")
