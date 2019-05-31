#!/usr/bin/env python3
# Created by Farhad Makiabady
# https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/
# https://www.geeksforgeeks.org/clear-screen-python/

import random
from os import system, name

def coordInput():
    size = int(input("Please select a size you wish to play (2, 4 or 6): "))
    return size

def createGrid(size):
    return [["0"] * size for _ in range(size)]

def printGrid(grid):
    for row in grid:
        print(row)

def populateGrid(answerGrid, size):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    selectedCards = random.sample(cards, int(size**2 / 2))
    # answerGrid = createGrid(size)
    
    while any("0" in sublist for sublist in answerGrid):
        randomCard = random.choice(selectedCards)
        if sum(elem.count(randomCard) for elem in answerGrid) < 2:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if answerGrid[y][x] == "0":
                answerGrid[y][x] = randomCard
        else:
            randomCard = random.choice(selectedCards)

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def playTurn(grid, answerGrid):
    x1, y1 = [int(x) for x in input("Enter the coordinates of the first card you would like to flip (x, y): ").split()]
    # print(answerGrid[y1 - 1][x1 - 1])
    grid[y1 - 1][x1 - 1] = answerGrid[y1 - 1][x1 - 1]
    printGrid(grid)

    x2, y2 = [int(x) for x in input("Enter the coordinates of the second card you would like to flip (x, y): ").split()]

    grid[y2 - 1][x2 - 1] = answerGrid[y2 - 1][x2 - 1]
    printGrid(grid)

    if grid[y1 - 1][x1 - 1] == answerGrid[y2 - 1][x2 - 1]:
        print("Yay! You got it!")
    else:
        print("Whoops! Try again!")
        grid[y1 - 1][x1 - 1] = "0"
        grid[y2 - 1][x2 - 1] = "0"
        input("Press Enter to try again.")
        clear()

def gameOver(grid):
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
        while not gameOver(grid):
            printGrid(grid)
            playTurn(grid, answerGrid)

    

main()