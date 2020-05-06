# A single file for all the PracticePython.org challenges
# Uncomment each function to see the results of the challenge

# Challenge 01 Character Input
def character_input():
    """This Challenge asks for a user's name, age, and a number of copies to be printed."""

    import datetime

    current_year = datetime.datetime.now().year
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))
    number_of_copies = int(input("How many copies do you wanted printed? "))
    print(
        f"\nHello {user_name}. You are {user_age}. You will turn 100 in the year {current_year + 100 - user_age}"
        * number_of_copies
    )


# character_input()


# Challenge 02 Odd Or Even
def odd_or_even():
    """
    This challange accepts 2 numbers from the user. The first is any number.
    The second is checked to see if it can be divided evenly into the first.
    """

    def division_check(num, check):
        if num % check == 0:
            return "Congratulations, your number divides evenly."
        return "Sorry, it does not divide evenly."

    num = int(input("Enter a number that you wanted divided: "))
    check = int(input("Enter a second number that will be divided into the first: "))

    print(division_check(num, check))


# odd_or_even()


# Challenge 03 List Less Than Ten
def list_less_than_ten():
    """
    This challenge is to take a list of numbers and print out a new list of all the
    integers that are less than the user's chosen number. Try to do it in one line
    if possible.
    """

    def less_than_five(input_list, user_number):
        return f"Your new list is {[number for number in input_list if number < user_number]}"

    list_of_numbers = [1, 4, 2, 6, 12, 29, 5, 12, 2, 1, 6, 23]
    print(f"The list of numbers is: {list_of_numbers}")
    user_number = int(
        input("Pick a number to show all the integers that are less than it. ")
    )

    print(less_than_five(list_of_numbers, user_number))


# list_less_than_ten()


# Challenge 04 Divisors
def divisors():
    """This challenge is to print out all the divisors of a chosen number."""

    def divisors(num):
        divisor_list = []
        for check in range(2, num):
            if num % check == 0:
                print(check)
                divisor_list.append(check)
        return divisor_list

    chosen_number = int(input("Chose a number to see all the divisors for it. "))
    print(divisors(chosen_number))


# divisors()


# Callenge 05 List Overlap
def list_overlap():
    """
    This challenge is to return a list with all the elements that
    are inside two different lists. For an additional challenge,
    write this in one line or using two randomly generated lists.
    """

    from random import randint

    random_list_one = [randint(1, 20) for num in range(10)]
    random_list_two = [randint(1, 20) for num in range(10)]
    unique_list = list({num for num in random_list_one if num in random_list_two})
    print(f"List one is: {random_list_one}")
    print(f"List two is: {random_list_two}")
    print(f"The list overlap is: {unique_list}")


# list_overlap()


# Challenge 06 String Lists
def string_lists():
    """This challange asks the user for a string and checks if it's a palindrome."""

    user_string = input("Enter a string and I'll check if it's a palindrome. ")
    if user_string[0:] == user_string[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome")


# string_lists()


# Challenge 07 List Comprehensions
def list_comprehensions():
    """
    Take a list and return a new list with only the even
    elements in it. Do it in a single line of code.
    """

    user_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([num for num in user_list if num % 2 == 0])


# list_comprehensions()


# Challenge 08 Rock Paper Scissors
def rock_paper_scissors():
    """Ask two different players to participate in a rock paper scissors game."""

    def game_loop():
        p1_choice = ""
        while p1_choice != "rock" and p1_choice != "paper" and p1_choice != "scissors":
            p1_choice = input("Player 1. Choose rock paper or scissors: ")

        p2_choice = ""
        while p2_choice != "rock" and p2_choice != "paper" and p2_choice != "scissors":
            p2_choice = input("Player 2. Choose rock paper or scissors: ")

        if p1_choice == "rock" and p2_choice == "rock":
            print("It's a tie.")
        elif p1_choice == "rock" and p2_choice == "paper":
            print("Player 2 wins.")
        elif p1_choice == "rock" and p2_choice == "scissors":
            print("Player 1 wins.")
        elif p1_choice == "paper" and p2_choice == "paper":
            print("It's a tie.")
        elif p1_choice == "paper" and p2_choice == "scissors":
            print("Player 2 wins.")
        elif p1_choice == "paper" and p2_choice == "rock":
            print("player 1 wins.")
        elif p1_choice == "scissors" and p2_choice == "scissors":
            print("It's a tie.")
        elif p1_choice == "scissors" and p2_choice == "rock":
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")

    another_game = ""
    while another_game == "y":
        game_loop()
        another_game = input("Would you like to player again? y/n ")


# rock_paper_scissors()


# Challenge 09 Guessing Game One
def guessing_game():
    """
    This challenge is to create a random number between 1 and 9, then
    tell the user if they are too high or too low after each guess.
    """

    from random import randint

    random_number = randint(1, 9)
    user_guess = 0
    count = 0

    while random_number != user_guess:
        print("Pick a number between 1 and 9.")
        user_guess = int(input("Number: "))
        if user_guess > random_number:
            print("Your number is too high.")
        elif user_guess < random_number:
            print("Your number is too low.")
        else:
            print("You guessed correctly.")
        count += 1

    print(f"You guessed {count} times.")


# guessing_game()


# Challenge 10 List Overlap Comprehensions
def list_overlap_comprehensions():
    """
    This challenge is to take two lists and return only the elements that
    are common between the two list, without duplicates. Try to write it
    in one line and with randomly generated lists.
    """

    from random import sample

    list_one = sample(range(20), 10)
    list_two = sample(range(20), 15)
    common_elements = list({num for num in list_one if num not in list_two})
    print(
        f"List one: {list_one}\nList Two: {list_two}\nCommon elements: {common_elements}"
    )


# list_overlap_comprehensions()


# Challenge 11 Check Primality Functions
def check_primality_functions():
    """Ask a user for a number and check if it is prime"""

    number_to_check = int(input("Give me a number and I'll check if it is prime: "))
    for num in range(2, number_to_check):
        if number_to_check % num == 0:
            print("Your number is not prime.")
            break
    print("It is a prime number")


# check_primality_functions()


# Challenge 12 List Ends
def list_ends():
    """
    This challenge is to write a function that takes a list of numbers and
    makes a new list with only the first and last elements of the original list
    """

    original_list = [5, 10, 15, 20, 25]

    def first_and_last(input_list):
        return [input_list[0], input_list[-1]]

    print(first_and_last(original_list))


# list_ends()


# Challenge 13 Fibonacci
def fibonacci():
    """
    This challenge is to ask a user for a number,
    then generate that many Fibonacci numbers
    """

    def fib(num):
        if num <= 2:
            return 1
        num = num - 1
        if len(fib_list) > 1:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib(num)

    fib_list = [1, 1]
    num = int(input("How many Fibonacci numbers do you want me to generate? "))
    fib(num)
    print(fib_list)


# fibonacci()


# Challenge 14 List Remove Duplicates
def list_remove_duplicates():
    """
    Write a program that takes a list and return it with all the duplicates removed.
    Write two different functions. One using a loop and another using sets.
    """

    def remove_with_loop(list_a, list_b):
        new_list = []
        for num in list_a:
            if num in list_b:
                new_list.append(num)
        return list(set(new_list))

    def remove_with_sets(list_a, list_b):
        new_list = {num for num in list_a if num in list_b}
        return list(new_list)

    list_a = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    list_b = [2, 3, 6, 7, 8, 9]

    print(remove_with_sets(list_a, list_b))
    print(remove_with_loop(list_a, list_b))


# list_remove_duplicates()


# Challenge 15 Reverse Word Order
def reverse_word_order():
    """This challenge is to reverse the order of a user's string"""

    user_string = input("Write a sentence and I will reverse the order. ")
    string_two = user_string.split(" ")
    final_string = []
    while len(string_two) > 0:
        final_string.append(string_two.pop())
    print(" ".join(final_string))


# reverse_word_order()


# Challenge 16 Password Generator
def password_generator():
    """
    This challenge is to generate a password every time a user asks for one.
    Make the password strong or week depending on the user's preference.
    """

    from random import choice, randint

    list_of_symbols = ["!", ".", "?", "@", "#", "$", "%", "&"]
    list_of_words = [
        "accept",
        "admit",
        "against",
        "among",
        "check",
        "child",
        "choice",
        "eight",
        "end",
        "energy",
        "glass",
        "green",
        "ground",
        "hand",
    ]

    print("This program will generate a password for you.")
    if input("Would you like a strong password? y/n ") == "y":
        print("strong")
        new_password = (
            choice(list_of_symbols)
            + str(randint(0, 9))
            + choice(list_of_words)
            + choice(list_of_symbols)
            + choice(list_of_symbols)
            + str(randint(0, 9))
            + choice(list_of_words).capitalize()
            + str(randint(0, 9))
            + choice(list_of_symbols)
        )
        print(f"Your strong password is: {new_password}")
    else:
        print(f"Your weak password is: {choice(list_of_words)}{choice(list_of_words)}")


# password_generator()


# Challenge 17 Decode A Web Page
def decode_a_web_page():
    """
    This challenge is to print out a list of all the
    headlines from the White House Briefings web page.
    """

    import requests
    from bs4 import BeautifulSoup

    r = requests.get("https://www.whitehouse.gov/briefings-statements/")
    soup = BeautifulSoup(r.text, "html.parser")
    for headline in soup.find_all("h2"):
        print(headline.get_text())


# decode_a_web_page()


# Challenge 18 Cows And Bulls
def cows_and_bulls():
    """This challenge is to create the Cows and Bulls game"""

    from random import randint

    game_number = str(randint(1000, 9999))
    player_guess = "0000"

    def game_loop():
        cows = 0
        bulls = 0

        for index, num in enumerate(player_guess):
            if num == game_number[index]:
                bulls += 1
            elif num in game_number:
                cows += 1

        print(f"You have {cows} cows and {bulls} bulls.")

    while player_guess != game_number:
        player_guess = input("Guess a four digit number: ")
        game_loop()

    print("Congratulations, you win!")


# cows_and_bulls()


# Challenge 19 Decode A Web Page Two
def decode_a_web_page_two():
    """This challenge is to print the entire text of a webpage"""

    import requests
    from bs4 import BeautifulSoup

    r = requests.get(
        "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    )
    soup = BeautifulSoup(r.text, "html.parser")
    for paragraph in soup("p")[3:-6]:
        print(paragraph.text)


# decode_a_web_page_two()


# Challenge 20 Element Search
def element_search():
    """
    This challenge is to take an ordered list and an additional
    number and returns a boolean if the number is inside the list.
    For an extra challenge, use binary search.
    """

    def binary_search_list(ordered_list, search_number):
        while len(ordered_list) > 1:
            middle_index = len(ordered_list) // 2
            if search_number < ordered_list[middle_index]:
                ordered_list = ordered_list[:middle_index]
            else:
                ordered_list = ordered_list[middle_index:]

        return True if search_number in ordered_list else False

    ordered_list = list(range(1, 101, 2))
    search_number = 67

    print(True if search_number in ordered_list else False)
    print(binary_search_list(ordered_list, search_number))


# element_search()


# Challenge 21 Write To A File
def write_to_a_file():
    """
    This challenge is to take HTML text and write it to a file.
    Let the user pick the file name for an extra challenge.
    """

    import requests
    from bs4 import BeautifulSoup

    r = requests.get("https://www.whitehouse.gov/briefings-statements/")
    soup = BeautifulSoup(r.text, "html.parser")

    file_name = input(
        "Please name the file that you would like the "
        "White House briefing headlines saved to. "
    )

    with open(f"{file_name}.txt", "w") as open_file:
        for headline in soup.find_all("h2"):
            open_file.write(f"{headline.get_text()}\n")


# write_to_a_file()


# Challenge 22 Read From A File
def read_from_a_file():
    """
    This challenge is to read from a file (sun_file.txt) and count
    how many of each "category" of each image there are.
    """

    with open(f"sun_file.txt", "r") as open_file:
        count_dictionary = {}
        for line in open_file.readlines():
            word = line.split("/")[2]
            if word not in count_dictionary:
                count_dictionary[word] = 1
            else:
                count_dictionary[word] += 1

        for count in count_dictionary.items():
            print(f"{count[0]}: {count[1]}")


# read_from_a_file()


# Challenge 23 File Overlap
def file_overlap():
    """
    This challenge is to take two text files and
    find the numbers that overlap between them.
    """

    def return_list_from_file(file):
        return_list = []
        with open(file) as open_file:
            for line in open_file.readlines():
                return_list.append(int(line))

        return return_list

    primes = return_list_from_file("primenumbers.txt")
    happy_numbers = return_list_from_file("happynumbers.txt")

    print([num for num in happy_numbers if num in primes])


# file_overlap()


# Challenge 24 Draw A Game Board
def draw_a_game_board():
    """This challenge is to draw a game board that is sized to the user's input."""

    board_size = int(input("What size game board would you like? "))
    print(" ---" * board_size)
    for _ in range(board_size):
        print(f"|{'   |' * board_size}\n{' ---' * board_size}")


# draw_a_game_board()


# Challenge 25 Guessing Game Two
def guessing_game_two():
    """
    This challenge is to have the computer guess a secret number
    between 1 and 100. Afterward, the computer will tell the user
    how many guesses it took to achieve this.
    """

    print(
        """
    Pick a number between 1 and 100. I am going to
    guess what it is. You tell me if my guess is
    higher or lower than your number.
    """
    )

    guess_count = 1
    guess_range = list(range(1, 101))
    correct_guess = False

    while correct_guess != True:
        middle_index = len(guess_range) // 2
        answer = input(f"Is you number {guess_range[middle_index]}? (y/n) ")
        if answer == "y":
            correct_guess = True
            break

        higher_or_lower = input("Is it higher or lower? (higher/lower) ")
        if higher_or_lower == "higher":
            guess_range = guess_range[middle_index:]
        else:
            guess_range = guess_range[:middle_index]

        guess_count += 1

    print(f"It took {guess_count} guesses to guess your number. Thank you for playing.")


# guessing_game_two()


# Challenge 26 Check Tic Tac Toe
def check_tic_tac_toe():
    """
    This challenge is to take a list of lists that represents
    a tic-tac-toe board and check who has won the game.
    """

    def check_winner(board):
        def player_check(player):
            if player == 0:
                return "It's a tie"
            return f"Player {player} wins"

        for row in board:
            if len(set(row)) == 1:
                return player_check(row[0])

        for i in range(0, 3):
            if board[0][i] == board[1][i] == board[2][i]:
                return player_check(board[0][i])

        if board[0][0] == board[1][1] == board[2][2]:
            return player_check(board[0][0])
        if board[0][2] == board[1][1] == board[2][0]:
            return player_check(board[0][2])

    board = [[2, 0, 2], [2, 1, 0], [2, 1, 1]]
    print(check_winner(board))


# check_tic_tac_toe()


# Challenge 27 Tic Tac Toe Draw
def tic_tac_toe_draw():
    """This challenge is to have a player input coordinates into a
    tic-tac-toe game and have the result printed out in the terminal.
    """

    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    game_running = True
    player = "X"

    while game_running == True:
        valid_choice = False

        for row in game_board:
            print(row)

        while valid_choice == False:
            player_choice = input(
                f"Player {player} choose coordinates for a square. (e.g. 1, 3) "
            )
            coords = player_choice.split(", ")
            if game_board[int(coords[0]) - 1][int(coords[1]) - 1] == " ":
                valid_choice = True
            else:
                print("Sorry, that square is already taken.")

        game_board[int(coords[0]) - 1][int(coords[1]) - 1] = player
        player = "O" if player == "X" else "X"
        game_running = " " in [item for sublist in game_board for item in sublist]


# tic_tac_toe_draw()


# Challenge 28 Max Of Three
def max_of_three():
    """This challenge is to take 3 numbers and returns the maximum of them"""

    def find_max(num_1, num_2, num_3):
        return sorted([num_1, num_2, num_3])[-1]

    print(find_max(1, 10, 8))


# max_of_three()

# Challenge 29 Tic Tac Toe Game
def tic_tac_toe_game():
    """This challenge is to make a Tic-Tac-Toe game"""

    pass


tic_tac_toe_game()


# Challenge 30 Pick Word
def pick_word():
    """This challenge is to pick a random word from an external file."""

    from random import choice

    with open("sowpods.txt") as open_file:
        lines = open_file.readlines()
        print(choice(lines).strip())


# pick_word()


# Challenge 31 Guess Letters
def guess_letters():
    """
    This challenge is to display the characters of a secret
    word that have been guessed correctly by the player
    """

    secret_word = "EVAPORATE"
    print("Welcome to Hangman!")
    playing = True
    guessed = []

    while playing == True:
        word_as_list = [letter if letter in guessed else "_" for letter in secret_word]
        display = ""
        for letter in word_as_list:
            display += f"{letter} "
        print(display)

        guess = input("Guess your letter: ").upper()
        while guess in guessed:
            print("Sorry, you have already guessed that letter.")
            guess = input("Guess your letter: ").upper()

        if guess not in secret_word:
            print("incorrect")
        else:
            print("correct")
            guessed.append(guess)

        playing = False
        for letter in secret_word:
            if letter not in guessed:
                playing = True

    print("Congratulations, You win!")


# guess_letters()


# Challenge 32 Hangman
def hangman():
    """This challenge is to make the game of Hangman."""

    import pics
    from random import choice

    continue_playing = "y"

    while continue_playing == "y":

        def random_word():
            with open("sowpods.txt") as open_file:
                lines = open_file.readlines()
                return choice(lines).strip()

        secret_word = random_word()
        print("Welcome to Hangman")
        game = True
        guessed = []
        display = ""
        turns_left = 6

        while game == True:
            word_as_list = [
                letter if letter in guessed else "_" for letter in secret_word
            ]
            display = ""
            for letter in word_as_list:
                display += f"{letter} "

            print(pics.pics[-turns_left - 1])
            print(f"\n{display}")
            print(f"You have {turns_left} turns left.")

            guess = input("Guess your letter: ").upper()
            while guess in guessed:
                print("Sorry, you have already guessed that letter.")
                guess = input("Guess your letter: ").upper()

            if guess not in secret_word:
                guessed.append(guess)
                turns_left -= 1
                if turns_left <= 0:
                    break
            else:
                guessed.append(guess)

            game = False
            for letter in secret_word:
                if letter not in guessed:
                    game = True

        if turns_left <= 0:
            print(pics.pics[6])
            print("Sorry, you lose.")
            print(f"The word was {secret_word}")
        else:
            print(f"The word was {secret_word}")
            print("Congratulations, You win!")

        while True:
            continue_playing = input("Would you like to play again? y/n ")
            if continue_playing == "y" or continue_playing == "n":
                break
            else:
                continue


# hangman()


# Challenge 33 Birthday Dictionaries
def birthday_dictionaries():
    """This challenge is to display the birthday of a name that the user chooses."""

    birthday_dictionary = {
        "Benjamin Franklink": "17/01/1706",
        "George Washington": "22/01/1732",
        "Ronald Reagan": "06/02/1911",
        "John Adams": "30/10/1735",
        "Thomas Jefferson": "13/04/1743",
    }

    print("Welcome to the presidential birthday dictionary. We know the birthdays of:")
    for name in birthday_dictionary.keys():
        print(name)

    name_choice = ""
    while name_choice not in birthday_dictionary.keys():
        name_choice = input("Whose birthday do you want us to display?\n")
        if name_choice not in birthday_dictionary.keys():
            print("Sorry, that is not a valid choice.")
    print(f"{name_choice} was born on {birthday_dictionary[name_choice]}.")


# birthday_dictionaries()


# Challenge 34 Birthday JSON
def birthday_json():
    """
    This challenge is to read birthdays from a JSON file and ask the user
    to choose one. For a bonus, allow the user to add more birthdays to the file.
    """

    import json

    with open("birthdays.txt") as open_file:
        birthday_dictionary = json.load(open_file)

    print("Welcome to the presidential birthday dictionary. We know the birthdays of:")
    for name in birthday_dictionary.keys():
        print(name)

    name_choice = ""
    while name_choice not in birthday_dictionary.keys():
        name_choice = input("Whose birthday do you want us to display?\n")
        if name_choice not in birthday_dictionary.keys():
            print("Sorry, that is not a valid choice.")
    print(f"{name_choice} was born on {birthday_dictionary[name_choice]}.")

    confirm = input("Would you like to add a name to the list? y/n\n")
    if confirm == "y":
        name = input("What is the person's name?\n")
        birthday = input("What is the person's birthday?\n")
        birthday_dictionary.update({name: birthday})

        with open("birthdays.txt", "w") as open_file:
            json.dump(birthday_dictionary, open_file, indent=4)


# birthday_json()


## Challenge 35 Birthday Months
def birthday_months():
    """
    This challenge is to read birthdays from a txt file. Then
    count how many birthdays appear in each month of the year.
    """

    import json
    from collections import Counter

    month_table = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    with open("birthdays.txt") as open_file:
        data = json.load(open_file)

    month_list = [month[3:5] for month in data.values()]
    print(Counter([month_table[month] for month in month_list]))


# birthday_months()


# Challenge 36 Birthday Plots
def birthday_plots():
    """
    This challenge is to read birthdays from
    a JSON file and plot them using Bokeh
    """

    import json
    from collections import Counter
    from bokeh.plotting import figure, show, output_file

    month_table = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    with open("date_dictionary.txt") as open_file:
        data = json.load(open_file)

    month_list = [month.split("/")[1] for month in data.values()]
    counted_list = Counter([month_table[month] for month in month_list])

    x = [month for month in counted_list.keys()]
    y = [count for count in counted_list.values()]
    x_categories = x
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.7)
    show(p)


# birthday_plots()
