from enum import Enum
from logging import exception

from Structure.Models import WordGuesser
from Structure.Views import WordPresenter
from Structure.Views import HangingShape
from Structure.Controllers.edge import PlayerInput

class LevelPhase(Enum):
    Guessing = 0
    EndedGuessing = 1
    StartedGuessingTurn = 2
    OutOfGuess = 3

class GlobalPhase(Enum):
    InGame = 0
    StartingMenu = 1
    Settings = 2

DEFAULT_SPACING = "\n\n\n"
class Game:

    instance: 'Game' = None

    gamePhase = GlobalPhase.StartingMenu
    levelPhase = LevelPhase.OutOfGuess

    input = PlayerInput()
    def __init__(self):
        if Game.instance == None:
            Game.instance = self

    def SetPlayerInput(self, input : PlayerInput):
        self.input = input

    def GetInGame(self):
        self.gamePhase = GlobalPhase.InGame

    def GoToNextTurn(self):
        if self.levelPhase == LevelPhase.EndedGuessing:
            self.levelPhase = LevelPhase.StartedGuessingTurn
            return True
        else:
            exception("cannot start another turn.\nthis button did not appear in the right time")
            return False

    def GameLoop(self):
        HangingShape()
        pInput = PlayerInput()
        pInput.SetContinueToNextTurn(lambda: self.GoToNextTurn())
        wordPresenter = WordPresenter()
        print("Hello and welcome to my Hangman game.")
        pInput.chooseKeyMapping(5)
        print(DEFAULT_SPACING)
        self.showRules()
        print(DEFAULT_SPACING)
        HangingShape.instance.SetDefaultNumOfTries()

        print("Let's begin the game!")
        WordGuesser.RandomizeANewWord()
        while True:
            if WordGuesser.CheckWin():
                print("YOU WiN! MABRUK!")
                break
            if WordGuesser.CheckLose():
                print("Nice try, let's try again...") #add result summary and back to word randomization.
            pInput.GetGuess()



    def showRules(self):
        print("Rules of the game")


