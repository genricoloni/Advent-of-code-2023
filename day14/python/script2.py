def north(matrix):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])): 
            if matrix[i][j] == "O":
                #move this element in the same column, reducing the row until there's another O or a #
                k = i
                while matrix[k-1][j] == '.' and k > 0:
                    k -= 1
                else:
                    matrix[i][j] = '.'
                    matrix[k][j] = 'O'
    return matrix

def west(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i])): 
            if matrix[i][j] == "O":
                #move this element in the same row, reducing the column until there's another O or a #
                k = j
                while matrix[i][k-1] == '.' and k > 0:
                    k -= 1
                else:
                    matrix[i][j] = '.'
                    matrix[i][k] = 'O'
    return matrix

def south(matrix):
    for i in range(len(matrix)-2, -1, -1):
        for j in range(len(matrix[i])): 
            if matrix[i][j] == "O":
                #move this element in the same column, reducing the row until there's another O or a #
                k = i
                while k < len(matrix)-1 and matrix[k+1][j] == '.' :
                    k += 1
                else:
                    matrix[i][j] = '.'
                    matrix[k][j] = 'O'
    return matrix

def east(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-2, -1, -1): 
            if matrix[i][j] == "O":
                #move this element in the same row, reducing the column until there's another O or a #
                k = j
                while k < len(matrix[i])-1 and matrix[i][k+1] == '.' :
                    k += 1
                else:
                    matrix[i][j] = '.'
                    matrix[i][k] = 'O'
    return matrix

def cycle(matrix):

    matrix = north(matrix)
    matrix = west(matrix)
    matrix = south(matrix)
    matrix = east(matrix)

    return matrix

def is_duplicate(configurations, matrix):
    # Convert the current matrix configuration to a tuple for hashability
    current_config = tuple(tuple(row) for row in matrix)
    if current_config in configurations:
        return True
    else:
        configurations.add(current_config)
        return False

with open("../input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

matrix = [[num for num in line] for line in lines]
count = 0

# Keep track of seen configurations
seen_configurations = set()

while True:
    count += 1

    # Check for duplicate configurations
    if is_duplicate(seen_configurations, matrix):
        break

    matrix = cycle(matrix)


matrix = [[num for num in line] for line in lines]
count = 1000000000%count

while count > 0:
    matrix = cycle(matrix)
    count -= 1

tot = 0
for i in range(len(matrix)):
    count = matrix[i].count('O')
    tot += count * (len(matrix[i]) - i)

print(tot)

    