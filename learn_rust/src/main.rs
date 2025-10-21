use std::fs; 
use std::cmp::max;

fn main() {
    let content = fs::read_to_string("./example").unwrap();

    let mut largest = 0;

    let elves = content.split("\n\n");
    for elf in elves {
        let packs = elf.split("\n").map(|p| p.parse::<i32>().unwrap());
        largest = max(largest, packs.sum());
    }

    println!("{}", largest)
}
