states = {
	"Oregon" : "OR",
	"Florida" : "FL",
	"California" : "CA",
	"New York" : "NY",
	"Michigan" : "MI"
}

cities = {
	"CA" : "San Fransisco",
	"MI" : "Detroit",
	"FL" : "Jacksonville"
}

cities["NY"] = "New York"
cities['OR'] = "Portland"


print "-" * 10

print "NY state has:", cities["NY"]
print "OR state has:", cities["OR"]

print "-" * 10

print "Michigan's abbrevation is:", states["Michigan"]
print "Florida's abbrevation is:", states["Florida"]

print "-" * 10

print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)

print "-" * 10

for abbrevv, city in cities.items():
	print "%s has the city %s" % (abbrevv, city)

print "-" * 10

for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev])

print "-" * 10

state = states.get("Texas")
if not state:
	print "Sorry, no Texas"

city = cities.get("TX", "Does not exist")
print "The citiy for the state 'tx' is: %s" % city