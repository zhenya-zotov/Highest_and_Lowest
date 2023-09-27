def high_and_low(numbers):
    numbers = list(map(int, numbers.split(" ")))
    numbers = f'{max(numbers)} {min(numbers)}'
    return numbers
