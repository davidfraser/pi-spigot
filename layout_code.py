import sys
r=raw_input
l=list(open('calcpi-compressed.html', 'rb').read())
w=sys.stdout.write
for c in"\n".join([r()for _ in[1]*input()]):w(c=='*'and(l and l.pop(0)or'.')or c)
w("".join(l))
