word = "tabernacle"
guess = ""
cont = 0
print("Welcome to the word guessing game!\n")

while guess.lower() != word:
    guess = input("What is your guess? ")
    cont +=1
    if guess.lower() != word:
        print("Your guess is not correct!")
    else:
        print("Congratulations! You guessed it")
        print(f"It toook you: {cont} guesses")