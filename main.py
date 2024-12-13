import random
print("este es el generador  de contraseñas, juntos crearemos tu contraseña, para ello, nesecitamos tus preferencias, si deseas mayusculas, minuscula, numeros y/o sombilos")
longitud = int(input("porfavor, ingresa cunatos caracteres quieres que sea la longitud de tu cadena: "))
print("-------------------------------------------------------------------------------------------------------------------------")

usuario =int(input("(ingrese '1' si desea todo), (2 si solo desa mayusculas, minusculas y numeros) (3 si solo desea mayusculas y minusculas) (4 si solo desea mayusculas) (5 si solo desea minusculas): "))

if usuario == 1:
    minuscula = input("ingrese la cantidad de letreas mayusculas que deseas en la contaseña: ")
    mayuscula = input("ingrese la cantidad de letreas minuscula que deseas en la contaseña: ") 
    numeros = input("ingrese cuantos numeros quieres que tenga tu contraseña: ")
    simbolos = input("ingrese la cantidad de simbolos que deseas en la contaseña")     


    cl_minuscula = len(minuscula)
    cl_mayuscula = len(mayuscula)
    cl_numeros = len(numeros)
    cl_simbolos = len(simbolos)


elif usuario == 2:
    minuscula2 = int(input("ingrese la cantidad de letreas mayusculas que deseas en la contaseña: "))
    mayuscula2 = int(input("ingrese la cantidad de letreas minuscula que deseas en la contaseña: ")) 
    numeros2 = int(input("ingrese cuantos numeros quieres que tenga tu contraseña: "))
    caracteresmin = "abcdefghijklmnñopqrstuvwxyz"
    caracteresmay = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    caracteres = "1234567890"

    random_index = random.randint(0, minuscula2)
    random_char = caracteresmin[random_index]
    random_index1 = random.randint(0, mayuscula2)
    random_char1 = caracteresmay[random_index]
    random_index2 = random.randint(0, numeros2)
    random_char2 = caracteres[random_index]


    contraseña_generada = random_char + random_char2+ random_char1

    if contraseña_generada > longitud: print (f"ingrese menos caracterese a {longitud}")
    else: print(f"la contraseña generada es: ({contraseña_generada})")