"""PY0016"""
"""print("a.Numeros del 0 al 20")
for numero in range(0,21):
    print(numero)"""
"""print("b.Los pares del 0 al 20")
for numero in range(0,21):
    if numero % 2 == 0 :
        print(numero)"""

"""Para ir hacia atrás (de 0 a -20), debes indicar un paso negativo:"""
"""print("Los impares del 0 al -20")

for numero in range(0,-21,-1):
    if numero % 2 !=0:
        print(numero)"""
"""PY0017"""
"""def suma_numeros():
    total=0
    for numero in range(0,101):
        if numero % 2 ==0:
            total +=numero

    return total

resultado=suma_numeros()
print(resultado)

#Tambien se puede hacer así
resultado=sum(range(0,101,2)) #range(101) genera números del 0 al 100
print(resultado)"""
"""PY0019"""
"""while True:
    entrada=input("Introduce un numero: ")

    try:
        numero = int(entrada)
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")
        continue #Vuelve al inicio del bucle

    #Verificamos si el numero es impar
    if numero % 2 != 0:
        print(f"{numero} es impar. ¡Programa terminado!")
        break #Salimos del bucle porque el número es impar
    else:
        print(f"{numero} no es impar. Intenta otra vez.")"""

#PY0014
#num1=int(input("Introduce primer numero:"))
#num2=int(input("Introduce segundo numero:"))
#num3=int(input("Introduce tercer numero:"))
"""PY0020"""
"""while True:
    try:
        num1=int(input("Introduce un numero:").strip())
        num2=int(input("Introduce otro numero").strip())

    except ValueError:
        print("Introduce un numero entero\n")
        continue

    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Restar")
    print("5. Salir\n")

    opcion= input("Introduce un opcion: ").strip().lower()
    if (opcion =="sumar"):
        suma=(num1+num2)
        print(f"Suma : {suma}")
        hay que terminarlo
        """

"""PY0018"""
"""registro= "zeréP nauJ, 01"

cadena2= registro [::-1]
print(cadena2)

nota, nombre= cadena2.split(",")
print(f"{nombre} ha sacado un: {nota}")"""

#PY0043
# Pedimos al usuario que introduzca una cadena
# .strip() quita espacios al inicio y al final
# .lower() convierte todas las letras a minúsculas
# .replace(" ", "") elimina los espacios dentro de la cadena
#cadena = input("Introduce una cadena:").strip().lower().replace(" ", "")

# Creamos una lista vacía para guardar las letras que ya hemos contado
#ocurrencias = []

# Recorremos cada letra de la cadena
#for letra in cadena:
    # Verificamos si ya contamos esta letra antes
 #   if letra not in ocurrencias:
        # Creamos un contador para esta letra
  #      contador = 0
        # Recorremos de nuevo toda la cadena para contar cuántas veces aparece la letra
   #     for i in cadena:
#            if i == letra:
#                contador += 1  # Si encontramos la letra, sumamos 1 al contador
        # Imprimimos el resultado de cuántas veces aparece esta letra
 #       print(f"La letra {letra} aparece {contador} veces")
        # Agregamos la letra a la lista de letras ya contadas
  #      ocurrencias.append(letra)

#PY0013
"""import time
frase= input("Introduce una cadena").lower()

letraO= input("Introduce una letra:\t").lower()
letraR=input("Introduce letra reemplazo\t").lower()

if len(letraO)!= 1 or len(letraR) != 1:
    print("Solo puedes introducir un caracter para reemplazar")
    time.sleep(3)
    exit(1)
nueva_frase= frase.replace(letraO,letraR);
#¿Qué se modificaría si solo quisieses cambiar las dos primeras ocurrencias?
#nueva_frase=frase.replace(letraO, letraR,2)
print(f"Salida:{nueva_frase}")"""
#PY0001
#LISTA DE EJEMPLOS
"""tareas= ["Limpiar", "Comprar Comida", "Salir"]
#Recorremos la lista con enumerate, empezando desde 1
for i, tarea in enumerate(tareas, start=1):
    print(f"{i}. {tarea}")

#Sin enumerate
for i in range(len(tareas)):
    print(f"{i+1}. {tareas[i]")   
    """
#PY0002
"""listaPrecios= [20,22.30,13.5,6]
listaPreciosDto=[]
listaPrecioAct=[]
for i in range(len(listaPrecios)):
    precio_antes=listaPrecios[i]
    if i%2==0:
        descuento=listaPrecios[i]*0.1

    else :
        descuento=listaPrecios[i]*0.2

    precio_despues = precio_antes -descuento

    #guardamos resultados
   
    listaPrecioAct.append(precio_despues)

 # Mostramos cambios
    print(f"indice_lista={i}, precio_antes={precio_antes:.2f}, precio_después={precio_despues:.2f}")

print("Lista de precios actualizados:", listaPrecioAct)"""

#PYOO15
"""matriz=[
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]"""
#Matriz original
"""print("Matriz Original")
for fila in matriz:
    print(fila)

#Recorremos cada fila de la matriz
for fila in matriz:
    suma=sum(fila[0:3]) #suma desde el indice 0 al 2
    fila[3]=suma# el valor de suma se añade en el indice 3

#Mostramos la matriz actualizada
print("Matriz actualizada")
for fila in matriz:
    print(fila)
    
#correccion clase
 matriz=[
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]

for fila in matriz:
    fila[3]= sum(fila[:3:])
    
print(matriz)   
    """

#PY0003
#Parte A
"""asistentes=[]

while True:
    nombre = input("Introduce un nombre: ")
    if (nombre.lower().strip() =="fin"):
        break

    asistentes.append(nombre)#añadimos el nombre a la lista
#Parte B
print(asistentes)
nombre2= input("Introduce el nombre que quieres consultar: ")
#Usamos count() para contar cuantas veces aparece
cantidad= asistentes.count(nombre2)
print(f"Nombre:('{nombre2}') ={cantidad}")

#Parte C
#Muestra por consola la primera posición en la que aparece el nombre anterior y elimina esta ocurrencia
indice=asistentes.index(nombre2)
print(f"El nombre aparece en el indice: {indice} ")
asistentes.pop(indice)#elimina el elemento cuando lo encuentra

#Parte D
nombre3= input("Introduce el asistente vip: ")
asistentes.insert(0,nombre3)

#Mostramos la lista final
print(f"Asistentes: {asistentes}")"""

#PY0004
"""menu=["ensalada","Sopa","Pasta"]
menu_hoy=menu.copy()
menu_hoy.extend(["Pescado","Postre"])
menu_hoy.pop(len(menu_hoy)-1)
menu_hoy.remove("Sopa")
menu_hoy.pop(2)
menuInvertido= menu_hoy[::-1]
print(menuInvertido)
menu.clear()
print(f"\nMenu base: {menu}")
print(f"\nMenu de hoy: {menu_hoy}")"""

#PY0025


"""listaPaises=["España","Argentina","Perú"]
contador=0 #ejecuciones del menu
contadorBien=0

while True:
    print("MENU. Elija una de las siguientes opciones marcando su número: ")
    print("1.Imprimir alfabéticamente en orden ascendente.")
    print("2.Imprimir alfabéticamente en orden descendente")
    print("3.Añadir País")
    print("4.Eliminar Pais")
    print("5.Salir")

    try:
        opcion= int(input("Introduce una opción (1-5):").strip())

        contador +=1


        if opcion < 1 or opcion > 5:
            print("Opcion fuera de rango (1-5).")
            continue


        match opcion:
            case 1:
                listaPaises.sort()
                print(f"Lista en orden ascendente: {listaPaises} \n\n")
            case 2:
                listaPaises.sort(reverse=True)
                print(f"Lista en orden descendente: {listaPaises} \n\n")
            case 3:  # si lista es mayor a 6 no puede insertar mas paise y tendra la opcion de eliminar 1 pais
                pais = input("Introduce un País: ").strip().capitalize()
                if pais == "":
                    print("No se puede añadir un país vacio.")
                    continue #vuelve al menu
                elif pais in listaPaises:
                    print(f"{pais} ya esta en la lista.")
                    continue
                elif len(listaPaises) >= 6:
                    print("No se pueden insertar más de 6 países, elimina uno primero")
                    ePais = input("Introduce el país a eliminar: ").strip().capitalize()

                    if ePais in listaPaises:
                        listaPaises.remove(ePais)  # elimina por nombre
                        print(f"{ePais} eliminado correctamente.")
                        listaPaises.append(pais)
                        print(f"{pais} añadido correctamente")
                    else:
                        print(f"{ePais}no esta en la lista, no se puede añadir {pais}.")
                else:
                    listaPaises.append(pais)
                    print(f"{pais} añadido correctamente.")
                print(f"Lista actual de países: {listaPaises}\n\n")
            case 4:
                eliminarPais = input("Introduce el País a eliminar: ").strip().capitalize()
                if eliminarPais=="":
                    print("No se puede eliminar un país vacío")
                    continue
                if eliminarPais in listaPaises:
                    listaPaises.remove(eliminarPais)  # elimina por nombre
                    print(f"{eliminarPais} eliminado correctamente")
                else:
                    print("No esta en la lista no se puede eliminar")
                print(f"Lista actual de países: {listaPaises}\n\n")
            case 5:

                break

        if opcion in (1,2,3,4):
            contadorBien += 1  # ejecuciones validas del 1 al 4
            print(f"{'#'*70}\n\n")
    except ValueError:
        print("Error: Introduce un numero del 1 al 5\n")
        contador +=1
    finally:
        print(f"Numero de ejecuciones del menú: {contador} ")


print("Gracias,Has salido del programa")
print(f"Numero de ejecuciones que han ido bien {contadorBien}")
print("Un saludo")"""

#PY0028
"""pizzas=["Margarita","Carbonara","Barbacoa"]
precios=[7.50,8.50,9.50]
ingredientesExtras=["Queso","Bacon","Barbacoa"]
precioIngredientesExtras=[1.50,1.75,1.25]

while True:
    print("Pizzeria San Jose")
    ##asegurarme de que la cantidad que introduce es valida
    try:
        dineroUsuario=float(input("Introduce cantidad de dinero que tenga:"))
        if dineroUsuario <= 0:
            print("La cantidad tiene que ser un numero positivo")
            continue
        break #para salir del bucle
    except ValueError:
        print("El valor no es un numero")

#Mostrar pizzas y su precio
for i in range (len(pizzas)):
    print(f"{i+1}.{pizzas[i]}: {precios[i]:.2f}")

while True:
    #Comprobar si el numero que inserta esta dentro de las opciones
    try:
        opcion=int(input("Introduce una opción: "))
        if opcion <1 or opcion >3:
            print("El numero insertado no está en el rango")
            continue
        break
    except ValueError:
        print("El valor no es un numero")

    #Obterner pizza y precio
pizzaElegida = pizzas[opcion-1]
precioElegida= precios[opcion-1]

#Mostrar al usuario la pizza elegida
print(f"Has elegido la pizza {pizzaElegida} que cuesta {precioElegida:.2f}€.")
saldoRestante= dineroUsuario - precioElegida
print(f"Saldo restante: {saldoRestante:.2f}" )

#Preguntar si quiere añadir ingredientes extras
extrasElegidos=[]
precioExtras=0

eligeExtras=input("¿Quieres añadir ingredientes extras (s/n): ").strip().lower()

if eligeExtras=="s":
    while True:
        print("Ingredientes extra disponibles:")
        for i in range (len(ingredientesExtras)):
            print(f"{i+1}.{ingredientesExtras[i]}: {precioIngredientesExtras[i]:.2f}€")

        try:
            pedirExtra=int(input("Elige el número del ingrediente extra(1-3)"))
            if pedirExtra < 1 or pedirExtra > 3:
                print("Número fuera de rango.\n")
                continue
        except ValueError:
            print("El valor no es un número.\n")
            continue

        extrasElegidos.append(ingredientesExtras[pedirExtra-1])
        precioExtras += precioIngredientesExtras[pedirExtra-1]
        print(f"{ingredientesExtras[pedirExtra-1]} añadido correctamente")

        otroExtra=input("¿Quieres añadir otro ingrediente? (s/n):").strip().lower()
        if otroExtra!="s":
            break
#Calcular importe a pagar
total = precioElegida + precioExtras
print(f"\nEl total del pedido es de {total:.2f} €.")

if total > dineroUsuario:
    print("No tienes suficiente dinero para pagar tu pedido.")
else:
    cambio = dineroUsuario - total
    print(f"Pedido completado. Tu cambio es {cambio:.2f} €.")"""

#PY0027
"""usuarios={"Marta","David","Elvira","Juan","Marcos"} #Cuando me pide un conjunto es con {}
administradores={"Juan","Marta"}#si pide lista es con []
administradores.discard("Juan")#la diferencia con remove es que lo elimina y si el elemento no existe lo ignora
administradores.add("Marcos")

for indice in usuarios:
    if indice in administradores:

        print(f"{indice} es administrador")
    else:
        print(f"{indice} no es administrador")"""


#PY0005
"""
personasTaller={"Pilar","Fernando","Lucía","Gonzalo"}
#1
print("===ALTA INDIVIDUAL DE INSCRITOS===")
while True:
    nombre=input("Introduce un nombre: ").strip().capitalize()
    if nombre.lower().strip() == "fin":
        break
    if nombre=="":
        print("No puedes introducir un nombre vacío")
        continue
    personasTaller.add(nombre)
    print(f"{nombre} añadido correctamente")

print("Personas inscritas en el taller:")
for personas in personasTaller:
    print(f"- {personas}")
#2
print("\n=== ALTA POR LOTES DE INSCRITOS ===")
entrada= input("Introduce varios nombres separados por comas:").strip()
#comprensión de conjuntos
nuevosLotes={nombrelote.strip().capitalize() for nombrelote in entrada.split(",") if nombrelote.strip() != ""} # maria, , juan   , pepe,
#unir conjuntos (puedes usar .update() o el operador |)
personasTaller.update(nuevosLotes)#añade varios usuarios
#otra forma
#print("\n=== ALTA POR LOTES FOR")
loteNuevo=set()
for lote in entrada.split(","):
    if lote.strip() != "":
        loteNuevo.add(lote.strip())
#se está mostrando por comprension de conjutos
print("Usuarios por lotes:")
for lotes in nuevosLotes:
    print(f"-{lotes}")

#3
copiaConjunto=personasTaller.copy()
print("Mostrar copia")
for copia in copiaConjunto:
    print(f"- {copia}")
#4
eliminarNombre= input("introduce un nombre a eliminar").strip().capitalize()
if eliminarNombre in copiaConjunto:
    copiaConjunto.remove(eliminarNombre)
    print(f"{eliminarNombre} eliminado correctamente.")
else:
    print("El nombre no existe en el conjunto")

print("Mostrar lista nombre eliminado")
for eliminado in copiaConjunto:
    print(f"- {eliminado}")
#5
consulta= input("introduce un nombre para consultar si está inscrito: ").strip().capitalize()
if consulta in copiaConjunto:
    print(f"{consulta} está inscrito en el taller.")
else:
    print(f"{consulta} no está inscrito en el taller")

#6
grupo={"Fernando","Lucía","Ana"}
inscritosDelGrupo= grupo & personasTaller
consultaGrupo= input("Introduce un nombre para consultar si alguién del grupo está inscrito en el taller").strip().capitalize()
if consultaGrupo in inscritosDelGrupo:
    print(f"{consultaGrupo} esta inscrito en el taller")
else:
    print(f"{consultaGrupo} no esta inscrito en el taller")

#7
print("Mostrar el numero total de inscritos y la lista ordendana")
print(f"Total de inscritos: {len(copiaConjunto)}")
for nombre in sorted(copiaConjunto):
    print(f"- {nombre}")"""
#PY0023
#importa el modulo time, contiene funciones relacionadas con el tiempo time.sleep()
"""import time

frase = input("Introduce una cadena: ").lower()

letraO= input("Introduce una letra: \t ").lower()
letraR= input("Introduce una letra a reemplazar: \t").lower()
#comprueba q la longitud de la letra sea 1
if len(letraO)!=1 or len(letraR)!=1:
    print("Solo puedes introducir un carácter para reemplazar.")
    #Pausa la ejecución 3 segundos para que el usuario vea el mensaje de error
    time.sleep(3)
   #termina el programa con código de salido 1 (indica un error)
    exit(1)

#Uso de set
caracteres_frase=set(frase)
if letraO not in caracteres_frase:
    print(f"El caracter {letraO} no esta en la cadena, no se reemplaza nada.")

else:
    frase= frase.replace(letraO,letraR)

print(f"Salida: {frase}")"""


#py0026
"""
listaPaises={"España","Argentina","Perú"}
contador=0 #ejecuciones del menu
contadorBien=0

while True:
    print("MENU. Elija una de las siguientes opciones marcando su número: ")
    print("1.Imprimir alfabéticamente en orden ascendente.")
    print("2.Imprimir alfabéticamente en orden descendente")
    print("3.Añadir País")
    print("4.Eliminar Pais")
    print("5.Salir")

    try:
        opcion= int(input("Introduce una opción (1-5):").strip())

        contador +=1


        if opcion < 1 or opcion > 5:
            print("Opcion fuera de rango (1-5).")
            continue


        match opcion:
            case 1:
                print("Lista en orden ascendente:")
                for pais in sorted(listaPaises):
                    print(f"- {pais}\n\n")

            case 2:

                print(f"Lista en orden descendente:")
                for pais in sorted(listaPaises, reverse=True):
                    print(f"- {pais}\n\n")
            case 3:  # si lista es mayor a 6 no puede insertar mas paise y tendra la opcion de eliminar 1 pais
                pais = input("Introduce un País: ").strip().capitalize()
                if pais == "":
                    print("No se puede añadir un país vacio.")
                    continue #vuelve al menu
                elif pais in listaPaises:
                    print(f"{pais} ya esta en la lista.")
                    continue
                elif len(listaPaises) >= 6:
                    print("No se pueden insertar más de 6 países, elimina uno primero")
                    ePais = input("Introduce el país a eliminar: ").strip().capitalize()

                    if ePais in listaPaises:
                        listaPaises.remove(ePais)  # elimina por nombre
                        print(f"{ePais} eliminado correctamente.")
                        listaPaises.add(pais)
                        print(f"{pais} añadido correctamente")
                    else:
                        print(f"{ePais}no esta en la lista, no se puede añadir {pais}.")
                else:
                    listaPaises.add(pais)
                    print(f"{pais} añadido correctamente.")
                print(f"Lista actual de países: {listaPaises}\n\n")
            case 4:
                eliminarPais = input("Introduce el País a eliminar: ").strip().capitalize()
                if eliminarPais=="":
                    print("No se puede eliminar un país vacío")
                    continue
                if eliminarPais in listaPaises:
                    listaPaises.remove(eliminarPais)  # elimina por nombre
                    print(f"{eliminarPais} eliminado correctamente")
                else:
                    print("No esta en la lista no se puede eliminar")
                print(f"Lista actual de países: {listaPaises}\n\n")
            case 5:

                break

        if opcion in (1,2,3,4):
            contadorBien += 1  # ejecuciones validas del 1 al 4
            print(f"{'#'*70}\n\n")
    except ValueError:
        print("Error: Introduce un numero del 1 al 5\n")
        contador +=1
    finally:
        print(f"Numero de ejecuciones del menú: {contador} ")


print("Gracias,Has salido del programa")
print(f"Numero de ejecuciones que han ido bien {contadorBien}")
print("Un saludo")"""

#PY0006
inventario_inicial= {'CUS001':12,'CUS002':5,'CUS003':0}
ventas=['CUS001','CUS002','CUS001','CUSSOO4']
reposiciones={'CUS002':10,'CUS004':7}

#Realizar las siguientes operaciones
#1 copia inventario
copia_inventario=dict.copy(inventario_inicial)
#2
#Lista de avisos
avisos=[]
#Procesar ventas
for codigo in ventas:
    #si el codigo no existe, añade con stock 0 antes de restar
    stock_actual=copia_inventario.get(codigo,0)
    #CUSSOO4 NO EXISTE EN INVENTARIO SE AÑADE CON STOCK 0
    if codigo not in copia_inventario:
        #registramos aviso(avisos.append(...) NO imprime nada, solo guarda el texto dentro de la lista avisos)
        avisos.append(f"Código {codigo} no existía en inventario, se añadió con stock 0")
    #Restar 1 unidad
    copia_inventario[codigo] = stock_actual-1

# Mostrar avisos
for a in avisos:
    print(a)

#Mostrar inventario final clave + stock
"""print("Inventario final:")
for codigo,stock in copia_inventario.items():

    print(f" {codigo} : {stock} ")

#3 aplica las reposiciones sumando cantidades a los stocks existentes no usar update
print("Sumar reposiciones a los stocks existentes")
#devuelve codigo y cantidad  (clave, valor)tuplas del diccionario de reposiociones
for codigo, cantidad in reposiciones.items():
    #busca stock actual del codigo en el diccionario copia si el codigo no existe devuelve 0
    stock_actual=copia_inventario.get(codigo,0)
    #Calcula la nueva cantidad
    copia_inventario[codigo] = stock_actual + cantidad

    print(f"Nuevo stock: {codigo} : {copia_inventario[codigo]}")
#4 Generar un informe
#Cuenta todas las claves (productos), incluso los añadidos por ventas o reposiciones
numero_referencias= len(copia_inventario)
#suma todos los valores(unidades en stock
unidades_totales= sum(copia_inventario.values())
#Mostrar informe
print("INFORME DEL INVENTARIO")
print(f"Número de referencias: {numero_referencias}")
print(f"Unidades totales: {unidades_totales}")

#5 Elimina los productos con stock 0 o negativo
print("\nEliminar productos con stock 0 o negativo")
""""""copia_inventario.items() devuelve pares (clave, valor) del diccionario.
Ejemplo: ('CUS001', 10), ('CUS003', 0), ('CUS004', -1).

for codigo, stock in copia_inventario.items() → desempaqueta cada par:

codigo toma la clave ('CUS003')

stock toma el valor (0)

if stock <= 0 → filtra solo los que tienen stock 0 o negativo.

codigo (el primero) es lo que se agrega a la lista final.

Resultado final: claves_a_borrar = ['CUS003', 'CUS004']."""
"""claves_a_borrar= [codigo for codigo, stock in copia_inventario.items() if stock <=0]

for codigo in claves_a_borrar:
    copia_inventario.pop(codigo)

#Mostrar inventario limpio
for codigo, stock in copia_inventario.items():
    print(f"{codigo} : {stock}")

#6 Consulta del stock de un codigo, en caso de que no exista(mostrar el mensaje no existe)
consulta= input("Introduce un codigo: ").upper().strip()
if consulta in copia_inventario:
    #copia_inventario["CUS002"]   →  14
    print(f"El codigo {consulta}: {copia_inventario[consulta]}")
else:
    print(f"El codigo {consulta} no existe")

#7 Borrar el objeto diccionario
#Eliminar todas las claves y valores
copia_inventario.clear()

print(copia_inventario)
#eliminar la variable entera
del copia_inventario
#print(copia_inventario) si hago el print da error"""
