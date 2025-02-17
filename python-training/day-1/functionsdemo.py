
def demoFun():
    print('demo function')


demoFun()

def mulDemo(x,y):
    return (x*y)

print(mulDemo(3,4))

def arrayInput(*boa):
    for userargs in boa:
        print(userargs)

arrayInput(2,5,6,1,5,9,8,7,6)