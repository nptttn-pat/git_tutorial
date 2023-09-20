strings = str(input("String: "))
backward = strings[::-1]
if strings == backward:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")