from Enemigo import *
import random 

class Zombie:
    def __init__(self, puntos_energia, nivel, ataque=3):
        self.tipo = "Zombie"
        self.puntos_energia = puntos_energia
        self.nivel = nivel
        self.ataque = ataque
    def get_tipo_enemigo(self):
        return self.tipo
    def habla(self):
            print("Hummm.....")

    def propagar_enfermedades(self):
            print("El Zombie esta tratando de propagar la enfermedad!!")
    def ataque_especial(self):
          print("Zombie ataque especial")
          funciona_ataque_especial = random.random() <0.50
          if funciona_ataque_especial:
                self.ataque += 2
                print('Zombie ha generado su energia con 2HP!!!')