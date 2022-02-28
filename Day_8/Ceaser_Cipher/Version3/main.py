import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount, direction):
    shift_amount = shift_amount % len(alphabet)
    end_text = ''
    for char in plain_text:
        if char in alphabet:
            if direction == "encode":
                position = alphabet.index(char) - ((len(alphabet) - shift_amount))
            elif direction == "decode":
                position = alphabet.index(char) - shift_amount
            end_text += alphabet[position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}.")   

ceasar(plain_text=text, shift_amount=shift, direction=direction)

work = True

while(work):
    keep_working = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if keep_working == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceasar(plain_text=text, shift_amount=shift, direction=direction)
    elif keep_working == 'no':
        work = False
        print("Goodbye!")