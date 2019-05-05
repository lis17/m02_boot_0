class Perro(): #el nombre de la clase siempre empieza en mayuscula
    def __init__(self, nombre, edad,peso):#función constructora, crea la instancia
        self.nombre = nombre
        self.edad= edad
        self.peso= peso
    
    def ladrar(self):#siempre poner self aunq luego no se pone cuando se invoca el método
        if self.peso >= 8:
            print('GUAU, GUAU')
        else:
            print('guau,guau')
            
    def __str__(self):
        return 'Soy el perro {}'.format(self.nombre)
        