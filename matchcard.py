#!/usr/bin/env python3
# Created by Farhad Makiabady
# https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/

import random

def coordInput():
    size = int(input("Please select a size you wish to play (2, 4 or 6): "))
    return size

def createGrid(size):
    return [["0"] * size for _ in range(size)]

def printGrid(grid):
    for row in grid:
        print(row)

def populateGrid(grid, size):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    selectedCards = random.sample(cards, int(size**2 / 2))
    answerGrid = createGrid(size)
    
    while any("0" in sublist for sublist in answerGrid):
        randomCard = random.choice(selectedCards)
        if sum(x.count(randomCard) for x in answerGrid) < 2:
            h = random.randint(0, size - 1)
            w = random.randint(0, size - 1)
            if answerGrid[h][w] == "0":
                answerGrid[h][w] = randomCard
        else: 
            randomCard = random.choice(selectedCards)

def main():
    print("Welcome to Match Card!")

    size = coordInput()
    grid = createGrid(size)
    populateGrid(grid, size)
    

main()