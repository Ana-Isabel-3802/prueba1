import random
print "Hello word 3.0"
def juego():
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
