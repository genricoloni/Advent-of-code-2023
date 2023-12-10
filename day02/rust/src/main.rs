use std::collections::HashMap;

fn part1() {
    // Open input file
    let input = std::fs::read_to_string("../input.txt").expect("Unable to open file");

    // Dictionary
    let mut dict = HashMap::new();
    dict.insert("red", 12);
    dict.insert("green", 13);
    dict.insert("blue", 14);

    let mut tot = 0;

    for line in input.lines() {
        // Split the line by :
        let mut split = line.split(":");

        // Get game info
        let info = split.next().unwrap().trim();

        // Get game data
        let game = split.next().unwrap().trim();

        // Extract id from info
        let _id = info.split(" ").nth(1).unwrap();

        let sets = game.split(";").collect::<Vec<&str>>();

        let mut dict_per_line = HashMap::new();
        dict_per_line.insert("red", 0);
        dict_per_line.insert("green", 0);
        dict_per_line.insert("blue", 0);

        for set in sets {
            let _set = set.trim();

            let _set = _set.split(",").collect::<Vec<&str>>();

            for s in _set {
                let _s = s.trim();

                let color = _s.split(" ").nth(1).unwrap();

                // Parse points as an integer
                let points = _s.split(" ").nth(0).unwrap().parse::<i32>();

                match points {
                    Ok(parsed_points) => {

                        // Access the dict using color as the key
                        if let Some(current_points) = dict_per_line.get_mut(color) {
                            // Compare and update the value if necessary
                            if parsed_points > *current_points {
                                *current_points = parsed_points;
                            }
                        }
                    }
                    Err(err) => {
                        eprintln!("Error parsing points as integer: {}", err);
                    }
                }
            }
        }
        //check if values in dict_per_line are lower than those in dict
        // Check if values in dict_per_line are lower than those in dict
        if dict_per_line.get("red").unwrap_or(&0) <= dict.get("red").unwrap_or(&0)
        && dict_per_line.get("blue").unwrap_or(&0) <= dict.get("blue").unwrap_or(&0)
        && dict_per_line.get("green").unwrap_or(&0) <= dict.get("green").unwrap_or(&0)
        {
        tot += _id.parse::<i32>().unwrap();
        }


    }
    println!("Total: {}", tot);

}


fn part2() {
    // Open input file
    let input = std::fs::read_to_string("../input.txt").expect("Unable to open file");

    // Dictionary
    let mut dict = HashMap::new();
    dict.insert("red", 12);
    dict.insert("green", 13);
    dict.insert("blue", 14);

    let mut tot = 0;

    for line in input.lines() {
        // Split the line by :
        let mut split = line.split(":");

        // Get game info
        let info = split.next().unwrap().trim();

        // Get game data
        let game = split.next().unwrap().trim();

        // Extract id from info
        let id = info.split(" ").nth(1).unwrap();

        let sets = game.split(";").collect::<Vec<&str>>();

        let mut dict_per_line = HashMap::new();
        dict_per_line.insert("red", 0);
        dict_per_line.insert("green", 0);
        dict_per_line.insert("blue", 0);

        for set in sets {
            let _set = set.trim();

            let _set = _set.split(",").collect::<Vec<&str>>();

            for s in _set {
                let _s = s.trim();

                let color = _s.split(" ").nth(1).unwrap();

                // Parse points as an integer
                let points = _s.split(" ").nth(0).unwrap().parse::<i32>();

                match points {
                    Ok(parsed_points) => {

                        // Access the dict_per_line using color as the key
                        if let Some(current_points) = dict_per_line.get_mut(color) {
                            // Compare and update the value if necessary
                            if parsed_points > *current_points {
                                *current_points = parsed_points;
                            }
                        }
                    }
                    Err(err) => {
                        eprintln!("Error parsing points as integer: {}", err);
                    }
                }
            }
        }

        // Check if values in dict_per_line are lower than those in dict
        tot += (dict_per_line.get("red").unwrap() * dict_per_line.get("green").unwrap() * dict_per_line.get("blue").unwrap()) ;
    }
    println!("Total: {}", tot);
}




fn main() {
    print!("Part 1-> ");
    part1();
    print!("Part 2-> ");
    part2();


    
}
