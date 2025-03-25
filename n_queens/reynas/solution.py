from typing import List
class solution:
    def solve_queens(self,n)->List[List[str]]:
        board =  [ [ '.'for _ in range(n)] for _ in range(n)]   
        ans = []
        self.queen(board,0,ans,n)
        return ans
    def queen(self,board:List[List[str]],row:int,ans:List[List[str]],n:int):
        if row ==n:
            ans.append([''.join(row) for row in board])
            return 
        for col in range(n):
            if self.isSafe(board,row,col,n):
                board[row][col] = 'Q'
                self.queen(board,row+1,ans,n)
                board[row][col] = '.'
    def isSafe(self,board:List[List[str]],row:int,col:int,n:int)->bool:
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i,j = row,col
        while i >=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i-=1
            j-=1
        i,j=row,col
        while i>=0 and j<n:
            if board[i][j] == 'Q':
                return False
            i-=1
            j+=1
        return True
        
        