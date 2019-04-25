import random
word_bank = ["trunk", "tree", "letter", "spider", "pull", "organize", "concrete", "laptop", "mindful", "charger"]

word = random.choice(word_bank)
guessed_letters = ["'", ]
guesses_left = 8

while guesses_left > 0:
    word_hidden = []
    for letter in word:
        if letter in guessed_letters:
            word_hidden.append(letter)
        else:
            word_hidden.append("*")
    print(word_hidden)
    user_guess = input("Guess a letter")
    guessed_letters.append(user_guess)
    guesses_left -= 1



