from guerrero import Guerrero
from hechicero import Hechicero
from espada import Espada
from conjuro import Conjuro

#crear personajes 
guerrero = Guerrero("Thorg", 50)
hechicero = Hechicero("Merlin", 50)

#crear objetos 
espada = Espada("Espada del valor", 50)
conjuro = Conjuro("Bola de fuego", 30)

#equipar objetos 
guerrero.equipar_arma(espada)
hechicero.aprender_conjuro(conjuro)

#acciones del juego 
guerrero.atacar(hechicero)
hechicero.lanzar_conjuro(guerrero)
