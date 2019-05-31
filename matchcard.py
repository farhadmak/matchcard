#!/usr/bin/env python3

def coordInput():
    size = int(input("Please select a size you wish to play: "))
    return size

def createGrid(size):
    return [[0] * size for _ in range(size)]

def printGrid(grid):
    for row in grid:
        print(row)

def main():
    print("Welcome to Match Card!")

    size = coordInput()
    grid = createGrid(size)
    printGrid(grid)

main()