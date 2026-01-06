def calculate_percentage(number):
    if number < 1000:
        value = ((5 / 100) * number)
    else:
        value = ((10 / 100) * number)
    return value



number = int(input())

result = calculate_percentage(number)

print(result)