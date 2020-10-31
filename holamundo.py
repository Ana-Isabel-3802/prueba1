import random
print "Hello word 3.0"
def juego():
    nuevoJuego ='S'
    while (nuevoJuego == 'S' or nuevoJuego == 's'
    or nuevoJuego == 'SI' or nuevoJuego == 'sI' or
    nuevoJuego == 'Si' or nuevoJuego == 'si'):
        print "Pienso en un numero del 1 al 20"
        print "Tienes 5 intentos"
        num=int(input("En que numero pienso: "))
        a= random.randint(1, 20)
        a=int(a)
        acierto=False
        for resp in range (1, 6):
            if a < num:
                print "El numero es menor"
                num= int(input("Dime el numero en el que pienso: "))
            elif a> num:
                print "El numero es mayor"
                num= int(input("Dime el numero en el que pienso: "))
            elif a== num:
                
                resp = 6
                acierto=True
        if acierto==False:
            print "Ya no tienes intentos, has perdido el juego :("
        else:
            print "Felicidades acertaste :D"
        nuevoJuego= raw_input("desea jugar de nuevo? S/N")
         
