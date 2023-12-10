fn part1(){
    //open input file
    let input = std::fs::read_to_string("../../input.txt").expect("Unable to open file");

    //split input into lines
    let lines = input.lines();

    let mut tot = 0;

    for line in lines {
        println!("{}", line);

        let mut firstNumber = 'a';
        let mut lastNumber = 'a';
        
        for c in line.chars() {
            if !firstNumber.is_numeric() {
                firstNumber = c;
            
            }
            if c.is_numeric(){
                lastNumber = c;
            }
            
        }
        //string concatenation
        let mut result = String::new();
        result.push(firstNumber);
        result.push(lastNumber);


        //convert to integer
        let mut n = result.parse::<i32>().unwrap();
        tot += n;
    }
    println!("{}", tot);
}

fn check_for_num_as_string(line: &str, num_as_string: &str, i: i32) -> String {
    let mut result = String::new();

    // take the first and last letter of num_as_string
    let first_letter = num_as_string.chars().nth(0).unwrap();
    let last_letter = num_as_string.chars().nth(num_as_string.len() - 1).unwrap();

    // push the first letter
    result.push(first_letter);

    // push the number
    result.push_str(i.to_string().as_str());

    // push the last letter
    result.push(last_letter);

    // replace all occurrences of num_as_string with result in line
    let modified_line = line.replace(num_as_string, result.as_str());

    modified_line
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
        let mut result = String::new();
        result.push(first_number);
        result.push(last_number);

        // convert to integer
        let n = result.parse::<i32>().unwrap();
        tot += n;
    }

    println!("{}", tot);
}


fn main() {

    
    //part1();
    part2();


}
