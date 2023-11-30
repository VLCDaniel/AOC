use std::fs;

const FILE_PATH: &str = "src/input.txt";
fn main() {
    println!("In file {}", FILE_PATH);

    let contents = fs::read_to_string(FILE_PATH)
        .expect("Should have been able to read the file");

    let reindeer: Vec<&str> = contents.split("\n\n").collect();

    let mut _max_calories: i32 = 0;
    for rudolph in reindeer {
        let reindeer: Vec<&str> = rudolph.split('\n').collect();
        let mut calories: i32 = 0;
        for _calorie in reindeer {
            let calorie: i32 = _calorie.parse().unwrap();
            calories += calorie;
        }
        _max_calories = if calories > _max_calories { calories } else { _max_calories };
    }

    println!("Max calories: {}", _max_calories);
}