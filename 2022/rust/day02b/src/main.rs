fn get_score(round: &str) -> i32 {
    let opponent: &char = &round.chars().nth(0).unwrap();
    let me: &char = &round.chars().nth(2).unwrap();
    // Selection Points:
    // Rock - 1; Paper - 2; Scissors - 3
    // Outcome Points:
    // Lose - 0; Draw - 3; Win - 6
    match opponent {
        'A' => { // Rock
            match me {
                'X' => { 0 + 3 }, // Lose - Scissors
                'Y' => { 3 + 1 }, // Draw - Rock
                'Z' => { 6 + 2 }, // Win - Paper
                _ => panic!(),
            }
        },
        'B' => { // Paper
            match me {
                'X' => { 0 + 1 }, // Lose - Rock
                'Y' => { 3 + 2 }, // Draw - Paper
                'Z' => { 6 + 3 }, // Win - Scissors
                _ => panic!(),
            }
        },
        'C' => { // Scissors
            match me {
                'X' => { 0 + 2 }, // Lose - Paper
                'Y' => { 3 + 3 }, // Draw - Scissors
                'Z' => { 6 + 1 }, // Win - Rock
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