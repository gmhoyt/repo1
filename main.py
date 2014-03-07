
import webapp2
import jinja2
import os

directorio_plantillas = os.path.join(os.path.dirname(__file__), 'Vistas')
entorno_jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(directorio_plantillas), 
	    autoescape=True)
def render_srt(plantilla, **params):
	p=entorno_jinja.get_template(plantilla)
	return p.render(params)

class Handler(webapp2.RequestHandler):
	def render(self, plantilla, **kw):
		self.response.out.write(render_srt(plantilla, **kw))

	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
		
class MainHandler(Handler):
    def get(self):
    	libros = [{'nombre':'Harry Potter','Fecha':'2012'},
		{'nombre':'Juegos del Hambre','Fecha':'2013'}]
        self.render('index.html', contenido = libros)
				
app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)