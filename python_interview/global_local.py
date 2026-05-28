count = 10

def update():
    global count
    count = 20

update()

print(count)


count = 10

def update():
    count = 20
    print(count)

update()

print(count)


def outer():
    x = 10

    def inner():
        x = 20
        print("inner:", x)

    inner()
    print("outer:", x)

outer()