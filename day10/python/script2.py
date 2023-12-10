def initialize_matrix(input_data):
    # Find the row with the first occurrence of "S"
    starting_positions = {
        min((row.find("S"), index) for index, row in enumerate(input_data) if "S" in row)
    }
    
    # Return the input data, starting positions, an empty set for visited positions, and -2 for n
    return input_data, starting_positions, set(), -2

file_path = "../input.txt"
input_data = open(file_path, "r").read().strip().split()

matrix, current_positions, visited_position, n = initialize_matrix(input_data)

# Main loop for grid traversal
while current_positions:
    # Update visited positions and potential next positions
    next_positions = set()
    
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

# Initialize an empty list to store row sums
row_sums = []

# Iterate over rows and columns in the matrix
for j in range(len(matrix)):
    for i in range(len(matrix[j])):
        # Check if the column has been visited
        column_has_been_visited = (i, j) in visited_position
        
        # Only proceed if the column has not been visited
        if not column_has_been_visited:
            # Count occurrences of characters "|JLS" in the visited columns
            count = 0
            
            # Iterate over visited columns and count occurrences of "|JLS"
            for k in range(i):
                if (k, j) in visited_position and matrix[j][k] in "|JLS":
                    count += 1
            
            # Append the count to the row_sums list
            row_sums.append(count)

# Calculate the total count by summing the remainders after dividing each row sum by 2
total_count = sum(row_sum % 2 for row_sum in row_sums)

# Print the final result
print(total_count)


