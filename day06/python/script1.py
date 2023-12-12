with open("../input.txt") as f:
    lines = f.readlines()

    #for part2, just de comment next line
    
    times = list(lines[0].split(":")[1].strip().split("   "))
    distances = list(lines[1].split(":")[1].strip().split("   "))

    tot = 1

    for i in range(0, len(times)):
        nunOfRecordBreak = 0
        time = int(times[i])
        distance = int(distances[i])

        for j in range(1, time):
            distance = j * (time - j)

            nunOfRecordBreak = nunOfRecordBreak + 1 if distance > int(distances[i]) else nunOfRecordBreak
            
        tot *= nunOfRecordBreak

    print(tot)
