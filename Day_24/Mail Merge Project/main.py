
with open("./Input/Names/invited_names.txt") as guest_list_file:
    for guest in guest_list_file.readlines():
        print(guest)
        guest.replace('\n', '')
        print(guest)
        with open("./Input/Letters/starting_letter.txt") as template_file:
            with open(f"./Output/ReadyToSend/letter_for_{guest.strip()}.txt", mode="w") as final_letter_file:
                final_letter_file.write(template_file.read().replace("[name]", guest.strip()))

