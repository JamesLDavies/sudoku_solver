#Sudoku Solver
"""
Version | Date | Comments
1.0.0	27-05-20	Initial release

ABOUT
Script to solve a sodoku puzzle using a backtracking algorithm

KNOWN BUGS/ISSUES

"""
#---------FUNCTIONS--------

#Function to print the current board
def print_board(board):
	for i in range(len(board)):
		print(" ")
		for j in range(len(board)):
			print(board[i][j],end=' ')
			if (j+1) % 3 == 0:
				print("|",end=' ')
	print("\n")
		
#Function to search for an unsolved element
def find_empty_cell(board):
	for i in range(len(board)):
		for j in range(len(board)):
			#print(board[i][j])
			if(board[i][j] == 0):
				#print("DEBUG: Empty cell found!")
				#print(board[i][j])
				return board[i][j],i,j


#Find solution for the given cell at board[x][y]
def find_cell_solution(board,x,y):

	print("DEBUG: Finding solution for",x,y)
	for i in range (1,10):
		print("DEBUG: Trial solution:",i)
		valid = validate_cell_solution(board,x,y,i)
		if  valid == True:
			print("DEBUG: Found solution to be",i)
			return i

		else:
			print("Error: No solution found")
		

def validate_cell_solution(board,x,y,num):
		#Check Row
		for j in range(0,9):
			if num == board[j][y] and j != x:
				#Invalid solution
				print("DEBUG: Invalid due to ROW using",j)
				return False
				

		#Check Col
		for j in range(0,9):
			if num == board[x][j] and j!=x:
				#Invalid solution
				print("DEBUG: Invalid due to COL using",j)
				return False

		#Check Box - ADDME!!!



		#return True if the trial solution passes all 3 checks
		return True




#Function to find a solution to the empty cell
def solve(board):
	cell,x,y = find_empty_cell(board)

	board[x][y] = find_cell_solution(board,x,y)



#---------CODE-------------
print("Sudoku Solver Version 1.0.0")


#Puzzle board that must be solved
#Zeros represent the blank numbers that must be solved
board = [
		[8,0,0,9,3,0,0,0,2],
		[0,0,9,0,0,0,0,4,0],
		[7,0,2,1,0,0,9,6,0],
		[2,0,0,0,0,0,0,9,0],
		[0,6,0,0,0,0,0,7,0],
		[0,7,0,0,0,6,0,0,5],
		[0,2,7,0,0,8,4,0,6],
		[0,3,0,0,0,0,5,0,0],
		[5,0,0,0,6,2,0,0,8]
]


#Print the inital board
print_board(board)

#Put in while false/true loop!!
solve(board)

#Print the solved board
print_board(board)

