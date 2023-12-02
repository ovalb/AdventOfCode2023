import Foundation

// 12 red cubes, 13 green cubes, and 14 blue cubes
let input = try String(contentsOfFile: "fileinput")
let sum = input.split(separator: "\n").reduce(0) { acc, game in
    let splitted = game.split(separator: ":")
    let gameId = splitted.first!.split(separator: " ").last!
    let allDraws = splitted.last!
    var isGameValid = true
    allDraws.split(separator: ";").forEach { draws in
        let curBucket = parseDrawAttempt(String(draws))
        if !isValidGame(curBucket) {
            isGameValid = false
        }
    }

    return isGameValid ? acc + Int(gameId)! : acc
}

print("Result is: ", sum)

func isValidGame(_ gameDict: [String: Int]) -> Bool {
    let redBalls = gameDict["red"] ?? 0
    let greenBalls = gameDict["green"] ?? 0
    let blueBalls = gameDict["blue"] ?? 0
    return redBalls <= 12 && greenBalls <= 13 && blueBalls <= 14
}

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
