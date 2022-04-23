"""
.
"""
# _Jayce McMillan_
# This is a population simulator where the success of your population is
# determined by your population start number, the amount of generations
# you input, and the random seed number you provide. The 5 digit seed
# number determines the diseases, triumphs, and game ending scenarios
# your population may or may not experience.
print("Hello! Welcome to my population simulator!", end=' ')
print("In this simulation, you are")
print("able to input your starting population,", end=' ')
print("the number of generations your")
print("society will go through, and a", end=' ')
print("random five digit code that will determine")
print("the diseases, triumphs, and game", end=' ')
print("ending scenarios your population will")
print("endure through their lifetime. Good luck!")
print(" ")
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# This was the website I used to gain a better understanding of end= statements
pop_no = input("Enter Population Start Number: ")
# The while statements prevent the user to input some invalid inputs
while not len(pop_no):
    pop_no = input("Enter Population Start Number: ")
new_pop = 0
# genNo = amount of generations the population will go through
gen_no = input("Enter your Society's Generations: ")
while not len(gen_no):
    gen_no = input("Enter your Society's Generations: ")
seed = input("Enter random 5 digit code: ")
while len(seed) != 5:
    seed = input("Code must be 5 digits: ")
# The seed is just something my code uses as a number to preform operations
# on that determine which predetermined scenario the population will go through
if not int(gen_no):
    print("Your population is ", pop_no, ". Not much progress...", sep='')


# https://www.geeksforgeeks.org/python-sep-parameter-print/
# This was the website I used to gain a better understanding of sep= statements
def defeat_aliens(deaths, kidnapped):
    """

    :param deaths:
    :param kidnapped:
    """
    print("Hooray! Your people killed ", end='')
    print(str(int(deaths * 2.6)) + " of the aliens and")
    print("stole all their fancy equipment!", end='')
    print("You also took " + str(int(kidnapped) - 450))
    print("of their people to conduct scientific research on.")


def lose_to_aliens(deaths, kidnapped):
    """

    :param deaths:
    :param kidnapped:
    """
    print("Uh oh, the aliens killed " + str(
        int(deaths * 5.3)) + " of your people,")
    print(
        "kidnapped " + str(int(kidnapped) + 1523) + " of them, and then left")
    print("out of boredom.")


def alien_execution():
    """
    .
    """
    print("Aliens have invaded your planet! Type the number of weapons")
    weapons = int(input("you would like to use to fight them: "))
    print("Woah! Now they're destroying your buildings!")
    yes_or_no = input("Would you like to surender: ")
    while yes_or_no != "Yes" and yes_or_no != "No":
        yes_or_no = input("Please type the words; Yes or No: ")
    if weapons >= 500 and yes_or_no == "No":
        defeat_aliens(weapons, weapons)
    if weapons >= 500 and yes_or_no == "Yes":
        lose_to_aliens(weapons, weapons)
    if weapons < 500 and yes_or_no == "No":
        lose_to_aliens(weapons, weapons)
    if weapons < 500 and yes_or_no == "Yes":
        lose_to_aliens(weapons, weapons)


# I added some functions to simulate an alien invasion
if int(gen_no) > 0:
    if int(pop_no) <= 1:
        print("Your population was too small to sustain itself.")
    elif int(pop_no) <= 7:
        print("Your society had to inbreed to sustain itself...")
        print("It didn't end well.")
    elif int(pop_no) > 12000000000:
        print("You crammed your world with too many people. Everyone died.")
    else:
        ye_or_no = 1
        huh = 1
        if 8 <= int(pop_no) <= 12000000000:
            if int(seed) % 2 == 0:
                # I used the numeric operation % to differentiate between even
                # and odd numbers.
                new_pop = (int(pop_no) * int(gen_no) ** 2)
            # I used the numeric operators * and ** to simulate rapid
            # population growth.
            if not int(seed) % 2 == 0:
                new_pop = ((int(pop_no) * (
                        int(gen_no) / (2 ** int(gen_no)))) + 100)
                # I used the / operator to simulate game ending
                # diseases.
        if not (int(seed) % 3):
            new_pop = int(new_pop) - 100
        if (int(seed) % 3) == 1:
            new_pop = int(new_pop) // 2
            # I used the numeric operator // to simulate a scenario where
            # approximately half the population dies.
        if (int(seed) % 3) == 2:
            new_pop = int(new_pop) + 100
            # I used the numeric operator + to add 100 people to the population

        if not (int(seed) % 4):
            print("Woah, your population developed birth control!")
            ye_or_no = input("Would you like to mass produce it? Yes or No: ")
            while ye_or_no != "Yes" and ye_or_no != "No":
                ye_or_no = input("Please type the words ; Yes or No: ")
            if ye_or_no == "Yes":
                new_pop = new_pop * 3 / 4
                int(new_pop)
            if ye_or_no == "No":
                new_pop = new_pop * 5 / 4
                int(new_pop)

        if (int(seed) % 4) == 1:
            huh = (int(gen_no)) // 10
            for x in range(huh):
                new_pop += 123

        if (int(seed) % 4) == 2:
            alien_execution()
            # function call
            new_pop += 1000
        if (int(seed) % 4) == 3:
            alien_execution()
            new_pop += 10000
            # function call
        if (int(seed) % 12345) == 0 or (int(seed) % 24680) == 0:
            # I added an or statement
            new_pop = -1

        if int(new_pop) >= int(pop_no) * 10:
            print("Wowie, your society was very successful!")
            if ye_or_no == "No":
                print("Unfortunately, your population contracted")
                print("wide spread STDs.")
            print("Your final population is", str(int(new_pop)) + "!")
            # I used the + string operator to combine a variable and text.
        if int(pop_no) * 1 < int(new_pop) < int(pop_no) * 10:
            print("Your society increased in population!")
            if ye_or_no == "No":
                print("Unfortunately, your population contracted")
                print("high high amounts of STDs.")
            print("Your final population is", str(new_pop) + "!")
        if int(new_pop) < int(pop_no):
            if not (int(seed) % 12345):
                print("Your population got hit with a meteor!", end=' ')
                print("Everyone died.")
            elif int(new_pop) >= 0:
                int(new_pop)
                print("Your population decreased to " + str(int(new_pop))
                      + ".")
            else:
                print("Your population discovered nuclear physics!", end=' ')
                print("However, your society went ")
                print("into nuclear war and destroyed the planet...")
        if int(new_pop) >= 12000000000:
            print("Unfortunately, you overloaded your world with too ")
            print("many people, causing global famine. Everyone died.")
        if int(new_pop) <= 1:
            print("Yikes!")
        elif int(new_pop) <= 15:
            print("That's pretty bad!")
else:
    print("I have no clue what happened. You", end=' ')
    print("broke" * 23)
    # I used the * string operator to say yhe word broke 23 times to
    # tell the user they inputted an "invalid" value.
    print(" ")
    print("..error")
