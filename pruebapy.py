import holamundo as h
import calculadoraLol as lol
#print "Hello cold word"
#cadena=raw_input("escribe algo para acabar ahora si el programa: ")
#entero=int(input("Escrbe un entero: "))
#decimal=float(input("Escrbe un decimal: "))
#print cadena
#print entero
#print decimal

#if entero <= 10:
 #   print "este numero solo tiene un digito"
#else:
#    print "este numero tiene mas de un digito"

#print "Pienso en un numero del 1 al 20"
#print "Tienes 5 intentos"
print "seleccione la aplicacion: "
print "1) adivina el numero"
print "2) calculadora de League of legends\n"
print "cualquier otro numero) salir"
applicacionSeleccionada=int(input("su seleccion: "))
if (applicacionSeleccionada==1):
    h.juego()
elif(applicacionSeleccionada==2):
    lol.menuCalculadora()
