alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt ( direction, text, shift ):
    encoded_text = ''
    for letter_index in range(0, len( text )):
        letter_index_on_alphabet = alphabet.index(text[letter_index])
        
        if direction == "encode":
            enconded_letter_index = (letter_index_on_alphabet + shift) % 26
        else:
            enconded_letter_index = (letter_index_on_alphabet - shift) % 26

        encoded_letter = alphabet[enconded_letter_index]

        encoded_text += encoded_letter
        
    print( encoded_text )

encrypt(direction=direction, text=text, shift=shift)