import random
import time

print("Welcome to HangMan Game play!")
name = input("Enter your name please: ")
print("Hello {}; Best of luck!".format(name))

time.sleep(2)
print("This game is about to start! Be ready to play")
time.sleep(3)


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "-" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_in_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_in_loop()

    elif count != limit:
        hangman()


def play_in_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ['y', 'n', 'Y', 'N', 'yes', 'no', 'Yes', 'No', 'YES', 'NO']:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game in ['y', 'Y', 'yes', 'Yes', 'YES']:
        game()
    else:
        print("Thanks for playing! We expect you back again.")
        exit()


def game():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]

    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '-' * length
    already_guessed = []
    play_game = ""


game()
hangman()
