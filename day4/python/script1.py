with open('../input.txt') as f:
    lines = f.readlines()

    

    tot = 0

    for line in lines:
        line = line.strip()
        parts = line.split(":")[1].split("|")

        winningNumbers = set(parts[0].split())
        myNumbers = set(parts[1].split())

        tmpPoints = 0


        for number in myNumbers:
            if number in winningNumbers:
                tmpPoints = 1 if tmpPoints == 0 else tmpPoints*2

        tot += tmpPoints

    print(tot)