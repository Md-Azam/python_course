# function in python.
# in built functions- sort,sorted,print
# user defined function
# lambda function
# recursive function

def my_func():
    print("hello azam")


# calling a function
my_func()


def my_funcWithReturn():
    return 2 * 2


my_funcWithReturn()
print(my_funcWithReturn())


#
# #function with single arguments:
def my_func1(name):
    print("hi ,how are you " + name)


my_func1("azam")


def my_func3(name, age):
    print("hi ,how are you " + name)
    print("your age is" + str(age))


my_func3("azam", 12)


def keyWordArgs(**name):
    print(name)


keyWordArgs(a="azam", b="furqaan", c=12, d=12.4, f=1 + 2j)

# lambda function
my_square = lambda x, y: x ** y
print(f'square of two given value is : {my_square(2, 4)}')


# recursive function :
def my_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n) * my_recursion(n - 1)
    # my_recursion(5)


print(my_recursion(5))