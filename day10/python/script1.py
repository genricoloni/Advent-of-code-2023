def initialize_matrix(input_data):
    # Find the starting position of "S"
    starting_positions = {
        min((row.find("S"), index) for index, row in enumerate(input_data) if "S" in row)
    }
    return input_data, starting_positions

# Read input data from the file and initialize variables
file_path = "../input.txt"
input_data = open(file_path, "r").read().strip().split()
matrix, current_positions = initialize_matrix(input_data)
visited_position = set()
n = -2

# Main loop for grid traversal
while current_positions:
    # Update visited positions and potential next positions
    next_positions = set()
    
    # Iterate over current positions to determine valid moves
    for current_x, current_y in current_positions - visited_position:
        # Define possible moves in each direction
        moves = [
            (current_x + 1, current_y, "-LFS", "-J7"),
            (current_x - 1, current_y, "-J7S", "-LF"),
            (current_x, current_y + 1, "|F7S", "|LJ"),
            (current_x, current_y - 1, "|LJS", "|F7")
        ]
        
        # Filter moves based on matrix boundaries and character constraints
        valid_moves = [
            (next_u, next_v) for next_u, next_v, f, g in moves
            if 0 <= next_v < len(matrix) and 0 <= next_u < len(matrix[next_v])
            and matrix[current_y][current_x] in f and matrix[next_v][next_u] in g
        ]
        
        # Add valid moves to the set of next positions
        next_positions.update(valid_moves)

    # Update variables
    visited_position |= current_positions
    current_positions = next_positions
    n += 1
else:
    # Print the final result after grid traversal
    print(n)
