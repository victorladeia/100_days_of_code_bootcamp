alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt ( direction, text, shift ):
    encoded_text = ''
    for letter_index in range(0, len( text )):
        if text[ letter_index ] in alphabet:
            letter_index_on_alphabet = alphabet.index(text[letter_index])
            
            if direction == "encode":
                enconded_letter_index = (letter_index_on_alphabet + shift) % 26
            else:
                enconded_letter_index = (letter_index_on_alphabet - shift) % 26

            encoded_letter = alphabet[enconded_letter_index]

            encoded_text += encoded_letter
        else:
            encoded_text += text[ letter_index ]
        
    print( encoded_text )


keep_game = True

while keep_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ['encode','decode']:
        direction = input("I couldn't identiy your answer. Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt(direction=direction, text=text, shift=shift)

    user_answer = input ( "Type 'yes' if you want to go again. Ohteriwse type 'no'. " ).lower()
    while user_answer not in ['yes','no']:
        user_answer = input ( "I couldn't identiy your answer. Type 'yes' if you want to go again. Ohteriwse type 'no'. " ).lower()

    if user_answer == 'no':
        keep_game = False