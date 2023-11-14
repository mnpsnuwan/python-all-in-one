def palindrome(word):
    reverse = word[::-1]
    if word.lower() == reverse.lower():
        print("\"" + word + "\" is a Palindrome")
    else:
        print("\"" + word + "\" is not a Palindrome")


string = input("Enter a string: ")
palindrome(string)

