 fn spelled_digit_occurrences(digit: &str, str: &str) -> (Option<usize>, Option<usize>) {
     let first_occurrence: Option<usize> = str.find(digit);
     let last_occurrence: Option<usize> = str.rfind(digit);
     (first_occurrence, last_occurrence)
 }

 fn convert_spelled_digit(digit: &str) -> usize {
     match digit {
         "zero" => 0,
         "one" => 1,
         "two" => 2,
         "three" => 3,
         "four" => 4,
         "five" => 5,
         "six" => 6,
         "seven" => 7,
         "eight" => 8,
         "nine" => 9,
         _ => panic!("Invalid digit!")
     }
 }

fn main() {
    let input: Vec<_> = include_str!("input.txt")
        .split('\n')
        .collect();
    let mut count: u32 = 0;

    for line in input {
        let mut first_digit: u32 = 0;
        let mut last_digit: u32 = 0;
        let mut found_digit: bool = false;

        let mut first_position: usize = usize::MAX;
        let mut last_position: usize = 0;

        // Check for normal digits
        for (pos, c) in line.chars().enumerate() {
            if c.is_digit(10) {
                if !found_digit {
                    first_position = pos;
                    first_digit = c.to_digit(10).unwrap();
                    last_position = pos;
                    last_digit = c.to_digit(10).unwrap();
                    found_digit = true;
                } else {
                    last_position = pos;
                    last_digit = c.to_digit(10).unwrap();
                }
            }
        }

        // Check for spelled digits
        let spelled_digits: [&str; 10] = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        ];
        for digit in spelled_digits {
            let occurrences = spelled_digit_occurrences(digit, line);
            if !occurrences.0.is_none() {
                let found_pos: usize = occurrences.0.unwrap();
                if found_pos < first_position {
                    first_digit = convert_spelled_digit(digit) as u32;
                    first_position = found_pos;
                }
            }
            if !occurrences.1.is_none() {
                let found_pos: usize = occurrences.1.unwrap();
                if found_pos > last_position {
                    last_digit = convert_spelled_digit(digit) as u32;
                    last_position = found_pos;
                }
            }
        }
        count += first_digit * 10 + last_digit;
    }
    println!("{}", count);
}