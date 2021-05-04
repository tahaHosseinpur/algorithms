# i just write the code and explain my understanding i will look into it even more and try to find ways to improve its functioning 
# . . . .
# all in all it is better than brute Force

# this func is here to display the chessBoard
def displyChessBoard(chessBoard):
    for row in chessBoard :
        print(row)

# there we check that the queens woudnt hit eachother it checks thesse conditions in order i assume it is not so proficinet this way        
def checkIfThePlacementIsValid(chessBoard , row , col):

            #check if there has been any queen placed on the same row 
            for c in range(col) :
               if (chessBoard[row][c] == 1) :
                   return False
        
            # it generates (i ,j) like for example if (i , j) = (4 , 3) it generates (3,2) -> (2,1) -> (1 , 0) to check there is any queen there so it can attack it
            for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
               if (chessBoard[r][c] == 1) :
                   return False
        
            # here we check .  . . . . . 
            for r, c in zip(range(row+1, len(chessBoard), 1), range(col-1, -1, -1)) :
              if (chessBoard[r][c] == 1) :
                  return False
            return True                

                                
# this is the main func of our algorithem , its a recursive func and calls it self over and over till all the queens have been placed 
def solveNqueenPuzzelUsingBacktracking(chessBoard , currentCol):
            # if all the queens had been placed stop the process and just print the current solution and return to see if there is another solution
            if (currentCol >= len(chessBoard)):
                #disply the chessBoard or array 
                print("<><><><><><><>")
                displyChessBoard(chessBoard)
                print("<><><><><><><>\n")            
            else :
                 # place queen in every row of first col and see if there would be a solution for it
                 # repeats for each row of same column
                for row in range(len(chessBoard)):
                    # here we place the queen 
                    chessBoard[row][currentCol] = 1
                    #we want to see if its valid woudlnt we ?
                    if(checkIfThePlacementIsValid(chessBoard , row , currentCol) == True):
                        # so it was valid try next col reapeat the same process
                        solveNqueenPuzzelUsingBacktracking(chessBoard , currentCol + 1)
                    #so if our valid func retuens false we switch the 1 in to 0 and try another row of current col
                    chessBoard[row][currentCol] = 0;     

#our main func 
def main() :
    #def an array
     chessboard = []
    #N is the number of columns and rows of chess board
     N = int(input("Enter chess1board size : "))
     #here we define the number of rows and cols 
     rows , cols = (N,N)
     #creat an array of N columns and N rows 
     chessBoard = [[0 for i in range(cols)] for i in range(rows)]
     #pass the created chessBoard to solve our problem 
     solveNqueenPuzzelUsingBacktracking(chessBoard , 0)   
