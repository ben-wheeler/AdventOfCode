import Foundation

struct CombinationDial {
    let values: [Int]
    var position: Int = 50 

        mutating func moveRight(_ steps: Int) -> Int {
        var pastZeroCount = 0
        var clicks = steps

        while clicks > 0 {
            position += 1

            if position == values.count {
                position = 0
                pastZeroCount += 1
            }
            clicks -= 1
        }

        return pastZeroCount
    }

    mutating func moveLeft(_ steps: Int) -> Int {
        var pastZeroCount = 0
        var clicks = steps

        while clicks > 0 {
            position -= 1

            if position == 0 {
                pastZeroCount += 1
            }
            if position < 0 {
                position = values.count - 1
            }
            clicks -= 1
        }

        return pastZeroCount
    }

    var currentValue: Int {
        values[position]
    }
}

let fileURL = URL(fileURLWithPath: "input.txt")

do {
    let contents = try String(contentsOf: fileURL, encoding: .utf8)
    let lines = contents.split(separator: "\n")

    var dial = CombinationDial(values: Array(0...99))

    var totalPastZeroCount = 0;

    for line in lines {
        var instruction = String(line)
        let direction = instruction.first
        instruction.removeFirst()  
        if(direction == "R") {
            if let steps = Int(instruction) {
                totalPastZeroCount += dial.moveRight(steps)
            }
        } else if(direction == "L") {
            if let steps = Int(instruction) {
                totalPastZeroCount += dial.moveLeft(steps)
            }
        } 
    }

    print(totalPastZeroCount)

} catch {
    print("Error reading file: \(error)")
}