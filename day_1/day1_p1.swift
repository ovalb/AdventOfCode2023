import Foundation

let contents = try String(contentsOfFile: "fileinput")

var sum = 0
contents.split(separator:"\n").forEach { line in
    let firstDigit = getFirstDigit(String(line))!
    let lastDigit = getLastDigit(String(line))!
    sum += Int("\(firstDigit)\(lastDigit)")!
}

print("Answer is: ", sum)


func getFirstDigit(_ str: String) -> Character? {
    for ch in str {
        if Int(String(ch)) != nil {
            return ch
        }
    }
    
    return nil
}

func getLastDigit(_ code: String) -> Character? {
    return getFirstDigit(String(code.reversed()))
}

