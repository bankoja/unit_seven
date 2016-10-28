# James Bankole 10/28/16 unit seven


def modeSelect():
    """This function asks the user whether they would like to encode, decode, or quit"""
    return input("Would you like to encode (e), decode (d), or quit (q)?")


def decode():
    """This function takes a string from the user, prompts them to input a number to represent what the original
    text was shifted by, decodes the string, and then displays to user."""
    userString = input("Please input a string you would like to decode (no spaces).")
    stringRotation = int(input("Input an amount between 1 and 25 that original text was rotated by."))
    x = stringRotation
    alphabetString = "abcdefghijklmnopqrstuvwxyz"
    rotatedAlphabet = alphabetString[x:] + alphabetString[:x]
    decodedString = ""
    for x in userString.lower():
        pie = rotatedAlphabet.index(x)
        decodedString += alphabetString[pie]
    print(decodedString)


def encode():
    """This function does the opposite of decode."""
    userString = input("Please input a string you would like to encode (no spaces).")
    stringRotation = int(input("Input an amount between 1 and 25 that you would like to rotate by."))
    x = stringRotation
    alphabetString = "abcdefghijklmnopqrstuvwxyz"
    rotatedAlphabet = alphabetString[x:] + alphabetString[:x]
    encodedString = ""
    for x in userString.lower():
        pie = alphabetString.index(x)
        encodedString += rotatedAlphabet[pie]
    print(encodedString)


def main():
    userChoice = modeSelect()
    if userChoice == "d":
        decode()
    elif userChoice == "e":
        encode()


main()
