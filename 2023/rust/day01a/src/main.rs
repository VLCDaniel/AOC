fn main() {
    let input: Vec<_> = include_str!("input.txt")
        .split('\n')
        .collect();
    let mut count: u32 = 0;

    for line in input {
        let digits: Vec<u32> = line.chars()
            .filter(|c| c.is_digit(10))
            .map(|c| c.to_digit(10).unwrap())
            .collect();

        let first_digit: &u32 = digits.first().unwrap();
        let last_digit: &u32 = digits.last().unwrap();
        count += first_digit * 10 + last_digit;
    }
    println!("{}", count);
}