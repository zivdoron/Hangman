import random

from Structure.Views import HangingShape
from Structure.Views import WordPresenter


class WordGuesser:
    chosenWord = ""
    guessedLetters = []

    @staticmethod
    def GetACustomWord(newWord):
        WordGuesser.chosenWord = newWord

    @staticmethod
    def RandomizeANewWord():
        WordGuesser.chosenWord = WordsRandomizer.RandomizeAWord()

    @staticmethod
    def GetGuess(guess : chr):
        if( not WordGuesser.guessedLetters.__contains__(guess)):
            WordGuesser.guessedLetters.__iadd__(guess)
            HangingShape.instance.RenderNext(WordGuesser.chosenWord.__contains__(guess))
            WordPresenter.instance.GetLetterToPresent(WordGuesser.guessedLetters, WordGuesser.chosenWord)
        #win condition
        else:
            print("You've already chosen this character, have another guess")
            WordGuesser.GetGuess(input())


    @staticmethod
    def CheckWin():
        lettersInWord = list(WordGuesser.chosenWord)
        return all(item in WordGuesser.guessedLetters for item in lettersInWord) and int(HangingShape.instance.numOfAttempts) > 0
#    lettersInWord.all(lambda l: WordGuesser.guessedLetters.__contains__(l))

    @staticmethod
    def CheckLose():
        return int(HangingShape.instance.numOfAttempts) == 0
    @staticmethod
    def KnownLetters():
        lettersInWord = list(WordGuesser.chosenWord)

        for i in range(len(lettersInWord)):
            if( not WordGuesser.guessedLetters.__contains__(lettersInWord[i])):
                lettersInWord.pop(i)

        return lettersInWord

    @staticmethod
    def rightAndWrongLetters():
        letters = {[]}
        letters.clear()
        for i in len(WordGuesser.chosenWord):
            letters.add([WordGuesser.chosenWord[i], WordGuesser.guessedLetters.__contains__(WordGuesser.chosenWord[i])])
        return letters



class WordsRandomizer:
    words = ["saturday","derivative","anonymous","suggestion","exclamation","rigorous","enormous", "umbrella"]

    @staticmethod
    def RandomizeAWord():
        return WordsRandomizer.words[random.randrange(len(WordsRandomizer.words) - 1)]

    @staticmethod
    def AddWordToLibrary(newWord):
        WordsRandomizer.words.__add__(newWord)
