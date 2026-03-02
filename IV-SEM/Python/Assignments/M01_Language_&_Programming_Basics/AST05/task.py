from typing import List

def Collatz_Sequence(n: int) -> List:
    sequence = []

    while n != 1:
        sequence.append(n)

        if n % 2 == 0:
            n = n // 2
        else:    
            n = 3 * n + 1

    sequence.append(1)     
    return sequence


if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))