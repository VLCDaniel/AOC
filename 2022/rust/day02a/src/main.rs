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
                'X' => { 1 + 3 }, // Rock - Draw
                'Y' => { 2 + 6 }, // Paper - Win
                'Z' => { 3 + 0 }, // Scissors - Lose
                _ => panic!(),
            }
        },
        'B' => { // Paper
            match me {
                'X' => { 1 + 0 }, // Rock - Lose
                'Y' => { 2 + 3 }, // Paper - Draw
                'Z' => { 3 + 6 }, // Scissors - Win
                _ => panic!(),
            }
        },
        'C' => { // Scissors
            match me {
                'X' => { 1 + 6 }, // Rock - Win
                'Y' => { 2 + 0 }, // Paper - Lose
                'Z' => { 3 + 3 }, // Scissors - Draw
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