
# program to make tic tac toe Game 

# firstly create dictionary of tic tac toe board 
theBoard = {'top-l':' ', 'top-m':' ', 'top-r':' ','mid-l':' ','mid-m':' ','mid-r':' ','low-l':' ','low-m':' ','low-r':' ' }

def printBoard(board):
    print(board['top-l']+ '|'+ board['top-m'] + '|'+ board['top-r']+'|')
    print('--+--+--')
    print(board['mid-l']+ '|'+ board['mid-m'] + '|'+ board['mid-r']+'|')
    print('--+--+--')
    print(board['low-l']+ '|'+ board['low-m'] + '|'+ board['low-r']+'|')
    print('--+--+--')

turn = 'X'

for i in range(9):
        printBoard(theBoard)
        print('turn for ', turn +' '+ 'move on which place')
        move = input()

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
printBoard(theBoard)