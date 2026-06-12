function throttle(cb, delay){
    let timeout
    return function(...args){
        if(!timeout){
            cb(...args)
            timeout = setTimeout(() => {
                timeout = null
            }, delay)
        }
    }
}



const throttledFn = throttle(() => {
    console.log("Hello")
}, 1000)

