import Foundation

let fileURL = URL(fileURLWithPath: "input.txt")

func isInvalidRepeatedID(_ id: String) -> Bool {
    let doubled = id + id
    let trimmed = doubled.dropFirst().dropLast()
    return trimmed.contains(id)
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
                if isInvalidRepeatedID(String(number)) {
                    mirroredNumbers.insert(number)
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