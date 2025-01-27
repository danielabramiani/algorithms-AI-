def hw2_1(a, b, c):
    if a == 0 or b == 0:
        return 0
    if a > b:
        return 0

    result = 0
    start = (a // c) + 1 if a % c != 0 else a // c
    end = b // c

    if start <= end:
        result = end - start + 1
    return result

def hw2_2_to_base(n, base):
    result = ''
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base
    
    return result

def hw2_2_from_base(n_str, base):
    result = 0
    digits = {}
    digits['0'] = 0
    digits['1'] = 1
    digits['2'] = 2
    digits['3'] = 3
    digits['4'] = 4
    digits['5'] = 5
    digits['6'] = 6
    digits['7'] = 7
    digits['8'] = 8
    digits['9'] = 9
    digits['A'] = 10
    digits['B'] = 11
    digits['C'] = 12
    digits['D'] = 13
    digits['E'] = 14
    digits['F'] = 15
    
    for i, char in enumerate(n_str[::-1]):
        result += digits[char] * (base ** i)
    
    return result
