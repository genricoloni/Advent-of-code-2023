with open("../input.txt", "r") as f:
    document = f.readlines()

    #first line is for seeds
    l = document[0].strip().split(":")[1].strip().split(" ")

    document = document[1:]

    #lines became an array 
    lines = [line.strip() for line in document]

    global seedToSoil, soilToFertilize, fertilizeToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation
    
    seedToSoil = []
    
    soilToFertilize = []

    fertilizeToWater = []

    waterToLight = []

    lightToTemperature = []

    temperatureToHumidity = []

    humidityToLocation = []

    for i in range(len(lines)):
        if 'seed-to-soil' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])

                seedToSoil.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort 
            seedToSoil.sort(key=lambda x: x[0])

        elif 'soil-to-fertilize' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])

                soilToFertilize.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort
            soilToFertilize.sort(key=lambda x: x[0])

                

        elif 'fertilizer-to-water' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])

                fertilizeToWater.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort
            fertilizeToWater.sort(key=lambda x: x[0])


        elif 'water-to-light' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])
                waterToLight.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort
            waterToLight.sort(key=lambda x: x[0])


        elif 'light-to-temperature' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])
                lightToTemperature.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort   
            lightToTemperature.sort(key=lambda x: x[0])


        elif 'temperature-to-humidity' in lines[i]:

            j = i + 1

            while lines[j].strip() != '':
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])
                temperatureToHumidity.append((sourceStart, newStart, rangeLen))

                j += 1
            #sort
            temperatureToHumidity.sort(key=lambda x: x[0])



        elif 'humidity-to-location' in lines[i]:

            j = i + 1

            while lines[j].strip() != '' or j != 0:
                sourceStart = int(lines[j].split()[1])
                newStart = int(lines[j].split()[0])
                rangeLen = int(lines[j].split()[2])
                humidityToLocation.append((sourceStart, newStart, rangeLen))

                j += 1

                if j >= len(lines):
                    break
            #sort
            humidityToLocation.sort(key=lambda x: x[0])


for i in range(len(l)):
    l[i] = int(l[i])

    mappings = [seedToSoil, soilToFertilize, fertilizeToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]

    for mapping in mappings:

        #build the entire mapping using the range
        for elem in mapping:
            sourceStart, newStart, rangeLen = elem
            if l[i] >= sourceStart and l[i] < sourceStart + rangeLen:
                l[i] = newStart + (l[i] - sourceStart)
                break
               

print(min(l))


