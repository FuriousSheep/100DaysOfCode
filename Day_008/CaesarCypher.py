import CaesarCypherData as C

def shiftChar(char, shift ):
    return chr(ord(char) + shift)

def shiftMessage(message, shift):
    temp = list(message)
    for i in range(0,len(temp)):
        temp[i] = shiftChar(temp[i], shift)
    shiftedMessage = "".join(temp)
    return shiftedMessage

def unshiftMessage(message,shift):
    return shiftMessage(message, -shift)

def encodeMessage():
    message = input(C.encodeMessage)

def decodeMessage():
    message = input(C.decodeMessage)

def caesarCypher():
    choice = input(C.encodeOrDecode)
    if choice == "encode":
        encodeMessage()
    elif choice == "decode":
        # input(C.decodeMessage)
        decodeMessage()
    else:
        print(C.inputErrorMessage + C.optionsDictionary['encodeOrDecode'])



def main():
    print(C.logo)
    caesarCypher()
    while(input(C.goAgainMessage) == "yes"):
        caesarCypher()


if __name__ == "__main__":
    main()
