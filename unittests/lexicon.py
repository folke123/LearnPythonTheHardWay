lexicon = {"north" : "direction",
		   "south" : "direction",
		   "west" : "direction",
		   "east" : "direction",
		   "go" : "verb",
		   "kill" : "verb",
		   "eat": "verb",
		   "the" : "stop",
		   "in" : "stop",
		   "of" : "stop",
		   "bear" : "noun",
		   "princess" : "noun"}

def convert_number(number_as_string):
	try:
		return int(number_as_string)
	except ValueError:
		return None


def scan(input):
	result = []
	words = input.split()
	for word in words:
		word = word.lower()
		type_of_word = lexicon.get(word)
		#check if it is a number
		if type_of_word == None:
			temp = convert_number(word)
			if temp == None:
				type_of_word = "error"
			else:
				type_of_word = "number"
				word = temp
		result.append((type_of_word,word))
		
	return result
	