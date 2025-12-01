import Foundation

struct CombinationDial {
    let values: [Int]
    var position: Int = 50 

    mutating func moveRight(_ steps: Int) {
        position = (position + steps) % values.count
    }

    mutating func moveLeft(_ steps: Int) {
        position = (position - steps % values.count + values.count) % values.count
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

    var zeroCount = 0;

    for line in lines {
        var instruction = String(line)
        let direction = instruction.first
        instruction.removeFirst()  
        if(direction == "R") {
            if let steps = Int(instruction) {
                dial.moveRight(steps)
            }
        } else if(direction == "L") {
            if let steps = Int(instruction) {
                dial.moveLeft(steps)
            }
        }
        if dial.currentValue == 0 {
            zeroCount += 1
        }
    }

    print(zeroCount)

} catch {
    print("Error reading file: \(error)")
}