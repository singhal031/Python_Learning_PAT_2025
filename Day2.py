# Demonstrating multiple data types and operations in Python
integer_val = 42
print(type(integer_val), integer_val)

float_val = 3.14
print(type(float_val), float_val)

string_val = "Hello"
print(type(string_val), string_val)

boolean_val = True
print(type(boolean_val), boolean_val)

none_val = None
print(type(none_val), none_val)

complex_val = 2 + 3j
print(type(complex_val), complex_val)

list_val = [1, 2, 3]
print(type(list_val), list_val)

tuple_val = (4, 5, 6)
print(type(tuple_val), tuple_val)

set_val = {7, 8, 9}
print(type(set_val), set_val)

dict_val = {"name": "Alice", "age": 25}
print(type(dict_val), dict_val)

bytes_val = b"Python"
print(type(bytes_val), bytes_val)

bytearray_val = bytearray(b"World")
print(type(bytearray_val), bytearray_val)

print("\n<- Type Conversions ->")
print("int from float:", int(float_val))
print("float from int:", float(integer_val))
print("str from int:", str(integer_val))
print("bool from int:", bool(integer_val))
print("list from tuple:", list(tuple_val))
print("tuple from list:", tuple(list_val))
print("set from list:", set(list_val))

# Operations combining types
print("\n<- Mixed Operations ->")
sum_val = integer_val + float_val
print("Sum (int + float):", sum_val)

concat_val = string_val + " World"
print("String concatenation:", concat_val)

bool_math = boolean_val + 10  
print("Boolean in math:", bool_math)

# String is Anagram or not:-n
def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
