import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST=False


for word in urlopen(WORD_URL).readlines():
#	print "'"+word+"'"
#	print "stripped: '"+word.strip()+"'"
	WORDS.append(word.strip())


def convert(snippet,phrase):
	#list comprehension
	class_names = [w.capitalize() for w in
				   random.sample(WORDS,snippet.count("%%%"))]


	other_names = random.sample(WORDS,snippet.count("***"))
	results = []
	param_names = []

	for i in range (0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(",".join(random.sample(WORDS,param_count)))


	for sentence in snippet, phrase:
		#result = sentence[:]

		for word in class_names:
			sentence = sentence.replace("%%%",word,1)

		for word in other_names:
			sentence = sentence.replace("***",word,1)

		for word in param_names:
			sentence = sentence.replace("@@@",word,1)

		results.append(sentence)

	return results


try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet,phrase)
		if PHRASE_FIRST:
			question, answer = answer, question

		print question
		print "prhases start"
		print PHRASES
		print "prhases end"

		raw_input("> ")
		print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nbye"
