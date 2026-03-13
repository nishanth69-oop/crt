def right_triangle(n: int) -> str:
    pattern = ""
    for i in range(1, n + 1):
        pattern += "*" * i
        if i != n:
            pattern += "\n"
    return pattern
if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))