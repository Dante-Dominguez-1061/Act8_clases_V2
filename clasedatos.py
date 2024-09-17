class Informacion:

    def mi_lista(self):
        lista_Nomperros = ["Boby","Dollar","Fany"]
        for x in lista_Nomperros:
            print(x)
    def mi_tupla(self):
        tupla_Razasperros = ("Chihuahua","Shih Tzu","Husky")
        for x in tupla_Razasperros:
            print(x)
    def mi_conjunto(self):
        conjunto_Edadperros = {"5","7","3"}
        for x in conjunto_Edadperros:
            print(x)
    def mi_diccionario(self):
        diccionario_Coloresperros = {
            "Boby: ":"Cafe",
            "Dollar: ":"Blanco",
            "Fany: ":"Negro"
        }
        for x,y in diccionario_Coloresperros.items():
            print(x,y)

# Creando el objeto

datos = Informacion()
print("Listado de nombre de perros")
datos.mi_lista()
print("Tupla de las razas de perros")
datos.mi_tupla()
print("Conjunto de edad de perros")
datos.mi_conjunto()
print("Diccionario de color de perros")
datos.mi_diccionario()