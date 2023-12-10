import multiprocessing

# Function that applies transformations to a number
def resultOf(number):
    # List of transformation mappings
    mappings = [seedToSoil, soilToFertilize, fertilizeToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]
    
    # Apply each mapping
    for mapping in mappings:
        for elem in mapping:
            sourceStart, newStart, rangeLen = elem
            # Check if the number falls within the range of the mapping
            if sourceStart <= number < sourceStart + rangeLen:
                # Apply the transformation
                number = newStart + (number - sourceStart)
                break
    return number

# Function executed by each process
def worker(seed, lenRange, result_queue):
    min_value = resultOf(seed)

    # Iterate over the range of the seed
    for j in range(1, lenRange):
        new_number = seed + j
        new_result = resultOf(new_number)
        # Update the minimum value if the new result is smaller
        min_value = min(new_result, min_value)

    result_queue.put(min_value)

if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        document = f.readlines()

        # Extract seed from the first line of the document
        seed = document[0].strip().split(":")[1].strip().split(" ")
        print(seed)

        # Remove the first line and extract lines from the document
        document = document[1:]
        lines = [line.strip() for line in document]

        # Declare global variables for transformation mappings
        global seedToSoil, soilToFertilize, fertilizeToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation
        
        # Initialize lists for each type of transformation
        seedToSoil = []
        soilToFertilize = []
        fertilizeToWater = []
        waterToLight = []
        lightToTemperature = []
        temperatureToHumidity = []
        humidityToLocation = []

        # Iterate over lines to extract transformation data
        for i in range(len(lines)):
            if 'seed-to-soil' in lines[i]:
                j = i + 1
                # Extract seed-to-soil transformations
                while lines[j].strip() != '':
                    sourceStart = int(lines[j].split()[1])
                    newStart = int(lines[j].split()[0])
                    rangeLen = int(lines[j].split()[2])
                    seedToSoil.append((sourceStart, newStart, rangeLen))
                    j += 1
                # Sort the transformations
                seedToSoil.sort(key=lambda x: x[0])
            
            # Repeat the same block for other types of transformations

    # Extract seeds and length ranges from the seed list
    l = seed
    seeds = [int(l[i]) for i in range(0, len(l), 2)]
    lenRange = [int(l[i]) for i in range(1, len(l), 2)]

    # Initialize multiprocessing structures
    result_queue = multiprocessing.Queue()
    processes = []

    # Iterate over seeds and start a process for each
    for i in range(len(seeds)):
        seed = seeds[i]
        len_range = lenRange[i]

        # Create a process for each seed
        process = multiprocessing.Process(target=worker, args=(seed, len_range, result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Retrieve minimum results from the queue
    min_values = []
    while not result_queue.empty():
        min_values.append(result_queue.get())

    # Print the minimum result
    print("Minimum result:", min(min_values))
