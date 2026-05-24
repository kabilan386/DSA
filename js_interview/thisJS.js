const user = {
    name : "Jhon",
    greet : function(){
        console.log(`Hello ${this.name}`)
    },
    greetArrow : () => {
        console.log(`Hello ${this.name}`)
    },
    greet2 : (function(){
        return function(){
            console.log(`Hello ${this.name}`)
        }
    })(),

    greet3 : function(){
        setTimeout(function(){
            console.log(`Hello ${this.name}`)
        }, 1000)
    },
    greet4 : function(){
        setTimeout(() => {
            console.log(`Hello ${this.name}`)
        }, 1000)
    },
    greet5 : function(){
        const self = this
        setTimeout(function(){
            console.log(`Hello ${self.name}`)
        }, 1000)
    },
    greet6 : function(){
        const self = this
        setTimeout(() => {
            console.log(`Hello ${self.name}`)
        }, 1000)
    }
}

// user.greet()
// user.greetArrow()
// user.greet2()
// user.greet3()
// user.greet4()
// user.greet5()
user.greet6()