def print_two(*args):
	arg1, arg2 = args
	print "args1: %r, arg2: %r" % (arg1,arg2)

def prtint_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)


def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin' :("


print_two("Folke", "Johan")
prtint_two_again("David","Tuan")
print_one("So lonenly")
print_none()