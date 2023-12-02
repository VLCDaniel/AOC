fn main() {
    let input: Vec<_> = include_str!("input.txt")
        .split('\n')
        .collect();
    let mut sum: i32 = 0;

    for line in input {
        let game: Vec<&str> = line.split(": ").collect();
        let records: Vec<&str> = game[1].split("; ").collect();

        let mut min_red: i32 = 0;
        let mut min_green: i32 = 0;
        let mut min_blue: i32 = 0;
        for record in records {
            let cubes: Vec<&str> = record.split(", ").collect();
            for cube in cubes {
                let components: Vec<&str> = cube.split(' ').collect();
                let color: &str = components[1];
                let number: i32 = components[0].parse::<i32>().unwrap();
                match color {
                    "green" => {
                        if number > min_green {
                            min_green = number;
                        }
                    },
                    "red" => {
                        if number > min_red {
                            min_red = number;
                        }
                    },
                    "blue" => {
                        if number > min_blue {
                            min_blue = number;
                        }
                    }
                    _ => panic!("Invalid color")
                }
            }
        }

        let power: i32 = min_green * min_red * min_blue;
        sum += power;
    }
    println!("{}", sum);
}