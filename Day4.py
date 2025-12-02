# Arithmetic operations 
def arithmetic(a, b):
    print("a = {a}, b = {b}")
    print("Addition (a + b):", a + b)
    print("Subtraction (a - b):", a - b)
    print("Multiplication (a * b):", a * b)
    print("True division (a / b):", a / b)       
    print("division (a // b):", a // b)   
    print("Modulo (a % b):", a % b)              
    print("Exponentiation (a ** b):", a ** b)
    print("Unary plus (+a):", +a)
    print("Unary minus (-a):", -a)

    # Augmented assignments
    x = a
    x += b
    print("Augmented add (x += b):", x)
    x *= 2
    print("Augmented multiply (x *= 2):", x)
    x //= 2
    print("Augmented floor division (x //= 2):", x)

# Try with integers
arithmetic(7, 3)
arithmetic(7.5, 2.0)
