def solution(number):
    sum = 0
    if number <= 0:
        return sum
    for number in range(0, number):
        if (number % 5 == 0) |  (number % 3 == 0):
            sum +=number
    return sum
print(solution(10))