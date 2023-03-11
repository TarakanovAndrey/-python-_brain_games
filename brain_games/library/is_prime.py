def is_prime_number(num):
    if num == 2:
        return 'yes'
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'
