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
        
        index = -1
        for i in range(len(matrix[j])):
            numbers = []

            if matrix[j][i] == '*':

                index = i

                
                
                #build a list of dictionaries

                

                tmpIndex = 0
                #now search for numbers "connected" with this element

                #previous line if exists
                if j - 1 >= 0:
                    #find all the numbers in the previous line
                    n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                    
                    for k in range(len(matrix[j-1])):
                        print("analyze:", matrix[j-1][k])

                        if matrix[j-1][k].isnumeric():
                            n['number'] += str(matrix[j-1][k])
                            if n['firstIndex'] == -1:
                                n['firstIndex'] = k
                            n['lastIndex'] = k
                        else:
                            #it's not a number, check if the number is 'near' the symbol
                            if index in range(n['firstIndex']-1, n['lastIndex']+2):
                                numbers.append(n)
                                print("added")
                                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                            else:
                                #means that the number is not 'near' the symbol
                                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}
                                continue
                    else:
                        #when we arrive at the end of the array
                        i#check if the current number is valid
                        if n['number'] != -1 and index in range(n['firstIndex']-1, n['lastIndex']+2):
                            numbers.append(n)
                            print("added")
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
                            #print all the elements of numbers
                            break

                n = {'number': '', 'firstIndex': -1, 'lastIndex': -1}

                #check the elem to the right of the *
                if index + 1 < len(matrix[j]) and matrix[j][index + 1].isnumeric():
                    print("to the right:", matrix[j][index+1:] )
                    #check backwards until the beginning of the array
                    for k in range(index + 1, len(matrix[j])):
                        
                        if matrix[j][k].isnumeric():
                            n['number'] += str(matrix[j][k])
                            
                        if not(matrix[j][k].isnumeric())  :
                            numbers.append(n)
                            #print all the elements of numbers
                            
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
                            tmpIndex += 1
            
            #multiply all the number of numbers
                print("found", len(numbers), "numbers")
                print(numbers)

                if len(numbers) ==2:
                    print("for * in line", j)
                    prod = 1
                    for elem in numbers:
                        print("number is", elem['number'])
                        prod *= int(elem['number'])
                    print("product is", prod)

                    tot += prod

    print(tot)


    


