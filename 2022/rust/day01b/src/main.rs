use std::fs;

const FILE_PATH: &str = "src/input.txt";
fn main() {
    println!("In file {}", FILE_PATH);

    let contents = fs::read_to_string(FILE_PATH).expect("Should have been able to read the file");

    let reindeer: Vec<&str> = contents.split("\n\n").collect();

    let mut _max_calories: Vec<i32> = vec![0; 3];
    for rudolph in reindeer {
        let reindeer: Vec<&str> = rudolph.split('\n').collect();
        let mut calories: i32 = 0;
        for _calorie in reindeer {
            let calorie: i32 = _calorie.parse().unwrap();
            calories += calorie;
        }
        if calories > _max_calories[2] {
            _max_calories[0] = _max_calories[1];
            _max_calories[1] = _max_calories[2];
            _max_calories[2] = calories;
        } else if calories > _max_calories[1] {
            _max_calories[0] = _max_calories[1];
            _max_calories[1] = calories;
        } else if calories > _max_calories[0] {
            _max_calories[0] = calories;
        }
    }

    println!(
        "Sum top 3 calories: {}",
        _max_calories[2] + _max_calories[1] + _max_calories[0]
    );
}
