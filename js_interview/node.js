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
    }, 100)

    setImmediate(() => {
        console.log("Immediate")
    },0)

    process.nextTick(() => {
        console.log("Next Tick")
    })
})

queueMicrotask(() => {
    console.log("Microtask")
})

process.nextTick(() => {
    console.log("Next Tick")
})

console.log("end")