let a = [16, 17, 4, 3, 5, 2]

let arr = []
        
// let arrLength = a.length()

// console.log(arrLength);

for(let i = a.length - 1 ; i >= 0 ; i--){
    if(arr.length == 0){
        arr.push(a[i]) 
    }
    else if(arr[arr.length - 1] < a[i]){
        arr.push(a[i]) 
    }
}
        
console.log(arr.reverse());