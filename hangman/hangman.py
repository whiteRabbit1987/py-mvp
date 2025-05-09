# Python hangman game

from word_list import words_with_hints, update_display, hangman
import random

guesses = 6
word, hint = random.choice(list(words_with_hints.items()))

def main():
    global guesses
    print(f"**************************\n"
        f"Welcome to python hangman!"
        f"\n**************************\n"
        f"Hint: {hint}")

    display = ['_' for _ in word]
    print(" ".join(display))

    is_running = True
    while is_running:
        guess = input("\nEnter your guess"
                    f"\n**************************\n: ").lower()
        guesses -= 1

        display = update_display(word, display, guess)
        print(" ".join(display))

        if guesses < 0:
            print("Game Over!")
            break
        elif guess == word:
            print("You win!")
            is_running = False
        elif guess not in word or guess != word:
            for _ in hangman[guesses]:
                print(_)


if __name__ == '__main__':
    main()