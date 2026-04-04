#funciones - son bloques de codigo que realiza una tarea especifica y que son reutilizables

#funcion sin parametros ni devolucion de valor
def saludar():
    print("hola, bienvenidos al curso de Python")
    
# funcion con parametros
def saludo(nombre):
    print("hola "+nombre+"bienvenido a clases")
    
#funcion que devuelve valores
def suma(a,b):
    return a + b

#establecer valores por defecto para los parametros de una funcion
def bienvenida(nombre="estudiante"):
    print("bienvenido",nombre)

#funcion con argumentos variables
def sumador(*args):
    return sum(args)

#llamada a la funcion
resultado = suma(10,20)
print("la suma es:",resultado)
#llamada a la funcion
saludo("Franco Yana")
saludo("Angela Tapira")
#llamada a la funcion
bienvenida()
bienvenida("susana")
#llamada a la funcion
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))

