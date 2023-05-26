import socket
import sys
import gameboard


class Player1:
    def __init__(self):
        self.playerName = "player1"
        self.gameBoard = gameboard.gameboard()


if __name__ == '__main__':
    socket1 = socket.socket()
    # 询问用户输入服务器的IP地址
    #host = input("Please input the server's IP address: ")
    # 询问用户输入服务器的端口号
    port = int(input("Please input the server's port number: "))
    host = socket.gethostname()
    # 连接服务器
    while True:
        try:
            socket1.connect((host, port))
            break
        except:
            print("Failed to connect to the server. try again.(y/n)")
            if input() == 'n':
                sys.exit()
    # 初始化游戏
    player1 = Player1()
    #询问用户名
    player1.playerName = input("Please input your username: ")
    player1.gameBoard.player1Name = player1.playerName
    # 向服务器发送用户名
    socket1.send(player1.playerName.encode())
    # 接收服务器的用户名
    otherUsername = socket1.recv(1024).decode()
    player1.gameBoard.player2Name = otherUsername
    print("You are playing with " + otherUsername)

    # 开始游戏
    while True:
        # 如果上一回合是对方走的
        if player1.gameBoard.lastPlayer == player1.gameBoard.player2Name or player1.gameBoard.lastPlayer == "":
            # 询问用户输入下一步的坐标
            move = input("Please enter the move.(a number between 1 and 9):")
            # 将用户输入的坐标发送给服务器
            socket1.send(move.encode())
            # 将用户输入的坐标更新到游戏棋盘
            position = int(move)
            player1.gameBoard.updateGameBoard(player1.playerName, position)
            # 打印游戏棋盘
            player1.gameBoard.display()
        else:
            # 接收服务器发送的下一步的坐标
            move = socket1.recv(1024).decode()
            # 将服务器发送的坐标更新到游戏棋盘
            position = int(move)
            player1.gameBoard.updateGameBoard(player1.gameBoard.player2Name, position)
            # 打印游戏棋盘
            player1.gameBoard.display()
        # 如果游戏结束
        if player1.gameBoard.isWinner():
            # 如果上一回合是自己走的
            if player1.gameBoard.lastPlayer == player1.playerName:
                # 自己赢了
                player1.gameBoard.numWins += 1
            else:
                # 自己输了
                player1.gameBoard.numLosses += 1

            # 询问用户是否继续游戏
            aws = input("Do you want to play again? y/n")
            if aws == 'y' or aws == 'Y':
                socket1.send("Play Again".encode())
                # 重置游戏棋盘
                player1.gameBoard.resetGameBoard()
                continue
            else:
                socket1.send("Fun Times".encode())
                player1.gameBoard.printStats()
                sys.exit()
        else:
            # 如果游戏棋盘已经满了
            if player1.gameBoard.boardIsFull():
                # 平局
                player1.gameBoard.numTies += 1
                # 询问用户是否继续游戏
                aws = input("Do you want to play again? y/n")
                if aws == 'y' or aws == 'Y':
                    socket1.send("Play Again".encode())
                    # 重置游戏棋盘
                    player1.gameBoard.resetGameBoard()
                    continue
                else:
                    socket1.send("Fun Times".encode())
                    player1.gameBoard.printStats()
                    sys.exit()
