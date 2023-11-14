a = 12
b = 6
print(a + b)  # 18
print(a - b)  # 6
print(a * b)  # 72
print(a / b)  # 2.0
print(a % b)  # returns reminder.
print(12 // 6)  # 2
print(2 ** 4)  # 16

# 2.Relational Operator-comparision operator:compares two values/object.


print(a < b)  # False
print(a <= b)  # False
print(a > b)  # True
print(a >= b)  # True

print(chr(99))  # c
print(chr(65))  # A
print(ord("a"))  # 97

s1 = "java"
s2 = "python"
print(f'unicode value is: {chr(99)}')  # c
print(f'ascii value of char is:  {ord("a")}')  # 97
print(f' s1 == s1: {s1 == s2}')  # False
print(f' s1>s1: {s1 > s2}')  # False
print(f' s1<s1: {s1 < s2}')  # True
print(f's1 != s2 !=  {s1 != s2}')  # True

print(f's1 == s2 {s1 == s2}')  # False
print(f's1 == s2 {s1 != s2}')  # True

# We use this operators mostly with conditional statement .
x = True
y = False
z = True

print(x and z)  # True
print(x and y)  # False

result1 = not x  # Returns False
result2 = not y  # Returns True
result3 = not 0  # Returns True
result4 = not "hello"  # Returns False

# Logical and operator behaviour with non - boolean type.

# A)if x is flase result will be x.
# B) if x is True result will be y
# c) if x and y both is true then second operand will be final result.

# Logical or operator behaviour with non-boolean type.
# if x is true result will be x.
# if x is false result will be y.
# if x and y both will true then result will be first operand.

x = "java"
y = "python"
z = ""
print(x and z)  # result empty String
print(x or z)  # result java
print(z and x)  # result ''
print(x and y)  # result python
print(x or y)  # result java

# 4.Membership Operators:
# A) in (Membership - used to test if a value is present in a sequence, like a list or a string)
# B)not in (Negative Membership).
# is (Identity - used to check if two objects have the same memory location)

a1 = 2
a2 = 24
print(id(a1))  # address of a1
print(id(a2))  # address of a2
print(a1 is a2)  # result False
print(a1 is not a2)  # result True

# membership operator : in,  not in
my_string = "hello world"
print('l' in my_string)  # Result True
print('zx' in my_string)  # Result False
print('zx' not in my_string)  # Result True

# 6. Ternary / Conditional
# Syntax:  x if condition else y
t1 = 12
t2 = 23
max_val = t2 if t1 < t2 else t1
print(f'max value is {max_val}')
