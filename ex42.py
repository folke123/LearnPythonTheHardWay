class Animal(object):
	def __init__(self,name):
		self.name=name

	def talk(self):
		print "AnimalSpeak:", self.name


class Dog(Animal):
	def __init__(self,name):
		#vad blir skillnaden?
		super(Dog,self).__init__(name)
		#self.name=name

	def talk(self):
		print "DogSpeak:", self.name
		super(Dog,self).talk()

	def secretDogMethod(self):
		print "I am secret dog method woof"


Folke = Animal("Folke")
Folke.talk()

plutten = Dog("Pluttis")

plutten.talk()
plutten.secretDogMethod()

