with open('../input.txt') as f:
    lines = f.readlines()

    instancies = [1]*len(lines)

    index = 0

    for line in lines:
        
        line = line.strip()
        parts = line.split(":")[1].split("|")

        winningNumbers = set(parts[0].split())
        myNumbers = set(parts[1].split())

        win = len(winningNumbers.intersection(myNumbers))

        for i in range(index+1, index+1+win):
            instancies[i] += instancies[index]
            
        index += 1
    #print the sum of instancies
    print(sum(instancies))