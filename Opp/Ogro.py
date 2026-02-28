from Enemigo import *
import random
class Ogro:
    def __init__(self, puntos_energia, nivel, ataque):
        self.tipo = "Ogro"
        self.puntos_energia = puntos_energia
        self.nivel = nivel
        self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.tipo

    def habla(self):
        print(f"{self.get_tipo_enemigo()} tiene {self.puntos_energia} de energia y puede hacer ataques de {self.ataque}")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funcional_ataque_especial = random.random() < 0.20
        if funcional_ataque_especial:
            self.ataque += 4
            print("Ogro enojado e incensato su ataque por 4!!")