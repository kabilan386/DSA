// Global Scope
var name = 'Kabilan'

function test(){
    console.log(name)
}

test()

// Lexical Scope
function test2(){
    var name = 'Kabilan2'
    function test3(){
        console.log(name)
    }
    test3()
}

test2()

// Block Scope
function test4(){
    var name = 'Kabilan4'
    function test5(){
        var name = 'Kabilan5'
        function test6(){
            console.log(name)
        }
        test6()
    }
    test5()
}

test4()

