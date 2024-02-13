def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def make_fibonacci():
    print("Enter a position to get the Fibonacci number:")
    position = int(input())

    if position < 0:
        print("Please enter a non-negative position.")
        return

    result = fibonacci(position)
    print('Fibonacci result:', result)

make_fibonacci()
