#script for the first part it's correct for the second one also, but it' pretty slow
#this script do the exactly same thing of the first one, but it's faster

with open("../input.txt") as f:
    lines = f.readlines()

    #for part2, just de comment next line
    lines = [line.replace(" ", "") for line in lines]
    
    times, distances = [list(map(int, line.split(":")[1].strip().split("   "))) for line in lines]

tot = 1

for time, distance in zip(times, distances):
    num_of_record_breaks = sum(1 for j in range(1, time) if j * (time - j) > distance)
    print(num_of_record_breaks)
    tot *= num_of_record_breaks

print(tot)

