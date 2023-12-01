#open input file

with open('day1/input.txt') as f:
    lines = f.readlines()

    tot = 0

    #for each line
    for line in lines:
        firstNumber = line[0]
        #take the length of the line as number of digits
        lastNumber = 'a'
                

        #for every digit in the line
        for digit in line:
            print("Char: ", digit, " bool: ", digit.isnumeric())

            if digit.isnumeric():
                #variable will be replaced is necessary
                lastNumber = digit
                
            #if firstNumber is not a number, then check if we can set the current digit as first number
            if (not firstNumber.isnumeric()) and digit.isnumeric():
                firstNumber = digit

            
            print("Last number: ", lastNumber)
        print(firstNumber, " ", lastNumber)
        tmpNum = str(firstNumber) + str(lastNumber)
        tot += int(tmpNum)

    print(tot)
