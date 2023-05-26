import sys

import gameboard
import socket


class Player2:
    def __init__(self):
        self.PlayerName = "player2"
        self.board = gameboard.gameboard()


if __name__ == '__main__':
    player2 = Player2()
    # 接受player1的连接
    socket2 = socket.socket()
    # 询问监听的地址和端口
    # hostname = input("Please enter your Hostname/IP address: ")
    hostname = socket.gethostname()
    port = int(input("Please enter your port: "))
    socket2.bind((hostname, port))
    socket2.listen(5)
    connection, client_addr = socket2.accept()
    print("Connection from: ", client_addr)
    # 接受player1的用户名
    otherUsername = connection.recv(1024).decode()
    # 发送自己的用户名
    connection.sendall(player2.PlayerName.encode())
    # 初始化棋盘
    player2.board.player1Name = otherUsername
    player2.board.player2Name = player2.PlayerName
    # 开始游戏
    while True:
        # 如果上一回合是对方走的
        if player2.board.lastPlayer == player2.board.player1Name:

            move = input("Please enter the move. a num between 1-9: ")
            position = int(move)
            # 更新坐标
            player2.board.updateGameBoard(player2.PlayerName, position)
            player2.board.display()
            # 发送下一步坐标
            connection.sendall(move.encode())
        else:  # 如果上一回合是自己走的
            # 接受player1的下一步坐标
            move = connection.recv(1024).decode()
            position = int(move)
            player2.board.updateGameBoard(player2.board.player1Name, position)
            player2.board.display()
        if player2.board.isWinner():
            if player2.board.lastPlayer == player2.board.player1Name:
                player2.board.numLosses += 1
            else:
                player2.board.numWins += 1
            is_go_on = connection.recv(1024).decode()
            if is_go_on == 'Play Again':
                player2.board.resetGameBoard()
                continue
            else:
                player2.board.printStats()
                sys.exit()
        else:
            if player2.board.boardIsFull():
                player2.board.numTies += 1
                is_go_on = connection.recv(1024).decode()
                if is_go_on == 'Play Again':
                    player2.board.resetGameBoard()
                    continue
                else:
                    player2.board.printStats()
                    sys.exit()
