from typing import Generator


def fibonacci(n: int) -> Generator[int, None, None]:
    current_fib, next_fib = 0, 1
    for _ in range(n):
        yield current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib


if __name__ == "__main__":
    for f in fibonacci(5):
        print(f)  # 0 1 1 2 3
