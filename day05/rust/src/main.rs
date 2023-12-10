use std::collections::HashMap;
use std::fs::File;

use std::io::{BufRead, BufReader};

fn process_vector(vec: &Vec<String>, key: &str) -> Vec<HashMap<String, String>> {
    let mut result: Vec<HashMap<String, String>> = Vec::new();

    for i in 1..vec.len() {
        let mut j = i + 1;
        if vec[i].contains(key) {
            while j < vec.len() && vec[j].chars().next().map_or(false, |c| c.is_digit(10)) {
                let mut dict = HashMap::new();

                // Split the element by spaces and get the substrings
                if let Some(source_start) = vec[j].split_whitespace().nth(1) {
                    // Do something with the source_start value
                    dict.insert("source_start".to_string(), source_start.to_string());
                }

                if let Some(new_start) = vec[j].split_whitespace().nth(0) {
                    // Do something with the new_start value
                    dict.insert("new_start".to_string(), new_start.to_string());
                }

                if let Some(range_len) = vec[j].split_whitespace().nth(2) {
                    // Do something with the range_len value
                    dict.insert("range_len".to_string(), range_len.to_string());
                }

                j += 1;
                result.push(dict);
            }
        }
    }

    result
}


fn main() {
    // Open the file
    let file = File::open("../input.txt").unwrap();
    let reader = BufReader::new(&file);

    //takes the first line

    let mut vec = Vec::new();
    for line in reader.lines() {
        let line = line.unwrap();

        //if the line is not empty
        if line.is_empty() {
            continue;
        }
        vec.push(line);
    }
    
    // Assuming 'vec' is a Vec<String>
let tmp: Vec<&str> = vec[0].split(' ').collect();

// Seeds are the tmp except for the first element
let mut seeds = Vec::new();
for i in 1..tmp.len() {
    // Check if the substring is empty
    if tmp[i] == "" {
        println!("Empty line");
        continue;
    }
    // Parse the substring as u64
    match tmp[i].parse::<u64>() {
        Ok(seed) => seeds.push(seed),
        Err(err) => {
            println!("Error parsing seed: {}", err);
            // Handle the error as needed
        }
    }
}

    let seed_to_soil = process_vector(&vec, "seed-to");
    let soil_to_fertilize = process_vector(&vec, "soil-to");
    let fertilizer_to_water = process_vector(&vec, "fertilizer-to");
    let water_to_light = process_vector(&vec, "water-to");
    let light_to_temperature = process_vector(&vec, "light-to");
    let temperature_to_umidity = process_vector(&vec, "temperature-to");
    let umidity_to_location = process_vector(&vec, "umidity-to");


    //create an array of all the previous mapping 
    let mut mappings = Vec::new();
    mappings.push(seed_to_soil);
    mappings.push(soil_to_fertilize);
    mappings.push(fertilizer_to_water);
    mappings.push(water_to_light);
    mappings.push(light_to_temperature);
    mappings.push(temperature_to_umidity);
    mappings.push(umidity_to_location);

    let mut result = Vec::new();

    for mut seed in seeds {
        
        for map in mappings.iter() {
            for m in map.iter() {
                    if seed >= m["source_start"].parse::<u64>().unwrap() && seed < m["source_start"].parse::<u64>().unwrap() + m["range_len"].parse::<u64>().unwrap() {
                        seed = m["new_start"].parse::<u64>().unwrap() + seed - m["source_start"].parse::<u64>().unwrap();
                        break;
                }   
        
        }

}   
        result.push(seed);
    }
    
    if let Some(min) = result.iter().cloned().min() {
    println!("The minimum value is {}", min);
}
}
