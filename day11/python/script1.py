from scipy.spatial.distance import cityblock

# Read the matrix from the file
with open("../input.txt", "r") as f:
    lines = f.readlines()

# Create a matrix from the lines
matrix = [list(x.strip()) for x in lines]

# Create a copy of the matrix
new_matrix = [x[:] for x in matrix]

# Assign indices to '#' elements and store their coordinates
index = 1
coords = []
for i in range(len(new_matrix)):
    for j in range(len(new_matrix[i])):
        if new_matrix[i][j] == "#":
            new_matrix[i][j] = str(index)
            index += 1
            coords.append((i, j))

# Identify rows without numbers
rows = [i for i, row in enumerate(new_matrix) if not any(char.isdigit() for char in row)]

# Identify columns without numbers
cols = [i for i in range(len(new_matrix[0])) if not any(row[i].isdigit() for row in new_matrix)]

# Adjust coordinates based on rows and columns without numbers
for i, (original_x, original_y) in enumerate(coords):
    for j in range(len(rows)):
        if original_x > rows[j]:
            coords[i] = (coords[i][0] + 1, coords[i][1])
    for k in range(len(cols)):
        if original_y > cols[k]:
            coords[i] = (coords[i][0], coords[i][1] + 1)

# Find distances in a single loop
tot = 0
for i in range(1, index):
    for j in range(1, index):
        if i > j:
            tot += cityblock(coords[i - 1], coords[j - 1])

# Print total distance
print(f"Total distance: {tot}")
