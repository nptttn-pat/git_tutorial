input_string = input("String: ")

# Remove spaces and convert the string to lowercase
cleaned = input_string.replace(" ", "").lower()

# Check if the cleaned string is equal to its reverse
if cleaned == cleaned[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
