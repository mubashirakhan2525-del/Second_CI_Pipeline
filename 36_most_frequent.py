
def most_frequent(numbers):
    if not numbers:
        return None

    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    return max(frequency, key=frequency.get)
