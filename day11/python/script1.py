from scipy.spatial.distance import cityblock
import itertools

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
coords = [(x + sum(1 for r in rows if x > r), y + sum(1 for c in cols if y > c)) for x, y in coords]

# Find distances in a single loop
# Find distances with symmetry optimization
tot = 0

for i in range(1, index):
    for j in range(i + 1, index):
        tot += cityblock(coords[i - 1], coords[j - 1])
   
# Print total distance
print(f"Total distance: {tot}")
