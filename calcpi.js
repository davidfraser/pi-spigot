function calcPi() {
    var q=1, r=0, t=1, k=1, n=3, l=3;
    while (true) {
        if (4*q+r-t < n*t) {
            process.stdout.write(''+n);
            nr = 10*(r-n*t);
            n  = Math.floor((10*(3*q+r))/t)-10*n;
            q  = q*10;
            r  = nr;
        } else {
            nr = (2*q+r)*l;
            nn = Math.floor((q*(7*k)+2+(r*l))/(t*l));
            q = q*k;
            t = t*l;
            l = l+2;
            k = k+1;
            n  = nn;
            r  = nr;
        }
    }
}
calcPi();
