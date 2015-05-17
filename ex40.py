class Song(object):

	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		print "say please"

	def please_sing_me_a_song(self):
		for line in self.lyrics:
			print line


happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"with pockets full of shells"])

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()

super_song = ["This is a super good song",
			  "It only has two rows of lyrics"]

super_song_song = Song(super_song)
super_song_song.please_sing_me_a_song()