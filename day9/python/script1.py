with open("../input.txt") as f:
    lines = f.read().splitlines()

    tot = 0

    for line in lines:
        newline = list(line.split(" "))
        
        num = 0

        while any(newline):
            num += int(newline[-1])

            result = []

            for i in range(1, len(newline)):
                result.append(int(newline[i]) - int(newline[i - 1]))
            
            newline = result
            

        tot += num

    print(tot)
