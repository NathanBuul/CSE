import random
print(random.randint(0, 10))
guesses = 5
playing = True
while guesses > 0 and playing:
    guesses = int(input("Take a guess"))
    print("guess is high")
    guesses -= 1
    print("guess is too low")
    guesses -= 1
    print("you got it")
    guesses -= 5
