# Ejercicio 1
"""  
num1 = int(input("Introduzca el primer digito: "))
num2 = int(input("Introduzca el segundo digito: "))

print(f"La multiplicacion entre {num1} y {num2} es {num1*num2}")
"""

# Ejercicio 2
"""
text = "Tengo {totalMoney} euros para comprar {quantity} tarjetas gráficas por {price:.2f} dólares."

print(text.format(totalMoney = 1000, quantity = 3, price = 450))
"""

# Ejercicio 3
"""
cadena1 = "Nombre" 
cadena2 = "Es"
cadena3 = "Ignatius"

print(cadena1, cadena2,cadena3, sep="**")
"""

# Ejercicio 4
"""
num = 8
print(f"El número octal del número decimal {num} es {oct(num)[2:]}")
"""

# Ejercicio 5
"""
num = 458.541315
print(round(num, 2))
"""

# Ejercicio 6
"""
f1 = float(input("Introduzca el primer numero flotante: "))
f2 = float(input("Introduzca el segundo numero flotante: "))
f3 = float(input("Introduzca el tercer numero flotante: "))
f4 = float(input("Introduzca el cuarto numero flotante: "))
f5 = float(input("Introduzca el quinto numero flotante: "))

print("Los numeros introducidos son :", f1 ,"-", f2,"-", f3,"-", f4,"-", f5)
"""

# Ejercicio 7
"""
nombres = input("Introduzca los nombres separados por coma: ")

aux = nombres.split(",")

print("1.-", aux[0])
print("2.-", aux[1])
print("3.-", aux[2])
"""

# Ejercicio 8
num1 = int(input("Introduzca el primer digito: "))
num2 = int(input("Introduzca el segundo digito: "))

if num1*num2 > 1000:
    print(f"El producto entre {num1} y {num2} es {num1*num2}")
else: 
    print(f"La suma entre {num1} y {num2} es {num1+num2}")
