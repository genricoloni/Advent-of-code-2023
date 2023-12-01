
#function that check if the string contains a number spelled, then replace all of its occurrences with the actual number
def checkForNumAsStr(line, numAsStr, num):
    while numAsStr in line:
        #double the first and the last char of the wirtten number
        toReplace = numAsStr[0] + num + numAsStr[-1]

        line = line.replace(numAsStr, toReplace)
    return line

#spell the numbers
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('day1/input.txt') as f:
    lines = f.readlines()

    tot = 0

    #for each line
    for line in lines:
        for i in range(len(num)):
            line = checkForNumAsStr(line, num[i], str(i))

        firstNumber = line[0]
        #take the length of the line as number of digits
        lastNumber = ''
                

        #for every digit in the line
        for digit in line:

            if digit.isnumeric():
                #variable will be replaced is necessary
                lastNumber = digit
                
            #if firstNumber is not a number, then check if we can set the current digit as first number
            if (not firstNumber.isnumeric()) and digit.isnumeric():
                firstNumber = digit

        tmpNum = str(firstNumber) + str(lastNumber)
        tot += int(tmpNum)

    print(tot)           

