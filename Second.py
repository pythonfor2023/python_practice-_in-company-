def add(x,y):
    print(x+y)

def simple():
    print("hello world")

def  fun(*args):
    for i in args:
        print(i)

def main():
    add(20,30)
    simple()
    fun(34,45,45,45,45,4,5,45)
    var=33443


if __name__=='__main__':
    print("It has all under control after this statement the  main function will be called")
    main()
    print("don't want but still you came:")
  