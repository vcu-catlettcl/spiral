def spiralize(number):
    n = 1
    cnt = 0
    inc = 2
    total = 0

    while n <= ** number 2:
        total += n
        n += inc
        cnt += 1
        if cnt == 4:
            inc += 2
            cnt = 0

    return total
