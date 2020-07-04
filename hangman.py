import random
import string

def play_game():
    word_list = ["python", "java", "kotlin", "javascript"]
    hidden_word = random.choice(word_list)
    word_set = set(hidden_word)
    open_letters = set()
    tried_letters = set()
    tries = 8
    while tries > 0:
        word = ''
        for l in hidden_word:
            if l in open_letters:
                word += l
            else:
                word += '-'
        print()
        print(word)

        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower() or letter not in string.ascii_letters:
            print("It is not an ASCII lowercase letter")
        elif letter in tried_letters:    
            print("You already typed this letter")
        elif letter in hidden_word:
            open_letters.add(letter)
            tried_letters.add(letter)
            if open_letters == word_set:
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("No such letter in the word")
            tries -= 1
            tried_letters.add(letter)

    else:
        print("You are hanged!")

if __name__ == "__main__":
    while True:
        print("\nH A N G M A N")
        command = ''
        while command not in {"play", "exit"}:
            command = input('Type "play" to play the game, "exit" to quit: ')

        if command == "play":
            play_game()
        else:
            break