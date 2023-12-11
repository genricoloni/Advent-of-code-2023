#open input file

with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #for each line
    for line in lines:
        firstNumber, lastNumber = ' ', ' '
        #take the length of the line as number of digits

        #for every digit in the line
        for digit in line:

            if digit.isnumeric():
                #variable will be replaced is necessary
                lastNumber = digit
                
            #if firstNumber is not a number, then check if we can set the current digit as first number
                if not firstNumber.isnumeric():
                    firstNumber = digit

        tot += int(str(firstNumber) + str(lastNumber))

    print(tot)