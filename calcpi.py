def strlen(i):
    return len(str(i))

def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    n_digits = 0
    n_calcs = 0
    calc_effort = 0
    print("  #    # *𝜋* len_q len_r len_t len_k len_n len_l")
    print("------------------------------------------------")
    while n_digits < 1000:
        qd, rd, td, kd, nd, ld = strlen(q), strlen(r), strlen(t), strlen(k), strlen(n), strlen(l)
        n_calcs += 1
        calc_effort += qd + rd + td + kd + nd + ld
        if 4*q+r-t < n*t:
            yield n
            n_digits += 1
            calc_eff = float(calc_effort) / n_digits
            print("%3d %4d (%d) %5d %5d %5d %5d %5d %5d : %6d %0.2f" % (n_digits, n_calcs, n, qd, rd, td, kd, nd, ld, calc_effort, calc_eff))
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            # print("... %4d ... %5d %5d %5d %5d %5d %5d" % (n_calcs, qd, rd, td, kd, nd, ld))
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr
 
import sys
pi_digits = calcPi()
i = 0
for d in pi_digits:
    str(d)
    # sys.stdout.write(str(d))

