def persistence(n):
    count = 0
    while n > 9:
        count += 1
        n = eval("*".join(list(str(n))))
    return count

print(persistence(10000))
    