a =23
a_float = 12.4  # defining a simple float value in python
print(f'type of a_float is {type(a_float)} and value is: {a_float}')

# defining a string in python
a_string = "python"
print(f'type of a_string is {type(a_string)} and value is: {a_string}')

# defining a boolean in python
a_bool = True
print(f'type of a_bool is {type(a_bool)} and value is: {a_bool}')

# a complex datatype with value in python
a_complex = 12 + 5j

# type Casting/type coertion.int(),float(),complex(),bool(),str()
# Type conversions with integer value
print(f'int to float conversion: {float(a)}, {type(a)}')  # int to float possible
print(f'int to string conversion {(str(a))}')  # int to string possible
print(f'int to complex datatype conversion {complex(a)}')  # int to complex bossible but imaginary value will be 0j.
print(f'int to bool type {bool(a)}')  # int to bool possible

# Type conversion with float value.
# for exact  int(0)/float(means 0) bool is false,for empty string bool is false.
# float(base- 2,8,16)- possible
print(f'float to int type conversion {int(a_float)}')  # valid conversion
print(f'float to complex type {complex(a_float)}')  # valid but imaginary part always will be 0j.
print(f'float to string {str(a_float)}')  # valid conversion
print(f'float to bool conversion:  {bool(a_float)}')

# Type conversion with Complex value.

print(f'complex to int conversion {int(a_complex)}')  # invalid-error
print(f'complex to float {float(a_complex)}')  # invalid-error

string_to_complex = str(a_complex)
print(f'complex to string conversion : {type(string_to_complex)}')  # valid

# string conversions.
print(f'string to int {int(a_string)}')  # invalid
print(f'string to complex {complex(a_string)}')  # invalid
print(f'string to bool {bool(a_string)}')  # valid-if string is not null
print(f'string to float {float(a_string)}')  # invalid

# Any data type to String type we can convert.
print(f'string to string {str("23")}')
print(f'int to string {str(10)}')
print(f'binary to string {str(0B111)}')
print(f'float to string {str(125.55)}')
print(f'complex to string {str(10 + 4j)}')
print(f'bool to string {str(True)}')# type Casting/type coertion.int(),float(),complex(),bool(),str()
#Type conversions with integer value
print(f'int to float conversion: {float(a)}, {type(a)}')  # int to float possible
print(f'int to string conversion {(str(a))}')  # int to string possible
print(f'int to complex datatype conversion {complex(a)}')  # int to complex bossible but imaginary value will be 0j.
print(f'int to bool type {bool(a)}')  # int to bool possible



#Type conversion with float value.
# for exact  int(0)/float(means 0) bool is false,for empty string bool is false.
# float(base- 2,8,16)- possible
print(f'float to int type conversion {int(a_float)}')  # valid conversion
print(f'float to complex type {complex(a_float)}')  # valid but imaginary part always will be 0j.
print(f'float to string {str(a_float)}')  # valid conversion
print(f'float to bool conversion:  {bool(a_float)}')



#Type conversion with Complex value.

print (f'complex to int conversion {int(a_complex)}')  #invalid-error
print(f'complex to float {float(a_complex)}')  # invalid-error

string_to_complex = str(a_complex)
print(f'complex to string conversion : {type(string_to_complex)}')  #valid



# string conversions.
print(f'string to int {int(a_string)}')   #invalid
print(f'string to complex {complex(a_string)}') #invalid
print(f'string to bool {bool(a_string)}')#valid-if string is not null
print(f'string to float {float(a_string)}')#invalid

# Any data type to String type we can convert.
print(f'string to string {str("23")}')
print(f'int to string {str(10)}')
print(f'binary to string {str(0B111)}')
print(f'float to string {str(125.55)}')
print(f'complex to string {str(10 + 4j)}')
print(f'bool to string {str(True)}')