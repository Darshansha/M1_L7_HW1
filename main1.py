
char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    ascii_value = ord(char)
    print("The ASCII value of ", char, " is", ascii_value)