alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type yeh shift number:\n"))

def encrypt(text, shift):
    cipher = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher += new_letter

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        plain_text = alphabet[new_position]

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)






