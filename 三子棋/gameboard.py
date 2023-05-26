class gameboard:
    def __init__(self):
        self.player1Name = ""
        self.player2Name = ""
        self.lastPlayer = ""
        self.numTies = 0
        self.numLosses = 0
        self.numWins = 0
        self.num_games = 1          # Number of games played
        self.turnNumber = 0         # Number of turns played
        self.gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.gameBoard[0] = " "
        self.gameBoard[1] = " "
        self.gameBoard[2] = " "
        self.gameBoard[3] = " "
        self.gameBoard[4] = " "
        self.gameBoard[5] = " "
        self.gameBoard[6] = " "
        self.gameBoard[7] = " "
        self.gameBoard[8] = " "
        self.gameBoard[9] = " "

    def updateGamesPlayed(self):
         self.num_games += 1

    def resetGameBoard(self):
        self.updateGamesPlayed()
        self.lastPlayer = ""
        self.turnNumber = 0
        self.gameBoard[0] = " "
        self.gameBoard[1] = " "
        self.gameBoard[2] = " "
        self.gameBoard[3] = " "
        self.gameBoard[4] = " "
        self.gameBoard[5] = " "
        self.gameBoard[6] = " "
        self.gameBoard[7] = " "
        self.gameBoard[8] = " "
        self.gameBoard[9] = " "

    # Updates the game board with the player's move
    def updateGameBoard(self, player, position):
        if self.gameBoard[position] == " ":
            if player == self.player1Name:
                self.gameBoard[position] = "X"
                self.lastPlayer = self.player1Name
            else:
                self.gameBoard[position] = "O"
                self.lastPlayer = self.player2Name
            self.turnNumber += 1
            return True

    def isWinner(self):
        if self.gameBoard[1] == self.gameBoard[2] == self.gameBoard[3] != " ":
            return True
        elif self.gameBoard[4] == self.gameBoard[5] == self.gameBoard[6] != " ":
            return True
        elif self.gameBoard[7] == self.gameBoard[8] == self.gameBoard[9] != " ":
            return True
        elif self.gameBoard[1] == self.gameBoard[4] == self.gameBoard[7] != " ":
            return True
        elif self.gameBoard[2] == self.gameBoard[5] == self.gameBoard[8] != " ":
            return True
        elif self.gameBoard[3] == self.gameBoard[6] == self.gameBoard[9] != " ":
            return True
        elif self.gameBoard[1] == self.gameBoard[5] == self.gameBoard[9] != " ":
            return True
        elif self.gameBoard[3] == self.gameBoard[5] == self.gameBoard[7] != " ":
            return True
        else:
            return False

    def isTie(self):
        if self.turnNumber == 9:
            return True
        else:
            return False

    def display(self):
        print(" ", self.gameBoard[1], " | ", self.gameBoard[2], " | ", self.gameBoard[3], " ")
        print(" ", self.gameBoard[4], " | ", self.gameBoard[5], " | ", self.gameBoard[6], " ")
        print(" ", self.gameBoard[7], " | ", self.gameBoard[8], " | ", self.gameBoard[9], " ")

    def boardIsFull(self):
        if self.turnNumber >= 9:
            return True
        else:
            return False

    def printStats(self):
        print("Player1 Name: ", self.player1Name)
        print('Player2 Name: ', self.player2Name)
        print("Last Player: ", self.lastPlayer)
        print("Number of games: ", self.num_games)
        print("Number of Ties: ", self.numTies)
        print("Number of Losses: ", self.numLosses)
        print("Number of Wins: ", self.numWins)
