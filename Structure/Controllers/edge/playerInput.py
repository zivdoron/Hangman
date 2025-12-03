import logging
from logging import DEBUG
from idlelib.delegator import Delegator
from typing import  Optional

from Structure.Controllers.basePlayerInput import BasePlayerInput, KeyMaps
from Structure.Models import WordGuesser
from Structure.Models import WordsRandomizer




class PlayerInput(BasePlayerInput) :

    OnGoToNextTurn = Delegator() #change to
    def GetGuess(self):
        print("Guess a letter")
        letter = self.WaitForPlayerResponse()
        if letter is not None:
            WordGuesser.GetGuess(letter.lower()[0])

    def AddWord(word):
        WordsRandomizer.AddWordToLibrary(word)

    def ContinueToNextTurn(self):
        self.OnGoToNextTurn

    def SetOnContinueToNextTurn(self, func):
        self.OnGoToNextTurn.setdelegate(func)




    def assignkeymaps(self, chosenMap):
        chosenMap = chosenMap.lower()
        if(chosenMap == "normal"):
            self.map = KeyMaps.Normal
            return True
        if(chosenMap == "alt"):
            self.map = KeyMaps.Alt
            return True
        if DEBUG: print("The player didn't type appropriately to choose a keymap. \nPlayer typo: " + chosenMap)
        return False

    def showKeyMapping(self):
        print("here are the key maps to choose from:\n")
        print("Normal key map:\n") #iterate upon the Enum itself
        for pair in KeyMaps.Normal.__dict__.items():
            print("key: " + str(pair[0]) + " order: " + str(pair[1]))
        print("\n\n")
        print("Alternative key map:\n")
        for pair in KeyMaps.Alt.__dict__.items():
            print("key: " + str(pair[0]) + " order: " + str(pair[1]))

    def chooseKeyMapping(self, retryCount):
        self.showKeyMapping()
        self.inputForChangingMap(retryCount)

    @classmethod
    def inputForChangingMap(cls, maxRetries, count: int = 0):
        print("Please choose your desired keymaps")
        if not cls.assignkeymaps(input()) and count <= maxRetries : cls.inputForChangingMap(maxRetries, count+1)
        if(count > maxRetries) :
            print("Fine... I'll stick with standard then.")
            cls.assignkeymaps("normal")