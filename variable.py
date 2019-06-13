print("hello world")

def tyield():
    a=1
    print(a,"before operation")
    a+=1
    print(a,"after optn")
    yield a
    print(a)
tyield()
