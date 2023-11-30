fn main() {
    let input: Vec<_> = include_str!("input.txt")
        .split('\n')
        .collect();
    let mut count: usize = 0;

    for line in input {
        let ranges: Vec<&str> = line.split(',').collect();
        let first_ids: Vec<&str> = ranges[0].split('-').collect();
        let id1 = first_ids[0].parse::<i32>().unwrap();
        let id2 = first_ids[1].parse::<i32>().unwrap();
        let second_ids: Vec<&str> = ranges[1].split('-').collect();
        let id3 = second_ids[0].parse::<i32>().unwrap();
        let id4 = second_ids[1].parse::<i32>().unwrap();

        if id1 <= id3 && id2 >= id4 || id3 <= id1 && id4 >= id2 {
            count += 1;
        }
    }
    println!("{}", count);
}