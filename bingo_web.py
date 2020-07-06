from jinja2 import Template
from src.bingo import *

template = Template(open('src/plantilla.j2').read())

carton_web = template.render(carton=newCarton())

file = open("bingo_output.html","w")

file.write(carton_web)

file.close()