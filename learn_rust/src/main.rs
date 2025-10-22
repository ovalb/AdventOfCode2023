use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fs;

fn main() {
    let content = fs::read_to_string("./input").unwrap();

    let mut h: BinaryHeap<Reverse<i32>> = BinaryHeap::new();

    let elves = content.split("\n\n");
    for elf in elves {
        let packsum: i32 = elf.lines().filter_map(|p| p.parse::<i32>().ok()).sum();
        h.push(Reverse(packsum));
        if h.len() > 3 {
            h.pop();
        }
    }

    let result: i32 = h.into_iter().map(|x| x.0).sum();
    println!("{}", result);
}
