from personaje import Personaje

class hechicero(Personaje):
    def __init__(self, nombre, salud):
        super().__init__(nombre, salud)
        self.conjuros = []

    def aprender_conjuro(self, conjuro):
        self.conjuros.append(conjuro)
        print(f"{self.nombre} ha aprendido el conjuro: {conjuro.nombre}")

        def lanzar_conjuro(self, objetivo):
            if self.conjuros:
                conjuro = self.conjuros[0]
                print(f"{self.nombre} lanza el conjuro: {conjuro.nombre}")
                objetivo.recibir_danio(conjuro.poder)
            else:
                print(f"{self.nombre} no conoce ningun conjuro")
                