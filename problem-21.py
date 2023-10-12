def factors(num):
    l=[]
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
        else:
            continue
    return l

def is_prime(num):
    if num > 1:
        for a in range(2, num):
            if (num % a) == 0:
                return False
                break
        else:
            return True

for i in range(1, 10001):
    for j in range(1, 10001):
        if factors(i) == factors(j):
            if is_prime(i) or is_prime(j):
                continue
            else:
                if i == j:
                    continue
                else:
                    print(i, j)
        else:
            continue
