numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    is_prime = True
    if num==1:
        print('1 - не является простым и сложным числом')
    elif num < 4:
        primes.append(num)
    elif num % 2 == 0 :
        not_primes.append(num)
    else:
        for div in range(2, int(num**0.5) + 1)  :
            if num % div ==0 :
                is_prime = False
                not_primes.append(num)
                #print('Not primes: ', num)
                break
        if is_prime:
            primes.append(num)
print(f'{primes = }')
print(f'{not_primes = }')

