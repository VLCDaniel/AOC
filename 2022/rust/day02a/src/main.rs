fn get_score(round: &str) -> i32 {
    let opponent: &char = &round.chars().nth(0).unwrap();
    let me: &char = &round.chars().nth(2).unwrap();
    match opponent {
        'A' => {
            match me {
                'X' => { 1 + 3 },
                'Y' => { 2 + 6 },
                'Z' => { 3 + 0 },
                _ => panic!(),
            }
        },
        'B' => {
            match me {
                'X' => { 1 + 0 },
                'Y' => { 2 + 3 },
                'Z' => { 3 + 6 },
                _ => panic!(),
            }
        },
        'C' => {
            match me {
                'X' => { 1 + 6 },
                'Y' => { 2 + 0 },
                'Z' => { 3 + 3 },
                _ => panic!(),
            }
        },
        _ => panic!(),
    }
}

fn main() {
    println!(
        "{}",
    include_str!("input.txt")
        .split('\n')
        .map(|l| get_score(l)).sum::<i32>()
    );
}