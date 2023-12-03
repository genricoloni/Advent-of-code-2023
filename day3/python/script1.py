sym = ['#', '*', '+', '$', '@', '%', '&', '-', '/', '=' ]


#open the input
with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #transform lines in a matrix
    matrix = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        line = list(line)
        matrix.append(line)


    for j in range(len(matrix)):
        #print(matrix[j])
        firstIndex = -1
        lastIndex = -1

        tmpnum = ''

        for i in range(len(matrix[j])):

            if matrix[j][i].isnumeric():
                tmpnum += str(matrix[j][i])
                lastIndex = i

                if firstIndex == -1:
                    firstIndex = i
                
            
            if (((not matrix[j][i].isnumeric()) and lastIndex != -1) or (i+1) == len(matrix[j])) and (lastIndex != -1 and firstIndex != -1):
                #check if there are symbols near the number
                # check for upper e down lines, and diagonals of first and last element
                print("checki for prev",tmpnum, firstIndex, lastIndex)

                prev = ''


                #check in the previous line
                if not (j -1 < 0):
                    #it the previous index is not negative
                    #add to prev char at same index of the current line
                    for k in range(firstIndex, lastIndex+1):
                        
                        #append to the string
                        prev += str(matrix[j-1][k])
                        

                    #edge case when the first index is at the beginning of the line
                    if not (firstIndex - 1 < 0):
                        #it the previous index is not negative
                        #append to the string
                        prev += str(matrix[j-1][firstIndex-1])

                    #edge case when the last index is at the end of the line
                    if not (lastIndex + 1 >= len(matrix[j-1])):
                        #it the previous index is not negative
                        print("prev diagonal:", matrix[j-1][lastIndex+1])
                        #append to the string
                        prev += str(matrix[j-1][lastIndex+1])

                #check the current line
                #edge case when element is the first element of the line
                if not (firstIndex - 1 < 0):
                    #it the previous index is not negative
                    print("current diagonal:", matrix[j][firstIndex-1])
                    #append to the string
                    prev += str(matrix[j][firstIndex-1])
                    print("current after:", prev)   

                #edge case when element is the last element of the line
                if not (lastIndex + 1 >= len(matrix[j])):
                    #it the previous index is not negative
                    #append to the string
                    prev += str(matrix[j][lastIndex+1])

                #check in the next line
                if not (j + 1 >= len(matrix)):
                    #it the previous index is not negative
                    for k in range(firstIndex, lastIndex+1):
                        
                        #append to the string
                        prev += str(matrix[j+1][k])
                        

                    #edge case when the first index is at the beginning of the line
                    if not (firstIndex - 1 < 0):
                        #it the previous index is not negative
                        #append to the string
                        prev += str(matrix[j+1][firstIndex-1])

                    #edge case when the last index is at the end of the line
                    if not (lastIndex + 1 >= len(matrix[j+1])):
                        #it the previous index is not negative
                        print("next diagonal:", matrix[j+1][lastIndex+1])
                        #append to the string
                        prev += str(matrix[j+1][lastIndex+1])         

                print(prev)

                for elem in prev:
                    if elem in sym:
                        tot += int(tmpnum)
                        break


                firstIndex = -1
                lastIndex = -1

                tmpnum = ''

    print(tot)


