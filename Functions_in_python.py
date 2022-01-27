def printme(str):
    """This is a passed string into a function"""
    print(str)
    return

printme("I'm first call to user defined function!")
printme("Again second call to the same function")
print("The Great")

def changeme(mylist):
    """This changes a passed list into this function"""
    mylist.append([1, 2, 3, 4])
    print("Values inside the function:", mylist)
    return

mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function:", mylist)


def changeme(mylist):
    """This changes a passed list into this function"""
    mylist = [1, 2, 3, 4]  # This will assign new reference in my list
    print("Values inside the function:", mylist)
    return

mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function:", mylist)

def printinfo(name, age):
    """This prints a passed info into this function"""
    print("NAME: ", name)
    print("AGE: ", age)
    return

printinfo(age=12, name="Samson")
