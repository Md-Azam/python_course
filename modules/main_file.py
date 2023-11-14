class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    def __init__(self, msg):
        self.msg = msg
    # you need to guess this number
def my_function():
    number = 12
    try:
        input_num = int(input("Enter a number: "))
        if input_num < number:
            raise InvalidAgeException("you are not eligible")
        else:
            print("Eligible to Vote")
    except InvalidAgeException as e:
        print("invalid arg", e)
        print("Exception occurred: Invalid Age")
    finally:
        print("finally block executed")
my_function()

