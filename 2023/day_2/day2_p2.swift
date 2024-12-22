import Foundation

// 12 red cubes, 13 green cubes, and 14 blue cubes
let input = try String(contentsOfFile: "fileinput")
let sum: Int = input.split(separator: "\n").reduce(0) { acc, game in
    let splitted = game.split(separator: ":")
    let allDraws = splitted.last!
    
    let baseDraw = allDraws.split(separator: ";")
        .map{d in parseDrawAttempt(String(d))}
        .reduce(into: [String:Int]()) { base, cur in
        ["red", "green", "blue"].forEach { color in
            base[color] = max(base[color] ?? 1, cur[color] ?? 1)
        }
    }

     let minimumPower = (baseDraw["red"]! * baseDraw["green"]! * baseDraw["blue"]!)
     return acc + minimumPower
}

print("Result is: ", sum)

func parseDrawAttempt(_ drawAttempt: String) -> [String: Int] {
    var bucket = [String:Int]()
    drawAttempt
        .trimmingCharacters(in: .whitespaces)
        .split(separator: ",")
        .forEach { attempt in
            let splitted = attempt.split(separator: " ")
            let (number, color) = (Int(splitted.first!), String(splitted.last!))
            bucket[color] = number
        }
    
    return bucket
}
