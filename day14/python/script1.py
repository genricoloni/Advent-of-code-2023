with open("../input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    matrix = [[num for num in line] for line in lines]
   

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


    tot = 0
    for i in range(len(matrix)):
        #count how much 'O' there are in the row
        count = matrix[i].count('O')
        tot += count*(len(matrix[i])-i)

    print(tot)

    