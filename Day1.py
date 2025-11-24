#print Hello World proram
print("Hello World")


# Reverse a String without using slice

def reverse_string(s):
    reversed_str = ""
    for i in s:
        reversed_str = i + reversed_str
    return reversed_str

print(reverse_string("Singhal"))  
#output:lahgniS
