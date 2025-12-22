def special_sum(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        value = numbers[i]
        if value % 5 == 0:
            value = value * 2
        if value > 0:
            total += value
        elif value < 0:
            total -= value 
        
        i += 1
    
    return total