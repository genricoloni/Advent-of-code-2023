

#open the input
with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #create the collection to check
    toCheck = { "red" : 12,
                "green" : 13,
                "blue" : 14}

    for line in lines:
        #divide the line by ":"
        line = line.replace("\n","")
        line = line.split(":")
        id = line[0].split(" ")[1]

        sets = line[1].split(";")

        points = {  "red"   : 0,
                    "green" : 0,
                    "blue"  : 0}

        for s in sets:
            s.strip()
            extraction = s.split(",")
            for e in extraction:
                #remove the first char which is a space
                e = e[1:]
                e = e.split(" ")
                
                #take e[1] and check if the number shown is greater than the one stored in dictionary for the same color
                if int(e[0]) > points[e[1]]:
                    points[e[1]] = int(e[0])


        print("ID:\t", id, "points: ", points["red"],  points["green"],  points["blue"])

        if points["red"] <= toCheck["red"] and points["green"] <= toCheck["green"] and points["blue"] <=toCheck["blue"]:
            print("Game", id, "is eligible")
            tot += int(id)


    print(tot)

        


