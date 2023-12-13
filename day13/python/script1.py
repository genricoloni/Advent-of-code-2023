def transpose(grid):
    #Transpose a grid by swapping rows and columns
    return list(map(''.join, zip(*grid)))

def count_differences(linea, lineb):
    #Count the number of differences between two lines
    return sum(chara != charb for chara, charb in zip(linea, lineb))

def find_reflections(grid):
    #Find reflections in the grid and return the perfect size
    height = len(grid)
    perfect = 0

    # Check reflections along the rows
    for size in range(1, height // 2 + 1):
        a = grid[:size]
        b = grid[size:2 * size][::-1]
        diff = count_differences(a, b)

        if diff == 0:
            perfect = size
            break

    # Check reflections along the columns
    if not perfect:
        for size in range(1, height // 2 + 1):
            a = grid[height - 2 * size:height - size]
            b = grid[height - size:][::-1]
            diff = count_differences(a, b)

            if diff == 0:
                perfect = height - size
                break

    return perfect

# Open the first argument as input or use stdin if no arguments were given

with open("../input.txt") as f:
    grids = f.read().split('\n\n')

ans = 0

for raw_grid in grids:
    g = raw_grid.splitlines()

    # Check reflections along rows
    perfect_rows = find_reflections(g)
    ans += 100 * perfect_rows

    # Check reflections along columns (transposed grid)
    transposed_grid = transpose(g)
    perfect_cols = find_reflections(transposed_grid)
    ans += perfect_cols

print(ans)
