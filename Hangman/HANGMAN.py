import random
from words import word_list
from stages import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    # check if the letter exist.
    if guess in display:
        print(f'"{guess}" all ready exists')

    #Check guessed letter.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'"{guess}" not in the word. You have {lives} lives left')
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
