#!/usr/bin python3
from base64 import b64encode,b64decode

def encoding(plainText):
    NUM = "0123456789"
    encText = ""
    for n in range(len(plainText)):
        if n <= 9:
            encText += plainText[n] + NUM[n]
        else:
            m = n % 10
            encText += plainText[n] + NUM[m]
    return encText

def encrypt(plainText):
    b64Text = str(b64encode(bytes(encoding(plainText),"utf-8")))
    b64Text = b64Text[2:-1]
    encDict = {
        'a': 'q','A': 'M',
        'b': 'w','B': 'N',
        'c': 'e','C': 'B',
        'd': 'r','D': 'V',
        'e': 't','E': 'C',
        'f': 'y','F': 'X',
        'g': 'u','G': 'Z',
        'h': 'i','H': 'L',
        'i': 'o','I': 'K',
        'j': 'p','J': 'J',
        'k': 'a','K': 'H',
        'l': 's','L': 'G',
        'm': 'd','M': 'F',
        'n': 'f','N': 'D',
        'o': 'g','O': 'S',
        'p': 'h','P': 'A',
        'q': 'j','Q': 'P',
        'r': 'k','R': 'O',
        's': 'l','S': 'I',
        't': 'z','T': 'U',
        'u': 'x','U': 'Y',
        'v': 'c','V': 'T',
        'w': 'v','W': 'R',
        'x': 'b','X': 'E',
        'y': 'n','Y': 'W',
        'z': 'm','Z': 'Q',
        '1': '2','2': '3',
        '3': '4','4': '5',
        '5': '6','6': '7',
        '7': '8','8': '9',
        '9': '0','0': '1'
        }
    encText = ""
    for letter in b64Text:
        if letter in encDict:
            encText += encDict[letter]
        else:
            encText += letter
    return encText

def decode(text):
    plainText = ""
    for t in range(len(text)):
        if t % 2 == 0:
            plainText += text[t]
    return plainText

def decrypt(text):
    decDict = {
        'q': 'a','M': 'A',
        'w': 'b','N': 'B',
        'e': 'c','B': 'C',
        'r': 'd','V': 'D',
        't': 'e','C': 'E',
        'y': 'f','X': 'F',
        'u': 'g','Z': 'G',
        'i': 'h','L': 'H',
        'o': 'i','K': 'I',
        'p': 'j','J': 'J',
        'a': 'k','H': 'K',
        's': 'l','G': 'L',
        'd': 'm','F': 'M',
        'f': 'n','D': 'N',
        'g': 'o','S': 'O',
        'h': 'p','A': 'P',
        'j': 'q','P': 'Q',
        'k': 'r','O': 'R',
        'l': 's','I': 'S',
        'z': 't','U': 'T',
        'x': 'u','Y': 'U',
        'c': 'v','T': 'V',
        'v': 'w','R': 'W',
        'b': 'x','E': 'X',
        'n': 'y','W': 'Y',
        'm': 'z','Q': 'Z',
        '0': '9','9': '8',
        '8': '7','7': '6',
        '6': '5','5': '4',
        '4': '3','3': '2',
        '2': '1','1': '0'
    }
    encText = ""
    for letter in text:
        if letter in decDict:
            encText += decDict[letter]
        else:
            encText += letter
    plainText = str(b64decode(bytes(encText,"utf-8")))
    plainText = plainText[2:-1]
    plainText = decode(plainText)
    return plainText

def main():
    plainText = "This is a test string, btw I love her"
    encrypted = encrypt(plainText)
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)

if __name__ == "__main__":
    main()
