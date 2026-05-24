
function test(){
    try {
        return 10 / "a"
    } catch (error) {
        return 2
    }finally{
        return 3
    }
}


console.log(test())