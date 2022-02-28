alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount, direction):
        
        if (direction == 'encode'):
            cipher_text = ""
            for letter in plain_text:
                new_letter = alphabet[alphabet.index(letter) - ((len(alphabet) - shift_amount))]
                cipher_text += new_letter
            print(f"The encoded text is {cipher_text}.")
        else:
            deciphered_text = ""
            for letter in plain_text:
                new_letter = alphabet[alphabet.index(letter) - shift_amount]
                deciphered_text += new_letter
            print(f"The decodes text is {deciphered_text}")

ceasar(plain_text=text, shift_amount=shift, direction=direction)