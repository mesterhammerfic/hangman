# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, bs4


#Old Word selector, draws from a given list of words, requires the random and nltk module
#def wordSelector(listOfWords):
#    #returns an all cap word from a wordlist
#    randomIndex = int(random.random() * len(listOfWords))
#    selectedWord = listOfWords[randomIndex]
#    return selectedWord.upper()

def retrieveWord():
    #gets the website
    while True:
        print('searching...')
        res = requests.get('https://animals.fandom.com/wiki/Special:Random')
        res.raise_for_status()
        animalSoup = bs4.BeautifulSoup(res.text, features='html5lib')
        #get the word
        wordElem = animalSoup.select('.page-header__title')
        word = wordElem[0].getText()
#        print(word)
        wordTest = word.split(' ')
        incorrectFormat = 0
        for item in wordTest:
#            print(item)
            if item.isalpha() == False: #makes sure there are only letters in the name
#                print("*incorrect format")
                incorrectFormat = 1
        if incorrectFormat == 1:
            continue
        #gets the clues
#        descriptionElem = animalSoup.select('p')
#        if len(descriptionElem) == 0: #makes sure there is a description paragraph
##            print('*no description')
#            continue
#        else:
#            listOfClues = descriptionElem[0].getText().split('. ')
#            betterListOfClues = listOfClues[1:]
#            if len(betterListOfClues)<3: #makes sure there are at least 3 clues
##                print('*not enough clues')
#                continue
#            else:
#                finalList = betterListOfClues
        finalList = []
        finalList.insert(0, word)
        break
    
    return finalList
    
def letterFinder(word, display, letterGuess):
    #finds the locations of all occurences of a specific letter
    #returns a list with the found letters added in
    letterPositions = display
    for index, item in enumerate(word):
        if item == letterGuess:
            letterPositions[index] = letterGuess
    return letterPositions



def game(gameData):
    #score.format the word
    word = gameData[0].upper()
    letterList = list(word)
    #score.set number of tries
    chances = 5
    
    #correct guesses
    displayWord = []
    for letter in letterList:
        displayWord.append("_")
    displayWord = letterFinder(letterList, displayWord, ' ')
    #incorrect guesses
    displayChances = []
    
    #begin game loop
    while chances > 0 and displayWord != list(word):
        #display
        displayWordString = ""
        for i in displayWord:
            displayWordString = displayWordString + i
        print(displayWordString)
        print("incorrect guesses: " + str(displayChances))
        #input
        while True:
            guess = input("Guess a letter: ")
            if type(guess) == str and len(guess) == 1 and guess.isalpha():
                guess = guess.upper()
                break
        #score.adjustment
        if letterList.__contains__(guess):
            displayWord = letterFinder(letterList, displayWord, guess)
        else:
            chances=chances-1
            displayChances.append(guess)
    #ending
    if chances == 0:
        print("You lost")
        print("the word was: "+word)
    else:
        print("You won")
        print(word)
    return

newGame = retrieveWord()

game(newGame)
