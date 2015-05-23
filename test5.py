from my_parser import *
#x = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])

x = parse_sentence([('verb', 'run'), ('direction', 'north')])

print x.subject

print x.verb

print x.object

x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])

print x.subject

print x.verb

print x.object