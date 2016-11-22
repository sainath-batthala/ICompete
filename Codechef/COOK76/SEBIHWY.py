tc=input()
def mod(a,b):
	if a>b:
		return a-b
	else:
		return b-a
for test in xrange(tc):
	p = raw_input().split(" ")
	s = (int)(p[0])
	sg = (int)(p[1])
	fg = (int)(p[2])
	d = (int)(p[3])
	t = (int)(p[4])
	act = s*t+180*d
	se = mod(act, sg*t)
	fe = mod(act, fg*t)
	if se == fe:
		print "DRAW"
	elif se < fe:
		print "SEBI"
	else:
		print "FATHER"