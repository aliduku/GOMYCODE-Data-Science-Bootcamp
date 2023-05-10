def palindrome_check(string):
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

palindrome_check(input("Enter a string: "))