with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    for line in lines:
        line = line.strip()
        parts = line.split(":")[1].split("|")

        winningNumbers = set(parts[0].split())
        myNumbers = set(parts[1].split())

        commonNumbers = winningNumbers.intersection(myNumbers)

        tmpPoints = 2**(len(commonNumbers) - 1) if commonNumbers else 0

        tot += tmpPoints

    print(tot)
