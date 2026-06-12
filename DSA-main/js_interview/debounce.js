function debounce(cb, delay){
    let timeout
    return function(...args){
        clearTimeout(timeout)
        timeout = setTimeout(() => {
            cb(...args)
        }, delay)
    }
}