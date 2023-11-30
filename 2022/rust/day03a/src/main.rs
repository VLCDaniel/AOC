fn main() {
    let input: Vec<&str> = include_str!("input.txt").split('\n').collect();
    let mut sum: usize = 0;

    for line in input {
        let mut first_compartment: Vec<i32> = vec![0; 256];
        // First compartment
        let comp_size = line.len() / 2;
        for (pos, c) in line.chars().enumerate() {
            if pos < comp_size {
                first_compartment[c as usize] += 1;
            } else {
                break;
            }
        }

        // Second compartment
        for c in line.chars().skip(comp_size) {
            if first_compartment[c as usize] != 0 {
                let char_prio = if c as usize > 96 {
                    c as usize - 'a' as usize + 1
                } else {
                    c as usize - 'A' as usize + 27
                };
                sum += char_prio;
                first_compartment[c as usize] = 0;
            }
        }
    }
    println!("{}", sum);
}