alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount, direction):
    end_text = ''
    for letter in plain_text:
        if direction == "encode":
            position = alphabet.index(letter) - ((len(alphabet) - shift_amount))
        elif direction == "decode":
            position = alphabet.index(letter) - shift_amount
        end_text += alphabet[position]
    print(f"The {direction}d text is {end_text}.")   

ceasar(plain_text=text, shift_amount=shift, direction=direction)