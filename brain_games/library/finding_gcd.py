def finding_gcd(num1, num2):
    max_num = max([num1, num2])
    min_num = min([num1, num2])
    gcd = min_num
    if max_num % min_num == 0:
        return min_num
    else:
        gcd = min_num // 2
    while gcd >= 1:
        if max_num % gcd == 0 and min_num % gcd == 0:
            return gcd
        else:
            gcd -= 1
    return gcd
