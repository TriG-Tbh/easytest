# Example program displayed in 

import easytest

@easytest.test(stdin="5", stdout="10")
def myfunc():
    x = int(input())
    print(x + 5)

easytest.linebreak()

@easytest.test(params=[5, 3], stdout="10")
def myfunc2(x, test=0):
    print(x + test)

easytest.render()