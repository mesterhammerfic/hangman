# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, bs4, string


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
        animalSoup = bs4.BeautifulSoup(res.text, features='lxml')
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
        descriptionElem = animalSoup.select('p')
        if len(descriptionElem) == 0: #makes sure there is a description paragraph
#            print('*no description')
            continue
        else:
            description = descriptionElem[0].getText()
#            
        finalList = [word, description]
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
    wordDescription = gameData[1]
    letterList = list(word)
    unusedLetters = list(string.ascii_uppercase)
    
    #score.set number of tries
    chances = 5
    
    #correct guesses
    displayWord = []
    for letter in letterList:
        displayWord.append("_")
    displayWord = letterFinder(letterList, displayWord, ' ') #automatically adds spaces
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
        print("available guesses: " + str(unusedLetters))
        #input
        while True:
            guess = input("Guess a letter: ")
            guess = guess.upper()
            if type(guess) == str and len(guess) == 1 and guess.isalpha() and unusedLetters.count(guess) == 1:
                break
        #score.adjustment
        if letterList.__contains__(guess):
            displayWord = letterFinder(letterList, displayWord, guess)
        else:
            chances=chances-1
            displayChances.append(guess)
        unusedLetters.remove(guess)
    #ending
    if chances == 0:
        print("You lost\n\n----------------")
        print("the word was: "+word+"\n\n"+wordDescription)
    else:
        print("You won\n\n----------------")
        print(word+"\n\n"+wordDescription)
        
    return

newGame = retrieveWord()

game(newGame)
