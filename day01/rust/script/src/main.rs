fn part1(){
    //open input file
    let input = std::fs::read_to_string("../../input.txt").expect("Unable to open file");

    //split input into lines
    let lines = input.lines();

    let mut tot = 0;

    for line in lines {

        let mut firstNumber = ' ';
        let mut lastNumber = ' ';
        
        for c in line.chars() {
            if !firstNumber.is_numeric() {
                firstNumber = c;
            
            }
            if c.is_numeric(){
                lastNumber = c;
            }
            
        }
        //string concatenation
        tot  += format!("{}{}", firstNumber, lastNumber).parse::<i32>().unwrap();

    }
    println!("{}", tot);
}

fn check_for_num_as_string(line: &str, num_as_string: &str, i: i32) -> String {
    // Take the first and last letters of num_as_string
    let first_letter = num_as_string.chars().next().unwrap();
    let last_letter = num_as_string.chars().last().unwrap();

    // Create the replacement string

    // Replace all occurrences of num_as_string with replacement in line
    line.replace(num_as_string, &format!("{}{}{}", first_letter, i, last_letter))
}



fn part2() {
    let num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    // open input file
    let input = std::fs::read_to_string("../../input.txt").expect("Unable to open file");

    // split input into lines
    let lines = input.lines();

    let mut tot = 0;

    for line in lines {
        // Create a new variable to store the modified line
        let mut modified_line = line.to_string();

        // Replace words with numbers in the line
        for i in 0..num.len() {
            modified_line = check_for_num_as_string(&modified_line, num[i], i as i32);
        }

        let mut first_number = 'a';
        let mut last_number = 'a';

        for c in modified_line.chars() {
            if !first_number.is_numeric() {
                first_number = c;
            }
            if c.is_numeric() {
                last_number = c;
            }
        }

        // string concatenation
        tot += format!("{}{}", first_number, last_number).parse::<i32>().unwrap();
    }

    println!("{}", tot);
}


fn main() {

    
    part1();
    part2();


}
