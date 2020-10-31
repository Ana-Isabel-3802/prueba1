def getPorcentajeArmadura(armadura):
    return armadura/(100.0+armadura)

def getArmaduraParaPorcentaje(reduccionEsperada):
    return (reduccionEsperada/(1.0-(reduccionEsperada/100.0)))

def getCantidadAtaques(vida, armadura, ataqueEnemigo):
    return vida/(ataqueEnemigo*(1.0-(getPorcentajeArmadura(armadura))))

def menuCalculadora():
    opcionSeleccionada=1
    while opcionSeleccionada!=0:
        print "Bienvenido a la calculadora de league of legends"
        print "Seleccione la operacion a realizar\n"
        print "0) Salir de la aplicacion"
        print "1) Calcular porcentaje de reduccion de dano con armadura"
        print "2) Calcular armadura necesaria para obtener porcentaje deseado"
        print "3) Calcular numero de basicos necesarios para que te maten\n"
        opcionSeleccionada=int(input("Su seleccion: "))
        if(opcionSeleccionada==0):
            print "bye :)"
        elif(opcionSeleccionada==1):
            armadura=int(input("ingrese la cantidad de armadura: "))
            porcentajeReduccion=getPorcentajeArmadura(armadura)
            print "reduces un ",(porcentajeReduccion*100.0),"% de dano y recibes unicamente el ",int(100.0-porcentajeReduccion*100),"% del dano esperado"
        elif(opcionSeleccionada==2):
            reduccionEsperada=100
            while (reduccionEsperada<0 or reduccionEsperada>=100):
                reduccionEsperada=int(input("ingrese el porcentaje de reduccion de dano que desea tener (0-99): "))
                if (reduccionEsperada>=0 and reduccionEsperada<100):
                    print "la cantidad de armadura minima para obtener el porcentaje es: ",getArmaduraParaPorcentaje(reduccionEsperada)
                else:
                    print "si seras.. si seras.. ingresa un valor entre 0 y 99!!"
        elif(opcionSeleccionada==3):
            vida=int(input("Ingrese la vida de su campeon: "))
            armadura=int(input("Ingrese la armadura de su campeon: "))
            ataqueEnemigo=int(input("Ingrese el Attack Damage (AD) enemigo: "))
            print "el oponente necesitara realizar ",getCantidadAtaques(vida, armadura, ataqueEnemigo)," ataques basicos para matarte"
        else:
            print "la opcion seleccionada no esta entre las opciones (fijeseee)"
