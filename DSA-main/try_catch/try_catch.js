
function test(){
    try {
        // console.log("try")
        return 10 / "a"
    } catch (error) {
        console.log("catch",error)
        // return 2
    }
    // finally{
    //     console.log("finally")
    // }
}


test()