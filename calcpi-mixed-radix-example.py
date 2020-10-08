import sys
n = 1000
l = 10*n//3
a = [2 for j in range(0, l)]
nines, predigit, started = 0, 0, False
for j in range(0, n):
    q = 0
    for i in range(l-1, -1, -1):
        x = 10*a[i] + q*(i+1)
        a[i] = x % (2*i+1)
        q = x // (2*i+1)
    q, a[0] = divmod(q, 10)
    if q == 9:
        nines += 1
    elif q == 10:
        sys.stdout.write(str(predigit+1) + '0'*nines)
        nines, predigit = 0, 0
    else:
        if started or predigit or nines:
            sys.stdout.write(str(predigit) + '9'*nines)
            if not started:
                sys.stdout.write('.')
                started = True
        nines, predigit = 0, q
sys.stdout.write(str(predigit) + '\n')