Array.prototype.myMap = function(cb){
    const result = []
    for(let i = 0; i < this.length; i++){
        result.push(cb(this[i], i, this))
    }
    return result
}

const arr = [1,2,3,4,5]

console.log(arr.myMap((item) => item * 2))

Array.prototype.myFilter = function(cb){
    const result = []
    for(let i = 0; i < this.length; i++){
        if(cb(this[i], i, this)){
            result.push(this[i])
        }
    }
    return result
}

console.log(arr.myFilter((item) => item % 2 === 0))

Array.prototype.myReduce = function(cb, initialValue){
    let accumulator = initialValue
    for(let i = 0; i < this.length; i++){
        accumulator = cb(accumulator, this[i], i, this)
    }
    return accumulator
}

console.log(arr.myReduce((acc, item) => acc + item, 0))

Array.prototype.myFlat = function(depth = 1){
    const result = []
    for(let i = 0; i < this.length; i++){
        if(Array.isArray(this[i]) && depth > 0){
            result.push(...this[i].myFlat(depth - 1))
        }else{
            result.push(this[i])
        }
    }
    return result
}

console.log(arr.myFlat(2))