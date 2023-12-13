def transpose(grid):
    #Transpose a grid by swapping rows and columns
	return list(map(''.join, zip(*grid)))

def count_differences(a, b):
    #Count the number of differences between two lines
	diff = 0
	for linea, lineb in zip(a, b):
		diff += sum(chara != charb for chara, charb in zip(linea, lineb))
		if diff > 1:
			break

	return diff

def find_reflections(grid):
	height = len(grid)
	imperfect = 0

	for size in range(1, height // 2 + 1):
		a = grid[:size]
		b = grid[size:2 * size][::-1]
		diff = count_differences(a, b)

		if  diff == 1:
			imperfect = size
			break

		

		a = grid[height - 2 * size:height - size]
		b = grid[height - size:][::-1]
		diff = count_differences(a, b)

		if diff == 1:
			imperfect = height - size
			break

	return imperfect


# Open the first argument as input or use stdin if no arguments were given
with open("../input.txt") as f:
    grids = f.read().split('\n\n')

ans = 0

for raw_grid in grids:
	g = raw_grid.splitlines()

	imperfect = find_reflections(g)
	ans += 100 * imperfect

	imperfect = find_reflections(transpose(g))
	ans += imperfect

print(ans)