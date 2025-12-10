import Foundation

let fileURL = URL(fileURLWithPath: "input.txt")

func splitStringInHalf(inputString: String) -> (String, String)? {
    let length = inputString.count

    if length % 2 != 0 {
        return nil
    }

    let middleIndex = length / 2
    let firstHalfEndIndex = inputString.index(inputString.startIndex, offsetBy: middleIndex)

    let firstHalf = String(inputString[..<firstHalfEndIndex])
    let secondHalf = String(inputString[firstHalfEndIndex...])

    if(firstHalf.count != secondHalf.count) {
        // Explicitly cast the result of dropLast to String
        return nil
    }
    return (firstHalf, secondHalf)
}

do {
    let contents = try String(contentsOf: fileURL, encoding: .utf8)
    let lines = contents.split(separator: ",") 


    var mirroredNumbers: Set<Int> = []

    for line in lines {
        let rangeParts = line.split(separator: "-")
        
        guard rangeParts.count == 2 else {
            print("Unable to parse line: \(line)")
            continue 
        }

        if let bottomRange = Int(rangeParts[0]), let topRange = Int(rangeParts[1]) {
            Array(bottomRange ... topRange).forEach { number in  
                if let (firstHalf, secondHalf) = splitStringInHalf(inputString: String(number)) {
                    if firstHalf == secondHalf {
                        if let number = Int(String(number)) {
                                mirroredNumbers.insert(number)
                        }
                    }
                }
            }
        }
    }

    var total = 0
        print("mirroed numbers: \(mirroredNumbers)")
    for number in mirroredNumbers {
        total += number
    }
    print("Total: \(total)")

} catch {
    print("Error reading file: \(error)")
}