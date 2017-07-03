#finds factors for numbers between 2 and anyother num

for n in range(6857,6858):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
