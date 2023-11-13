# 01
def odd_even(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


odd_even(4)
odd_even(7)


# 02
def longest_string(str1, str2, str3):
    len1 = len(str1.replace(' ', ''))
    len2 = len(str2.replace(' ', ''))
    len3 = len(str3.replace(' ', ''))
    max_string = max(len1, len2, len3)
    if max_string == len1:
        if max_string == len2:
            if max_string == len3:
                print("String 1, 2, 3 are the longest. Those have {} characters.".format(len1))
            else:
                print("String 1, 2 are the longest. Those have {} characters.".format(len1))
        elif max_string == len3:
            print("String 1, 3 are the longest. Those have {} characters.".format(len1))
        else:
            print("String 1 is the longest. It has {} characters.".format(len1))

    elif max_string == len2:
        if max_string == len3:
            print("String 2, 3 are the longest. Those have {} characters.".format(len2))
        else:
            print("String 2 is the longest. It has {} characters.".format(len2))

    elif max_string == len3:
        print("String 3 is the longest. It has {} characters.".format(len3))


string1 = input("Enter a sentence or word: ")
string2 = input("Enter a sentence or word: ")
string3 = input("Enter a sentence or word: ")

longest_string(string1, string2, string3)

