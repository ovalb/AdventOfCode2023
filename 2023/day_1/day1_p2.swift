import Foundation

let contents = try String(contentsOfFile: "fileinput")

let writtenDigits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

let sum = contents.split(separator:"\n").reduce(0) { sum, line in
    let firstDigit = getFirstDigitV2(String(line), writtenDigits)!
    let lastDigit = getLastDigitV2(String(line), writtenDigits)!
    return sum + Int("\(firstDigit)\(lastDigit)")!
}

print("Answer is: ", sum)

func getFirstDigitV2(_ line: String, _ writtenDigits: [String]) -> String? {
    for i in 0..<line.count {
        let currentChar = String(line[i])
        if Int(currentChar) != nil {
            return currentChar
        } 

        for (digitIdx, digit) in writtenDigits.enumerated() {
            let endIdx = min(i + digit.count, line.count)
            if line[i..<endIdx] == digit {
                return String(digitIdx)
            }
        }
    }
    
    return nil
}

func getLastDigitV2(_ line: String, _ writtenDigits: [String]) -> String? {
    let lineReversed = String(line.reversed())
    let  digitsReversed = writtenDigits.map{String($0.reversed())}
    return getFirstDigitV2(lineReversed, digitsReversed)
}



extension String {
    subscript (index: Int) -> Character {
        let charIndex = self.index(self.startIndex, offsetBy: index)
        return self[charIndex]
    }

    subscript (range: Range<Int>) -> Substring {
        let startIndex = self.index(self.startIndex, offsetBy: range.startIndex)
        let stopIndex = self.index(self.startIndex, offsetBy: range.startIndex + range.count)
        return self[startIndex..<stopIndex]
    }
}