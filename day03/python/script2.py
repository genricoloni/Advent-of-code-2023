with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #transform lines in a matrix
    matrix = [list(line.strip()) for line in lines]


    for j in range(len(matrix)):
        
        index = -1
        for i in range(len(matrix[j])):
            numbers = []

            if matrix[j][i] == '*':

                index = i

                #previous line if exists
                if j - 1 >= 0:
                    #find all the numbers in the previous line
                    n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                    
                    for k in range(len(matrix[j-1])):

                        if matrix[j-1][k].isnumeric():
                            n['number'] += str(matrix[j-1][k])
                            if n['firstIndex'] == -1:
                                n['firstIndex'] = k
                            n['lastIndex'] = k
                        else:
                            #it's not a number, check if the number is 'near' the symbol
                            if index in range(n['firstIndex']-1, n['lastIndex']+2):
                                numbers.append(n)
                                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                            else:
                                #means that the number is not 'near' the symbol
                                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                    else:
                        #when we arrive at the end of the array
                        i#check if the current number is valid
                        if  index in range(n['firstIndex']-1, n['lastIndex']+2):
                            numbers.append(n)
                            n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}



                #current line 
                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                
                #check the elem to the left of the *
                if matrix[j][index - 1].isnumeric():
                    #check backwards until the beginning of the array
                    for k in range(index - 1, -1, -1):
                        
                        if matrix[j][k].isnumeric():
                            n['number'] += str(matrix[j][k])
                            
                        if (not(matrix[j][k].isnumeric()) or (k == 0)) and( n['number'] != -1):
                            n['number'] = n['number'][::-1]
                            numbers.append(n)
                            break

                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}

                #check the elem to the right of the *
                if index + 1 < len(matrix[j]) and matrix[j][index + 1].isnumeric():
                    #check backwards until the beginning of the array
                    for k in range(index + 1, len(matrix[j])):
                        
                        if matrix[j][k].isnumeric():
                            n['number'] += str(matrix[j][k])
                            
                        if not(matrix[j][k].isnumeric())  :
                            numbers.append(n)
                            
                            n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                            # because the number is finished
                            break


                #check for the next line
                if j + 1 < len(matrix):
                    #find all the numbers in the previous line
                    n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                    
                    for k in range(len(matrix[j+1])):
                        if matrix[j+1][k].isnumeric():
                            n['number'] += str(matrix[j+1][k])
                            if n['firstIndex'] == -1:
                                n['firstIndex'] = k
                            n['lastIndex'] = k
                        else:
                      
                            #if the number is 'near' the symbol 
                            if index in range(n['firstIndex']-1, n['lastIndex']+2):
                                numbers.append(n)
                                

                            n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
            
            #multiply all the number of numbers

                if len(numbers) ==2:
                    prod = 1
                    for elem in numbers:
                        prod *= int(elem['number'])

                    tot += prod

    print(tot)


    


