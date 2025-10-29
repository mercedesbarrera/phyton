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
cadena = input("Introduce una cadena:").strip().lower().replace(" ", "")

# Creamos una lista vacía para guardar las letras que ya hemos contado
ocurrencias = []

# Recorremos cada letra de la cadena
for letra in cadena:
    # Verificamos si ya contamos esta letra antes
    if letra not in ocurrencias:
        # Creamos un contador para esta letra
        contador = 0
        # Recorremos de nuevo toda la cadena para contar cuántas veces aparece la letra
        for i in cadena:
            if i == letra:
                contador += 1  # Si encontramos la letra, sumamos 1 al contador
        # Imprimimos el resultado de cuántas veces aparece esta letra
        print(f"La letra {letra} aparece {contador} veces")
        # Agregamos la letra a la lista de letras ya contadas
        ocurrencias.append(letra)
