import random
pet_list = ['dog', 'cat', 'mouse', 'camel', 'horse']
chosen_word = random.choice(pet_list)
print(chosen_word)
end_of_game = False
lives = 6
display = []
for letter in chosen_word:
    display += "_"
    str_display = ' '.join([str(elem) for elem in display])
print(str_display)


while not end_of_game:
    guess = input("Guess a letter: \n ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Your guessed letter '{guess}' is not in the word  you lost one life:(")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")