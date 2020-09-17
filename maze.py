######################################## Function A ###################################################
############################################ Code #####################################################

# function to check if x, y is valid 
def isSafe( maze, x, y ): 
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
		return True
	return False

# Creating 2-D list 
def solveMaze( maze ): 
	sol = [ [ 0 for j in range(N) ] for i in range(N) ] 
	if not solveMazeUtil(maze, 0, 0, sol):
		return "No Path Found"
	return sol
	
# A recursive function to solve Maze problem 
def solveMazeUtil(maze, x, y, sol): 
	if x == N - 1 and y == N - 1 and maze[x][y]== 1: 
		sol[x][y] = 1
		return True
		
	# Check if maze[x][y] is valid 
	if isSafe(maze, x, y):
		sol[x][y] = 1
		
		# Move forward in x direction 
		if solveMazeUtil(maze, x + 1, y, sol): 
			return True
		
		# then Move down in y direction 
		if solveMazeUtil(maze, x, y + 1, sol): 
			return True
		
		# BACKTRACK: unmark x, y as part of solution path 
		sol[x][y] = 0
		return False

######################################### Function B ##################################################
################################### Function to Input Maze ############################################
#Input
input_maze = open("inputmaze.txt", "w")
input_maze.write(input())
input_maze.close()


input_maze = open("inputmaze.txt", "r")
N = input_maze.readline()
input_maze.close()


input_maze = open("inputmaze.txt", "a")
input_maze.write('\n')
for i in range(int(N)):
    input_maze.write(input())
    input_maze.write('\n')


input_maze = open("inputmaze.txt", "r")
input_matrix = []
N = int(N)
for i in range(N + 1):
    line = input_maze.readline()
    if i > 0:
        input_matrix.append(list(map(int, line.rstrip().split())))
input_maze.close()



####################################### Function C ##################################################
################################# Function To Get Output ############################################

matrix_list = solveMaze(input_matrix)

output_maze = open("outputmaze.txt", "w")
if type(matrix_list) is list:
    for i in matrix_list:
        for j in i:
            output_maze.write(str(j))
            output_maze.write("")

        output_maze.write("\n")
    output_maze.close()

else:
    output_maze.write(str(matrix_list))
    output_maze.close()
