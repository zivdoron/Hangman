from Structure.Models.GamePhase import Game, GlobalPhase

if __name__ == "__main__":
    game = Game()
    while game.gamePhase != GlobalPhase.Quit:
        game.GameLoop()