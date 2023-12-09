use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashSet;

fn pt1(){
        // Open file
        let file = File::open("../input.txt").unwrap();
        let buf_reader = BufReader::new(file);
    
        let mut tot = 0;
    
        for line in buf_reader.lines() {
            let line = line.unwrap();
    
            // Split line by '|'
            let parts: Vec<&str> = line.split('|').collect();
    
            // Split the first part by ':'
            let parts2: Vec<&str> = parts[0].split(':').collect();
            let winning_numbers: HashSet<&str> = parts2[1].split_whitespace().collect();
    
            let numbers_to_check: HashSet<&str> = parts[1].split_whitespace().collect();
    
            let count = winning_numbers.intersection(&numbers_to_check).count();
    
            let tmp_points = if count == 0 {
                0
            } else {
                2u32.wrapping_pow(count as u32 - 1)
            };
    
            tot += tmp_points;
        }
    
        println!("{}", tot);
}

fn pt2(){

        // Open file
        let file = File::open("../input.txt").unwrap();
        let buf_reader = BufReader::new(file);
    
        let mut tot = 0;

        let mut index = 0;

        let lines: Vec<_> = buf_reader.lines().collect();

        let mut instances: Vec<i32> = vec![1; lines.len()];
    
        for line in lines {
            let line = line.unwrap();
    
            // Split line by '|'
            let parts: Vec<&str> = line.split('|').collect();
    
            // Split the first part by ':'
            let parts2: Vec<&str> = parts[0].split(':').collect();
            let winning_numbers: HashSet<&str> = parts2[1].split_whitespace().collect();
    
            let numbers_to_check: HashSet<&str> = parts[1].split_whitespace().collect();
    
            let win = winning_numbers.intersection(&numbers_to_check).count();
    
            for i in index+1..index+1+win{
                instances[i] += instances[index]
            }
            index += 1;
        }
    
    //print the sum of all the instances
    for i in instances{
        tot += i;
    }

    println!("{}", tot);
}


fn main() {
    pt1();
    pt2();
}
