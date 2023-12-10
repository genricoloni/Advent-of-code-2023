use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // Define a vector of symbols to check for in the matrix
    let symbols = vec!['#', '*', '+', '$', '@', '%', '&', '-', '/', '='];

    // Open the input file
    let file = File::open("../input.txt")?;
    let reader = io::BufReader::new(file);

    // Create a matrix to store characters from the input file
    let mut matrix = Vec::new();

    // Transform lines into a matrix
    for line in reader.lines() {
        // Convert each line into a vector of characters and trim whitespace
        let mut row: Vec<char> = line?.trim().chars().collect();
        // Add the row to the matrix
        matrix.push(row);
    }

    // Initialize a variable to store the total sum of numeric sequences
    let mut total = 0;

    // Iterate over each row in the matrix
    for j in 0..matrix.len() {
        // Initialize variables to track the start and end indices of numeric sequences
        let mut first_index = None;
        let mut last_index = None;
        // Temporary variable to accumulate numeric characters
        let mut tmp_num = String::new();

        // Iterate over each character in the current row
        for i in 0..matrix[j].len() {
            // Check if the character is numeric
            if matrix[j][i].is_numeric() {
                // Accumulate numeric characters into tmp_num
                tmp_num.push(matrix[j][i]);
                // Update last_index
                last_index = Some(i);

                // Update first_index if not set
                if first_index.is_none() {
                    first_index = Some(i);
                }
            }

            // Check if the current character is non-numeric or it's the last character in the row
            if ((!matrix[j][i].is_numeric() && last_index.is_some())
                || (i + 1 == matrix[j].len()))
                && (last_index.is_some() && first_index.is_some())
            {
                // Check for symbols in adjacent lines and diagonals
                let mut prev = String::new();

                // Check the row above
                if j > 0 {
                    for k in first_index.unwrap()..=last_index.unwrap() {
                        prev.push(matrix[j - 1][k]);
                    }

                    // Edge cases for the row above
                    if first_index.unwrap() > 0 {
                        prev.push(matrix[j - 1][first_index.unwrap() - 1]);
                    }
                    if last_index.unwrap() + 1 < matrix[j - 1].len() {
                        prev.push(matrix[j - 1][last_index.unwrap() + 1]);
                    }
                }

                // Check the current row
                if first_index.unwrap() > 0 {
                    prev.push(matrix[j][first_index.unwrap() - 1]);
                }
                if last_index.unwrap() + 1 < matrix[j].len() {
                    prev.push(matrix[j][last_index.unwrap() + 1]);
                }

                // Check the row below
                if j + 1 < matrix.len() {
                    for k in first_index.unwrap()..=last_index.unwrap() {
                        prev.push(matrix[j + 1][k]);
                    }

                    // Edge cases for the row below
                    if first_index.unwrap() > 0 {
                        prev.push(matrix[j + 1][first_index.unwrap() - 1]);
                    }
                    if last_index.unwrap() + 1 < matrix[j + 1].len() {
                        prev.push(matrix[j + 1][last_index.unwrap() + 1]);
                    }
                }

                // Print the characters being considered for each numeric sequence

                // Check if any character in prev is in the symbols vector
                for elem in prev.chars() {
                    if symbols.contains(&elem) {
                        // If a symbol is found, parse tmp_num to an integer and add to the total
                        total += tmp_num.parse::<i32>().unwrap();
                        break;
                    }
                }

                // Reset indices and tmp_num for the next numeric sequence
                first_index = None;
                last_index = None;
                tmp_num.clear();
            }
        }
    }

    // Print the total sum of numeric sequences
    println!("{}", total);

    Ok(())
}
