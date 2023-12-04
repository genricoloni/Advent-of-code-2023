with open('../input.txt') as f:
    lines = f.readlines()

    instancies = [1]*len(lines)

    print(instancies)
    
    tot = 0

    index = 0

    for line in lines:

        
        line = line.strip()
        parts = line.split(":")[1].split("|")

        winningNumbers = set(parts[0].split())
        myNumbers = set(parts[1].split())

        win = len(winningNumbers.intersection(myNumbers))

        print("For game", index+1, "you have", win, "win")

        for i in range(index+1, index+1+win):
            print("Increasing copies of the card", i)
            instancies[i] += instancies[index]
            
        index += 1
    #print the sum of instancies
    print(instancies)
    print(sum(instancies))