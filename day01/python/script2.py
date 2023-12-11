
#function that check if the string contains a number spelled, then replace all of its occurrences with the actual number
def checkForNumAsStr(line,  n):

    return checkForNumAsStr(line.replace(num[int(n)], num[int(n)][0] + n + num[int(n)][-1]) , n) if num[int(n)] in line else line


#spell the numbers
num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #for each line
    for line in lines:
        for i in range(len(num)):
            line = checkForNumAsStr(line, str(i))

        firstNumber, lastNumber = ' ', ' '

        #for every char in the line
        for char in line:

            if char.isnumeric():
                #variable will be replaced is necessary
                lastNumber = char
                
                #if firstNumber is not a number, then check if we can set the current char as first number
                if (not firstNumber.isnumeric()):
                    firstNumber = char

        tot += int(str(firstNumber) + str(lastNumber))

print(tot)           

