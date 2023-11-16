#import inBuilt modules
# import math
# from math import ceil
from math import *
print(pow(2,0))
print(pow(2,5))

#import user_defined modules
import my_module
from my_module import palindrome_string
palindrome_string("azma")

#importing modules from outside directory
from functions import function_basic
function_basic.my_func()