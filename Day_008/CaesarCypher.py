import CaesarCypherData as C

#####################################
#              UTILITY              #
#####################################

def shiftChar(char, shift ):
    shiftedChar = ord(char) + shift
    if shiftedChar > 122:
        shiftedChar -= 26
    elif shiftedChar < 97:
        shiftedChar +=26
    return chr(shiftedChar)

def shiftMessage(message, shift):
    temp = list(message)
    for i in range(0,len(temp)):
        if ord(temp[i]) >= 97 and ord(temp[i]) <= 122:
            temp[i] = shiftChar(temp[i], shift)
    shiftedMessage = "".join(temp)
    return shiftedMessage

def unshiftMessage(message,shift):
    return shiftMessage(message, -shift)

#####################################
#         encode / decode           #
#####################################

def getCypherNumber():
    cypherNumber = int(input(C.cypherChoice))
    while cypherNumber > 25 or cypherNumber < 1:
        print(C.inputErrorMessage)
        cypherNumber = int(input(C.cypherChoice))

def encodeMessage():
    message = input(C.encodeMessage).lower()
    cypherNumber = getCypherNumber()
    codedMessage = shiftMessage(message, cypherNumber)
    print(C.encodeResultMessage + "\n" + codedMessage) 

def decodeMessage():
    message = input(C.decodeMessage).lower()
    cypherNumber = getCypherNumber()
    decodedMessage = unshiftMessage(message, cypherNumber)
    print(C.decodeResultMessage + "\n" + decodedMessage)

#####################################
#            main loop              #
#####################################

def caesarCypher():
    choice = input(C.encodeOrDecode)
    if choice == "encode":
        encodeMessage()
    elif choice == "decode":
        decodeMessage()
    else:
        print(C.inputErrorMessage + C.optionsDictionary['encodeOrDecode'])

#####################################
#               MAIN                #
#####################################


def main():
    print(C.logo)
    caesarCypher()
    while(input(C.goAgainMessage) == "yes"):
        caesarCypher()


if __name__ == "__main__":
    main()
