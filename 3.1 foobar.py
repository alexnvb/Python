
for i in range(100):
    if (i+1)%3 == 0:
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            print("FooBar")
        else:
            print("Foo")
    elif (i+1)%5 == 0:
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            print("FooBar")
        else:
            print("Bar")
    else:
            print(i+1)
