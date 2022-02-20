import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for num in range(len(chosen_word)):
    display.append('_')

print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess

print(display)