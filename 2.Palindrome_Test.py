Strings = str(input("String: "))
Backward = Strings[::-1]
if Strings == Backward:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")