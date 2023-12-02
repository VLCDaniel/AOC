fn main() {
    let input: Vec<_> = include_str!("input.txt")
        .split('\n')
        .collect();
    let mut sum: i32 = 0;

    for line in input {
        let game: Vec<&str> = line.split(": ").collect();
        let game_id: &str = game[0].split(' ').collect::<Vec<_>>()[1];
        let id: i32 = game_id.parse::<i32>().unwrap();

        let records: Vec<&str> = game[1].split("; ").collect();
        let mut add: bool = true;
        for record in records {
            let mut red: i32 = 12;
            let mut green: i32 = 13;
            let mut blue: i32 = 14;

            let cubes: Vec<&str> = record.split(", ").collect();
            for cube in cubes {
                let components: Vec<&str> = cube.split(' ').collect();
                let color: &str = components[1];
                let number: i32 = components[0].parse::<i32>().unwrap();
                match color {
                    "green" => {
                        green -= number;
                    },
                    "red" => {
                        red -= number;
                    },
                    "blue" => {
                        blue -= number;
                    }
                    _ => panic!("Invalid color")
                }
            }

            add = if red < 0 || blue < 0 || green < 0 { false } else { add };
        }

        sum = if add { sum + id } else { sum };
    }
    println!("{}", sum);
}