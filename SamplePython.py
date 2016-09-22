Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
def fastexp(b,e,m):
	n=1
	while e!=0 :
		if e%2 ==1 :
			n=(n*b)%m
		e=e/2
		b=(b*b)%m
	return n

>>> def find10():
	counter=0
	x=1000000001
	while counter < 10:
		if fastexp(2,x-1,x)==1 :
			counter=counter+1
			print(x)
		x=x+2

		
>>> find10()
1000000007
1000000009
1000000021
1000000033
1000000087
1000000093
1000000097
1000000103
1000000123
1000000181
>>> 
