import web

urls = (
	"/hello", "Index"
	)

app = web.application(urls,globals())

render = web.template.render("templates/")

class Index:
	def GET(self):
		#form = web.input(name="Nobody",surname="svanslos")
		#greeting = "Hello, %s" % form.name + form.surname
		#return render.index(greeting = greeting)

		return render.hello_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" %(form.greet,form.name)
		return render.index(greeting=greeting)

if __name__ == "__main__":
	app.run()