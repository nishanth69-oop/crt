# Fibonacci series generator
# Reads number of terms from user and prints the sequence

def print_fibonacci(n):
    """Prints first n terms of the Fibonacci sequence.

    Args:
        n (int): number of terms to print
    """
    if n <= 0:
        print("Number of terms must be positive")
        return
    a, b = 0, 1
    terms = []
    for _ in range(n):
        terms.append(a)
        a, b = b, a + b
    print("Fibonacci series:", " ".join(str(t) for t in terms))


if __name__ == "__main__":
    try:
        n = int(input("Enter number of Fibonacci terms: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print_fibonacci(n)
