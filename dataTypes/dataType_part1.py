a = 12  # defining simple integer
print(type(a), f'value of a is {a}')
a_hex = 0XC  # Hexadecimal representation of an int.
print(type(a_hex), a_hex)
a_oct = 0o14  # Octal representation of an int.
print(type(a_oct), a_oct)
a_bin = 0B1100
print(type(a_bin), a_bin)

# we have some inbuilt function to convert a decimal base value to binary  , octal,hexadecimal.


print(oct(12), bin(12), hex(12))

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
print(f'type of data  is {type(a_complex)} and value is: {a_complex}')
print(f'real part value is: {a_complex.real} and imaginary part value is: {a_complex.imag}')