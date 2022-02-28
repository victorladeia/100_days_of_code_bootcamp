from xml.etree.ElementTree import tostring


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Encrypting Function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        new_letter = alphabet[alphabet.index(letter) - ((len(alphabet) - shift_amount))]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}.")

#Decrypting Function
def decrypt(plain_text, shift_amount):
    deciphered_text = ""
    for letter in plain_text:
        new_letter = alphabet[alphabet.index(letter) - shift_amount]
        deciphered_text += new_letter
    print(f"The decodes text is {deciphered_text}")

if (direction == 'encode'):
    encrypt(text, shift)
else:
    decrypt(text, shift)