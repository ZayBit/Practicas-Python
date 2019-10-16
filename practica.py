#Practicas Python

# Crear una funcion simple con 2 parametros
def nameAndYear(name,year):
    # Mostrar un mensaje con los parametros recibidos
    print(name,year)
# Invocar a la funcion con 2 parametos (nombre,edad)
nameAndYear('frank',22)
# Declaracion de variables
a = 2
b = 2
#Mostrar a + b concatenandolas
print (a + b)
# Condicional
if a == b :
    print ('A y B son iguales')
#else if
elif a < b :
    print('A es menor a B')
else :
    print('es A o B tienen valores distintos')
#creacion de los arrays y llamada de los elementos del mismo
lista_array = ['frank','pepe','carlos']
print(lista_array[1]) #Salida 'pepe'

# Diccionario
Persona = {
    'nombre':'Frank',
    'edad'  :22,
    'ciudad':'mexico',
    'sexo'  :'hombre'
}
#Mostrar valores del directorio por su nombre
print(Persona['nombre'])
#Sustutuir valores del directorio
Persona['nombre'] = 'Elena'
print(Persona['nombre'])

#Convertir int a string y inversa
n1 = '2'
#mostrar el tipo de la variable n1 antes de cambiarla
print(type(n1))
#comprobar si es un tipo string
if type(n1) is str:
    #convertir la variable tipo string a tipo int
    n1 = int(n1)
    #mostrar de nueva cuenta el tipo de vairable pero modificada
    print (type(n1))

#Clases
class Heroe:
#la función __init __ () para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias para realizar cuando se crea el objeto
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    #Mostrar los datos de una manera mas variada
    def mensaje(self):
            print('Hola heroe parece que tu nombre es '  + self.name + ' y tienes ' + str(self.age))
#Crear un nuevo objeto Heroe
pu1 = Heroe('feer','22')
# Mostrar la funcion mensaje() de pu1
print(pu1.mensaje())
# Bucles For Loops
lista_edades = [22,35,23]
# Bucle ForIn
for persona in lista_edades:
    print(persona)
####
# for i in range(0,2):
#     if i == 2:
#         print(i)
#         break


# "switch-case"
def switch (value):
    return {
        1: "Dificultad facil",
        2: "Dificultad normal",
        3: "Dificultad dificil",
        4: "Dificultad legendaria"
    }.get(value)

dificultad = int(input("Seleccione dificultad: "))
print(dificultad)
print(switch(dificultad))