with open("../input.txt") as f:
    lines = f.readlines()

    #for part2, just de comment next line
    lines = [line.replace(" ", "") for line in lines]
    
    times = list(lines[0].split(":")[1].strip().split("   "))
    distances = list(lines[1].split(":")[1].strip().split("   "))

    tot = 1

    for i in range(0, len(times)):
        nunOfRecordBreak = 0
        time = int(times[i])
        distance = int(distances[i])

        for j in range(1, time):
            remainingTime = time - j

            distance = j * remainingTime

            if distance > int(distances[i]):
                nunOfRecordBreak += 1
            
        print(nunOfRecordBreak)
        tot *= nunOfRecordBreak

    print(tot)
