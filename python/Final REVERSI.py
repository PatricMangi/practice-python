import copy

def New_Board():
    Board = [[0] * 8 for i in range(8)]
    Board[3][3]=1
    Board[4][3]=2
    Board[4][4]=1
    Board[3][4]=2
    
    for i in Board:
        print(i,'\n')
    return Board
    

    

def score(Board):
    s1=2
    s2=2
    for i in range(8):
        for j in range(8):
            if Board[i][j]=='1':
                s1=s1+1
            if Board[i][j]=='2':
                s2=s2+1
    return s1,s2
Board=New_Board()
print(" the score is ",score(Board))

def enclosing(Board,player,pos,direct):
    direct=[dr(x,y) for x,y in [(-1,-1),(-1,0),(0,-1),(1,-1),
                                (-1,1),(0,1),(1,0),(1,1)]]


#def valid_Moves(Board,player1,player2):
    
    
