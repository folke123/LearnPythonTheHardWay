def func1():
	#global a 
	a= 5
#	def func2():
#		print a
	func2()


def func2():
#	global a
	print a
	#a+=5

a= 10
func1()
print a