const fs = require("fs")

console.log("start")

setTimeout(() => {
    console.log("Hello1")
}, 100)

setImmediate(() => {
    console.log("Immediate")
})

fs.readFile("./node.js", () => {
    console.log("File Read")

    setTimeout(() => {
        console.log("Hello2")
    }, 0)

    setImmediate(() => {
        console.log("Immediate")
    })

    process.nextTick(() => {
        console.log("Next Tick")
    })
})

process.nextTick(() => {
    console.log("Next Tick")
})

console.log("end")