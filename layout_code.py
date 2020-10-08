import sys
r=input
l=list(open('calcpi-compressed.html', 'r').read())
w=sys.stdout.write
for c in"\n".join([r()for _ in[1]*int(r())]):w(c=='*'and(l and l.pop(0)or'.')or c)
w("".join(l))
