import cmath

a=1
b=-6
c=9

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return x1, x2

print(f"(1)={quadratic_formula(1,-6,9)}")
print(f"(2)={quadratic_formula(1,2,-8)}")
print(f"(3)={quadratic_formula(8,-6,-35)}")
print(f"(4)={quadratic_formula(1,0,1)}")
