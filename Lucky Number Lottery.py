from random import *

def intro():
    print("Welcome to the lottery!")
    print("Pick three numbers from 1 to 10.")
    print("If one number matches, you get half your money back.")
    print("If two numbers match, you get double your money back.")
    print("If all three numbers match, you get 5 times your money.")
    print("The order of the numbers matter!")
    print("")

def lottery():
    currentMoney = 10.00

    def amountBid():
        print("You currently have {}$".format(round(currentMoney, 2)))
        amount = input("How much do you want to bid? ")
        print("")
        while amount.isalpha() == True or float(amount) > currentMoney:
            print("Not a valid number or you don't have that much.")
            amount = input("How much do you want to bid? ")
            print("")
        return float(amount)
             
    def luckyNumberOne():
        luckyNumber = randint(1, 10)
        return luckyNumber

    def luckyNumberTwo():
        luckyNumber = randint(1, 10)
        return luckyNumber

    def luckyNumberThree():
        luckyNumber = randint(1, 10)
        return luckyNumber

    def userGuessOne():
        guess = input("What is the first number? ")
        print("")
        while guess.isalpha() == True or int(guess) > 10 or int(guess) < 1:
            print("Pick a number from 1 to 10!")
            guess = input("What is the first number? ")
            print("")
        return int(guess)
    
    def userGuessTwo():
        guess = input("What is the second number? ")
        print("")
        while guess.isalpha() == True or int(guess) > 10 or int(guess) < 1:
            print("Pick a number from 1 to 10!")
            guess = input("What is the second number? ")
            print("")
        return int(guess)
    
    def userGuessThree():
        guess = input("What is the third number? ")
        print("")
        while guess.isalpha() == True or int(guess) > 10 or int(guess) < 1:
            print("Pick a number from 1 to 10!")
            guess = input("What is the third number? ")
            print("")
        return int(guess)
    
    def guessOneChecker(luckyOne, firstGuess):
        return luckyOne == firstGuess

    def guessTwoChecker(luckyTwo, secondGuess):
        return luckyTwo == secondGuess

    def guessThreeChecker(luckyThree, thirdGuess):
        return luckyThree == thirdGuess

    def moneyMulti(amount):
        multi = 0
        if oneCorrect == True:
            multi += 1
        if twoCorrect == True:
            multi += 1
        if threeCorrect == True:
            multi += 1
        if multi == 1:
            return amount / 2
        if multi == 2:
            return amount * 2
        if multi == 3:
            return amount * 5
        if multi == 0:
            return 0

    def playAgain(choice = False):
        choice = input("Keep playing? Enter Yes or No. ")
        while choice != "Yes" or choice != "No":
            if choice == "Yes":
                return choice == "Yes"
            if choice == "No":
                break
            choice = input("Keep playing? Enter Yes or No. ")

    #Activates Functions
    amount = amountBid()
    currentMoney -= amount
    print("You now have {}$.".format(currentMoney))
    luckyOne = luckyNumberOne()
    luckyTwo = luckyNumberTwo()
    luckyThree = luckyNumberThree()
    firstGuess = userGuessOne()
    secondGuess = userGuessTwo()
    thirdGuess = userGuessThree()
    oneCorrect = guessOneChecker(luckyOne, firstGuess)
    twoCorrect = guessTwoChecker(luckyTwo, secondGuess)
    threeCorrect = guessThreeChecker(luckyThree, thirdGuess)
    print("Lucky numbers: {}, {}, {}".format(luckyOne, luckyTwo, luckyThree))
    print("User guesses: {}, {}, {}".format(firstGuess, secondGuess, thirdGuess))
    print("Matches: {}, {}, {}".format(oneCorrect, twoCorrect, threeCorrect))
    currentMoney = currentMoney + moneyMulti(amount)
    print("You now have {}$.".format(round(currentMoney, 2)))
    choice = playAgain()
    while choice == True:
        if currentMoney == 0:
            print("You ran out of money! Better luck next time!")
            break
        
        amount = amountBid()
        currentMoney -= amount
        print("You now have {}$.".format(round(currentMoney, 2)))
        luckyOne = luckyNumberOne()
        luckyTwo = luckyNumberTwo()
        luckyThree = luckyNumberThree()
        firstGuess = userGuessOne()
        secondGuess = userGuessTwo()
        thirdGuess = userGuessThree()
        oneCorrect = guessOneChecker(luckyOne, firstGuess)
        twoCorrect = guessTwoChecker(luckyTwo, secondGuess)
        threeCorrect = guessThreeChecker(luckyThree, thirdGuess)
        print("Lucky numbers: {}, {}, {}".format(luckyOne, luckyTwo, luckyThree))
        print("User guesses: {}, {}, {}".format(firstGuess, secondGuess, thirdGuess))
        print("Matches: {}, {}, {}".format(oneCorrect, twoCorrect, threeCorrect))
        currentMoney = currentMoney + moneyMulti(amount)
        print("You now have {}$.".format(round(currentMoney, 2)))
        choice = playAgain()
        

intro()
lottery()
    
    
