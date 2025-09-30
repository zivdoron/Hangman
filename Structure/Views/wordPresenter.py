


class WordPresenter:
    instance = None

    def __init__(self):
        if(WordPresenter.instance == None):
            WordPresenter.instance = self

    def GetLetterToPresent(self, guessedLetters, correctWord):
        wordToPrint = ''
        for i in range(list(correctWord).__len__()):
            if(list(guessedLetters).__contains__( list(correctWord)[i])):
                wordToPrint += correctWord[i]
            else:
                wordToPrint += '_'
        print(wordToPrint)

