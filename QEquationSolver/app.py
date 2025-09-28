import math

def get_discriminant(a, b, c):
    """Return the discriminant (b^2 - 4ac)."""
    return b**2 - 4*a*c

def explain_discriminant(d):
    """Explain what the discriminant means."""
    if d > 0:
        return "Discriminant is positive → Two distinct real roots."
    elif d == 0:
        return "Discriminant is zero → One real root (repeated)."
    else:
        return "Discriminant is negative → Two complex roots."

def get_roots(a, b, c):
    """Return the roots based on the discriminant."""
    d = get_discriminant(a, b, c)

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return f"Roots are real and distinct: {root1} and {root2}"
    elif d == 0:
        root = -b / (2*a)
        return f"Root is real and repeated: {root}"
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-d) / (2*a)
        return f"Roots are complex: {real_part}+{imag_part}i and {real_part}-{imag_part}i"

# Example usage
if __name__ == "__main__":
    print("Quadratic Equation Solver")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    d = get_discriminant(a, b, c)
    print(f"\nDiscriminant (Δ) = {d}")
    print(explain_discriminant(d))
    print(get_roots(a, b, c))

