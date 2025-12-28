def special_sum(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        value = numbers[i]
        if value % 5 == 0:
            value *= 2
        value = 0-(value)
        total += value
        i += 1
    return total
print(special_sum([5, -2, 3, 4, -10, 17]))