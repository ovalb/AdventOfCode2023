use std::fs;

struct TopPacks {
    packs: Vec<i32>,
    capacity: u8,
}

impl TopPacks {
    fn new(c: u8) -> TopPacks {
        TopPacks {
            packs: vec![],
            capacity: c,
        }
    }
    fn try_add(&mut self, value: i32) {
        if self.capacity > 0 {
            self.packs.push(value);
            self.capacity -= 1;
        } else {
            let f = self
                .packs
                .iter()
                .enumerate()
                .fold(
                    (self.packs[0], 0),
                    |acc, (i, &x)| if x < acc.0 { (x, i) } else { acc },
                );

            if value > f.0 {
                self.packs[f.1] = value;
            }
        }
    }

    fn sum(&self) -> i32 {
        self.packs.iter().sum()
    }
}

fn main() {
    let content = fs::read_to_string("./input").unwrap();

    let mut top_packs = TopPacks::new(3);

    let elves = content.split("\n\n");
    for elf in elves {
        let packs = elf.split("\n").map(|p| p.parse::<i32>().unwrap());
        top_packs.try_add(packs.sum());
    }

    println!("{}", top_packs.sum())
}
