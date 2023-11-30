use std::collections::HashSet;

fn main() {
    let input: Vec<&str> = include_str!("input.txt").split('\n').collect();
    let mut sum: usize = 0;

    for chunk in input.chunks(3) {
        let [chunk1, chunk2, chunk3] = [chunk[0], chunk[1], chunk[2]];
        let mut char_set: HashSet<char> = HashSet::new();

        for c in chunk1.chars() {
            char_set.insert(c);
        }

        for &c in &char_set {
            if chunk2.contains(c) && chunk3.contains(c) {
                let char_prio = if c as usize > 96 {
                    c as usize - 'a' as usize + 1
                } else {
                    c as usize - 'A' as usize + 27
                };
                sum += char_prio;
                break;
            }
        }
    }
    println!("{}", sum);
}