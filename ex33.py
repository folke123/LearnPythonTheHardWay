#i = 0
#numbers = []

def loop_function(count, increment_size):
	numbers = []
	i = 0
	while i< count:
		numbers.append(i)
		i+=increment_size
	return numbers

def loop_function_for(count,increment_size):
	numbers = []
	for num in range(0,count,increment_size):
		numbers.append(num)
	return numbers

#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)
#
#	i +=1
#	print "Numbers now: ", numbers
#	print "At the botom i is %d" % i
numbers = loop_function_for(10,2)


print "The numbers: "

for num in numbers:
	print num