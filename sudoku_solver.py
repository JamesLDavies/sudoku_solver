#Sudoku Solver
"""
Version | Date | Comments
1.1.0	28-05-20	Used recursion and backwards tracing to solve board
1.0.0	27-05-20	Initial release

ABOUT
Script to solve a sudoku puzzle using a backtracking algorithm

"""

#---------Global Variables---------
verbose = 0

#---------FUNCTIONS--------

#Function to print the current board
def print_board(board):
	for i in range(len(board)):

		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - -")

		for j in range(len(board)):
			print(board[i][j],end=' ')

			if (j+1) % 3 == 0:
				print("|",end=' ')
		print(" ")
		
#Function to search for an unsolved element
def find_empty_cell(board):
	for i in range(len(board)):

		for j in range(len(board)):

			if board[i][j] == 0:
				return i,j

	return None #if no 'empty' (0) squares remain, the board is solved, end recursion
		

def validate_cell_solution(board,x,y,num):
		#Check Row
		for i in range(0,9):
			if num == board[i][y] and i != x:
				#Invalid solution
				return False
				

		#Check Col
		for i in range(0,9):
			if num == board[x][i] and i!=x:
				#Invalid solution
				return False

		#Check Box
		#Find current 3x3 box
		box_x = y // 3
		box_y = x // 3
		#Cycle through all box elements using binomial expressions
		for i in range(box_y * 3, box_y*3 + 3):

			for j in range(box_x * 3, box_x*3 + 3):

				if num == board[i][j] and (i,j) != (x,y):
					#Invalid solution
					return False

		#Return True if the trial solution passes all 3 checks
		return True


#Function to find a solution to the empty cell
#Function uses recursion until entire board is solved
def solve(board):
	#verbose option to show each step of board being solved
	if verbose > 0:
		print("SOLVING...")
		print_board(board)

	find = find_empty_cell(board)
	if not find:
		return True #Board has been solved
	else:
		x,y = find

	for i in range(1,10): #sudoku cell solutions must be a number from 1-9
		if validate_cell_solution(board,x,y,i):
			board[x][y] = i

			if solve(board):
				return True
			if verbose > 0:
				print("BACKTRACKING...")
			board[x][y] = 0 #backtracking

	return False



#---------CODE-------------
print("Sudoku Solver Version 1.1.0")


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
print("\n===\tInitial Board\t===")
print_board(board)

#Recursive solve function
solve(board)

#Print the solved board
print("\n===\tSolved Board\t===")
print_board(board)

