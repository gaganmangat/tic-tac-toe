from random import random
import math

def noOfMoves(board):
    count = 0

    for line in board:
        for value in line:
            if value != '_':
                count += 1
    return count

def getResult(board, symbol):
    #check if any row is a win
    if noOfMoves(board) < 5:
        return 0 #incomplete

    winlist = [symbol]*3

    for line in board:
        #if line == xlist or line == olist:
        if line == winlist:
            return symbol #win for symbol

    #check if any column is a win
    for i in range(3):
        clist = [board[0][i], board[1][i], board[2][i]]
        #if clist == xlist or clist == olist:
        if clist == winlist:
            return symbol #win for symbol

    #check for diagonals
    dlist1 = [board[0][0], board[1][1], board[2][2]]
    dlist2 = [board[0][2], board[1][1], board[2][0]]
    #if (dlist1 == xlist or dlist1 == olist) or (dlist2 == xlist or dlist2 == olist):
    if dlist1 == winlist or dlist2 == winlist:
        return symbol #win for symbol

    #check for tie or incomplete board
    #for value in (board[0] + board[1] + board[2]):
    #    if value != 'x' or value != 'o':
    #        return 0 #incomplete board
    #    else:
    #        return 3 #complete board with o's and x's, hence a tie
    if noOfMoves(board) == 9:
        return 3
    return 0

"""
def getBestMove(board):
    #boardlist = board[0] + board[1] + board[2] #concatenate the three rows(lists) into a single list
    newboard = board.copy() #create a new board
    i = 0 #board row iterator

    for line in newboard: #for every position
        j = 0 # column iterator
        for value in line:
            if value == '_':  #for every empty position
                newboard[i][j] = 'o'
            result = getResult(newboard)
            if result == 1:
                break #computer has won
            j += 1
        i += 1
"""

def getAvailableMoves(board):
    availableMoves = [] #list of available moves i.e. empty cells
    i = 0
    for line in board:
        j = 0
        for value in line:
            if value == '_':
                availableMoves.append([i,j]) #append location of empty cell
            j += 1
        i += 1
    #print("availableMoves: ")
    #print(availableMoves)
    return availableMoves

def getBestMove(board, symbol): #symbol has the symbol of player with next move

    def shuffle(list):
        #print("shufflelist is")
        #print(list)
        if len(list) == 0:
            return list

        i = len(list) - 1
        while i != 0:
            rand = math.floor(random() * (i))
        #    print("rand is " + str(rand))
            list[i], list[rand] = list[rand], list[i]
            i -= 1
        return list


    def sortIt(list):
        for i in range(len(list) - 1):
            for j in range(1, len(list)):
                if list[i][2] < list[j][2]:
                    list[i], list[j] = list[j], list[i]
        #print("After sorting:")
        #print(list)
        return list

    availableMoves = getAvailableMoves(board) #get a list of empty cells
    availableMovesAndScores = [] #dictionary

    i = 0
    newboard = []
    while i < len(availableMoves): #moves is a list which has the location of empty cell i.e. [i,j]
        j = 0
        k = len(availableMoves) - 1
        #newboard = []
        move = availableMoves[i]
        #print("ITERATION" + str(i))
        #print("moves is: " + str(move))
        newboard = board.copy() #make a copy of the board for temporary processing
        while j < i:
            tempmove = availableMoves[j]
            newboard[tempmove[0]][tempmove[1]] = '_'
            j += 1
        while k > i:
            tempmove = availableMoves[k]
            newboard[tempmove[0]][tempmove[1]] = '_'
            k -= 1

        #print("newboard is: ")
        #print(newboard)
        #newboard[moves[0]][moves[1]] = symbol #moves[0], moves[1] contain the row and column number of the empty cell
        newboard = applyMove(newboard, move, symbol)
        #print("after applying move, newboard is: ")
        #print(newboard)
        result = getResult(newboard, symbol)
        #print("result is: ")
        #print(result)

        if result == 3: #tie
            score = 0
            #print("in if")
        elif result == symbol: #win
            score = 1
        #    print("in elif")
        else:
        #    print("in else")
            othersymbol = 'x' if symbol == 'o' else 'o'
            nextMove = getBestMove(newboard, othersymbol)
            score = -nextMove[2] #score

        t = move
        t.append(score)
        #print("t is ")
        #print(t)

        if score == 1:
            return t #moves is already a list, score is the score corresponding to the location present in moves
        availableMovesAndScores.append(t)
        #print("availableMovesAndScores is: ")
        #print(availableMovesAndScores)
        i += 1

    shuffle(availableMovesAndScores)

    #moves.append(score)
    #sortedDict = sorted(availableMovesAndScores.items(), key = lambda kv: kv[1])
    sortIt(availableMovesAndScores)

    #print("availableMovesAndScores")
    #xprint(availableMovesAndScores)
    #if len(availableMovesAndScores) != 0:
    return availableMovesAndScores[0]
    #else:
    #    return availableMovesAndScores.append(moves.append())

def applyMove(board, move, symbol):
    board[move[0]][move[1]] = symbol
    return board

def main():
    Board = [ ['_' , '_' , '_'], ['_' , '_' , '_'], ['_' , '_' , '_']] #empty board
    realBoard = [ ['_' , '_' , '_'], ['_' , '_' , '_'], ['_' , '_' , '_']]
    xlist = ['x', 'x', 'x'] #x wins
    olist = ['o', 'o', 'o'] #o wins

    plsymbol = input("Choose a symbol(x/o) :   ")
    if plsymbol == 'x':
        comsymbol = 'o'
    if plsymbol == 'o':
        comsymbol = 'x'

    k = 0
    while k < 9:
        #print("k " + str(k))
        #print("noOfMoves: " + str(noOfMoves(Board)))
        print("1   2   3")
        print("4   5   6")
        print("7   8   9")
        loc = int(input("Choose a location:"))
        Board = [ ['_' , '_' , '_'], ['_' , '_' , '_'], ['_' , '_' , '_']] #empty board
        for i in range(3):
            for j in range(3):
                if realBoard[i][j] != '_':
                    Board[i][j] = realBoard[i][j]

        if 1 <= loc <= 3 and Board[0][loc-1] == '_':
            Board[0][loc-1] = plsymbol
            realBoard[0][loc-1] = plsymbol
        elif 4 <= loc <= 6 and Board[1][loc-4] == '_':
            Board[1][loc-4] = plsymbol
            realBoard[1][loc-4] = plsymbol
        elif 7 <= loc <= 9 and Board[2][loc-7] == '_':
            Board[2][loc-7] = plsymbol
            realBoard[2][loc-7] = plsymbol
        else:
            print("Choose a valid location")
            continue

        #computer's turn:
        if (k != 4):
            move = getBestMove(Board, comsymbol)
            print("best move is" + str(move[0]) + str(move[1]))
            realBoard[move[0]][move[1]] = comsymbol

        for row in realBoard:
            print(row)
        #print(realBoard)

        if getResult(realBoard, plsymbol) == plsymbol:
            print("PLAYER WON")
            break
        if getResult(realBoard, comsymbol) == comsymbol:
            print("COMPUTER WON")
            break
        if getResult(realBoard, plsymbol) == 3:
            print("TIE")
            break
        k += 1

if __name__ == "__main__":
    main()
