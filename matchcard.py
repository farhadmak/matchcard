# Match Card Game
# Created by Farhad Makiabady

# References:
# https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/
# https://www.geeksforgeeks.org/clear-screen-python/

import random
from os import system, name

def coordInput():
    # This function takes the user's input for the initial size of the grid
    while True:
        try:
            size = int(input("Please select a size you wish to play (2, 4): "))
            if ((size != 2) and (size != 4)):
                print("Please select 2 or 4")
                continue
            return size
        except ValueError: 
            print("Please select an integer.")
    
def createGrid(size):
    return [["0"] * size for _ in range(size)]

def printGrid(grid):
    for row in grid:
        print(row)

def populateGrid(answerGrid, size):
    # This function populates an answerGrid with the answers to the game
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    selectedCards = random.sample(cards, int(size**2 / 2))
    
    while any("0" in sublist for sublist in answerGrid): # While no "0"s in answerGrid
        randomCard = random.choice(selectedCards)
        if sum(elem.count(randomCard) for elem in answerGrid) < 2: # if count of randomCard is  less than 2
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if answerGrid[y][x] == "0":
                answerGrid[y][x] = randomCard
        else:
            randomCard = random.choice(selectedCards)

def clear(): 
    # This function clears the screen so you do not see your previous play
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def flipCard(grid, answerGrid):
    # This is the sub function of playTurn that handles the coordinates recieved from the user
    while True:
        try:
            x, y = [int(x) for x in input("Coordinates: ").split()]
            if grid[y - 1][x - 1] == "0":
                grid[y - 1][x - 1] = answerGrid[y - 1][x - 1]
                break
            else:
                print("You have previously flipped this card! Try again!")
        except ValueError:
            print("Something isn't right! Try the coordinates again.")
            continue
        except IndexError:
            print("Out of range!")
            continue

    return x, y, grid

def playTurn(grid, answerGrid, score):
    # This function handles the matching of two cards chosen by user
    print("Enter the coordinates of your first card you would like to flip (x y)")
    x1, y1, grid = flipCard(grid, answerGrid)
    printGrid(grid)

    print("Enter the coordinates of your second card you would like to flip (x y)")
    x2, y2, grid = flipCard(grid, answerGrid)
    printGrid(grid)

    if grid[y1 - 1][x1 - 1] == answerGrid[y2 - 1][x2 - 1]:
        print("Yay! You got it!")
        input("Press Enter to continue.")
        clear()
    else:
        print("Whoops! Try again!")
        grid[y1 - 1][x1 - 1] = "0"
        grid[y2 - 1][x2 - 1] = "0"
        input("Press Enter to try again.")
        clear()
    
    score += 1
    return score

def gameOver(grid):
    # Checks if game is over
    if any("0" in sublist for sublist in grid):
        return False
    else:
        return True

def main():
    while True:
        print("Welcome to Match Card!")

        size = coordInput()
        grid = createGrid(size)
        answerGrid = createGrid(size)
        populateGrid(answerGrid, size)
        score = 0
        while not gameOver(grid):
            printGrid(grid)
            score = playTurn(grid, answerGrid, score)
        
        if gameOver(grid):
            print("Your final score is {}!".format(score))
            playAgain = input("Congratz! You won! Would you like to play again? Y/N: ")
            if playAgain == "Y" or playAgain == "y":
                continue
            else:
                print("Thank you for playing, see you around!")
                break

    

main()