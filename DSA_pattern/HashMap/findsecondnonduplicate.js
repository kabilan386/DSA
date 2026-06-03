let value = 'aaabcdbcffvvgee'

let hashmap = {}

for(i=0;i < value.length;i++){
    hashmap[value[i]] = (hashmap[value[i]] || 0) + 1
}

let count = 0

for(const key in hashmap){
    if(hashmap[key] == 1){
        count += 1
        if(count == 2){
            console.log(key)
        }
    }
}
   
        

console.log(hashmap)