#Name: Santino Viscariello
#Date: 09/21/24
#Course: CINF308-Programming for Informatics


# This porgram will accept user input and uses lists.
# It will have a list of current available items in the output.
# It can take the input for the item and put it into a 
# separate “used” list.
# Has a quit and start option as well as at 
# least one other way of manipulating the data.

# Import random to the code.
import random

# The list of words provided.
words = ["computer", "science", "programming", "mathematics", "player"]

# The following recent items provided.
recent_items = ["potato", "carrot", "celery", "tomato", "mushroom"]

# The welcome message for the game.
print("Welcome to the word guessing game!")

#Shows items used recently.
print("Recent available items: ", recent_items)

used_items = []

# The list of choices featured.
while True:
    print("\nChose the follwing:")
    print("1. Start game")
    print("2. Pick an item")
    print("3. Show the used items")
    print("4. Restart")
    print("5. Exit")

    # Inputs the following choices in the game.
    choice = input("Select from 1 to 5: ")

    # Choice #1 choses a random word 
    if choice == "1":
        word = random.choice(words)
        guessed = "_" * len(word)
        attempts = 10
        guessed_letters = []

        print(f"Guess the word: {guessed}")

        while attempts > 0 and "_" in guessed:
            # Prompt the user to guess a letter
            guess = input("Enter a letter: ").lower()

            # Check if the letter has already been guessed
            if guess in guessed_letters:
                print("You have already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            # Check if the guessed letter is in the word
            if guess in word:
                
                # Update the guessed word
                guessed = "".join(
                    [
                        letter if letter == guess or letter in guessed_letters else "_"
                        for letter in word
                    ]
                )
                print(f"Good guess! Current word: {guessed}")
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")

        # Check if the game has been won or lost
        if "_" not in guessed:
            print(f"Congratulations! You've guessed the word: {word}")
        else:
            print(f"Sorry, you ran out of attempts. The word was: {word}")

    # Choice #2 show's the items the are recently available.
    elif choice == "2":
        print("Items recently available:", recent_items)
        item = input("Enter the name of the item provided: ").lower()

        if item in recent_items:
            recent_items.remove(item)
            used_items.append(item)
            print(f"You have used this item: {item}")
        else:
            print("Item unavailable.")

    # Choice #3 show's the items already used.
    elif choice == "3":
        print("Used items:", used_items)

    # Choice #4 shows the  program starting over.
    elif choice == "4":
        print("Starting over.")
        used_items.clear()
        recent_items = ["potato", "carrot", "celery", "tomato", "mushroom"]

    # Choice # 5 show's the closing message after 
    #playing the game.
    elif choice == "5":
        print("Thanks for playing!")
        break
    #A meesage if chose somthing not part of
    #choices shown. 
    else:
        print("Invalid choice. Try again.")
