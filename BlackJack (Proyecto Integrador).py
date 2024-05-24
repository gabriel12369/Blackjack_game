import random
cartas_completa=[]
cartas=["As","Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve","Diez","Jota","Reina","Rey"]
cartas_tipo=["Picas","Corazones","Rombos","Tréboles"]
cartas_crupier=[]
cartas_jugador=[]
cartav_c=[]
cartav_j=[]
cont_cru=0
cont_ju=0
cont_cru_com=0
cont_ju_com=0
cn="J"
print("                                      ¡BLACKJACK!\n")

#Mensaje de Bienvenida
def bienvenida():
    print("\n\"Bienvenidos a el juego de Blacjack\"\n")
    print("El juego consiste en llegar al valor de 21 con las cartas repartidas, o lo más cercano posible")
    print("sin sobrepasar esta cantidad para ganar el juego, sin embargo si no se llega a la cantidad de 21, se debe contener")
    print("un valor mayor a las del crupier para ganar eljuego.")
    print("Si el crupier contiene un número mayor que usted sin sobrepasarse de 21, usted pierde el")
    print("juego. Si el crupier llega a 21, usted perderá el juego.")
    print("\nBUENA SUERTE\n")
    
#Función para crear una carta aleatoria
def crear_carta_aleatoria(c,ct,cc):
    for i in range(0,13):
        for j in range(0,4):
            carta=c[i]+" de "+ct[j]
            cc.append(carta)
    random.shuffle(cc)
    return cc[0]

#Función para asignar un valor a la carta aleatoria extraída
def valor_cartas(c_c,c_j):
    for i in c_c:
        if i=="As de Picas" or i=="As de Corazones" or i=="As de Rombos" or i=="As de Tréboles":
            cartav_c.append(1)
        elif i=="Dos de Picas" or i=="Dos de Corazones" or i=="Dos de Rombos" or i=="Dos de Tréboles":
            cartav_c.append(2)
        elif i=="Tres de Picas" or i=="Tres de Corazones" or i=="Tres de Rombos" or i=="Tres de Tréboles":
            cartav_c.append(3)
        elif i=="Cuatro de Picas" or i=="Cuatro de Corazones" or i=="Cuatro de Rombos" or i=="Cuatro de Tréboles":
            cartav_c.append(4)
        elif i=="Cinco de Picas" or i=="Cinco de Corazones" or i=="Cinco de Rombos" or i=="Cinco de Tréboles":
            cartav_c.append(5)
        elif i=="Seis de Picas" or i=="Seis de Corazones" or i=="Seis de Rombos" or i=="Seis de Tréboles":
            cartav_c.append(6)
        elif i=="Siete de Picas" or i=="Siete de Corazones" or i=="Siete de Rombos" or i=="Siete de Tréboles":
            cartav_c.append(7)
        elif i=="Ocho de Picas" or i=="Ocho de Corazones" or i=="Ocho de Rombos" or i=="Ocho de Tréboles":
            cartav_c.append(8)
        elif i=="Nueve de Picas" or i=="Nueve de Corazones" or i=="Nueve de Rombos" or i=="Nueve de Tréboles":
            cartav_c.append(9)
        elif i=="Diez de Picas" or i=="Diez de Corazones" or i=="Diez de Rombos" or i=="Diez de Tréboles" or i=="Jota de Picas" or i=="Jota de Corazones" or i=="Jota de Rombos" or i=="Jota de Tréboles" or i=="Reina de Picas" or i=="Reina de Corazones" or i=="Reina de Rombos" or i=="Reina de Tréboles" or i=="Rey de Picas" or i=="Rey de Corazones" or i=="Rey de Rombos" or i=="Rey de Tréboles":
            cartav_c.append(10)
    for i in c_j:
        if i=="As de Picas" or i=="As de Corazones" or i=="As de Rombos" or i=="As de Tréboles":
            cartav_j.append(1)
        elif i=="Dos de Picas" or i=="Dos de Corazones" or i=="Dos de Rombos" or i=="Dos de Tréboles":
            cartav_j.append(2)
        elif i=="Tres de Picas" or i=="Tres de Corazones" or i=="Tres de Rombos" or i=="Tres de Tréboles":
            cartav_j.append(3)
        elif i=="Cuatro de Picas" or i=="Cuatro de Corazones" or i=="Cuatro de Rombos" or i=="Cuatro de Tréboles":
            cartav_j.append(4)
        elif i=="Cinco de Picas" or i=="Cinco de Corazones" or i=="Cinco de Rombos" or i=="Cinco de Tréboles":
            cartav_j.append(5)
        elif i=="Seis de Picas" or i=="Seis de Corazones" or i=="Seis de Rombos" or i=="Seis de Tréboles":
            cartav_j.append(6)
        elif i=="Siete de Picas" or i=="Siete de Corazones" or i=="Siete de Rombos" or i=="Siete de Tréboles":
            cartav_j.append(7)
        elif i=="Ocho de Picas" or i=="Ocho de Corazones" or i=="Ocho de Rombos" or i=="Ocho de Tréboles":
            cartav_j.append(8)
        elif i=="Nueve de Picas" or i=="Nueve de Corazones" or i=="Nueve de Rombos" or i=="Nueve de Tréboles":
            cartav_j.append(9)
        elif i=="Diez de Picas" or i=="Diez de Corazones" or i=="Diez de Rombos" or i=="Diez de Tréboles" or i=="Jota de Picas" or i=="Jota de Corazones" or i=="Jota de Rombos" or i=="Jota de Tréboles" or i=="Reina de Picas" or i=="Reina de Corazones" or i=="Reina de Rombos" or i=="Reina de Tréboles" or i=="Rey de Picas" or i=="Rey de Corazones" or i=="Rey de Rombos" or i=="Rey de Tréboles":
            cartav_j.append(10)
    
#Función para repartir las cartas al jugador y el crupier
def cartas_repartir():
    for i in range(2):
        while True:
            carta_c=crear_carta_aleatoria(cartas,cartas_tipo,cartas_completa)
            carta_j=crear_carta_aleatoria(cartas,cartas_tipo,cartas_completa)
            if carta_c not in cartas_crupier:
                break
        cartas_crupier.append(carta_c)
        cartas_jugador.append(carta_j)
    valor_cartas(cartas_crupier,cartas_jugador)

#Función para mostrar las cartas repartidas del jugador y del crupier
def mostrar_repartir():
    c_jugador=0
    c_crupier=0
    print("Crupier muestra: ")
    print("-",cartas_crupier[0])
    for i in range(len(cartav_c)):
        if cartav_c[i]==1 and sum(cartav_c)<=11:
            cartav_c[i]=11
    print("\nSus cartas: ")
    for i in cartas_jugador:
        print("-",i)
    for i in range(len(cartav_j)):
        if cartav_j[i]==1:
            while True:
                eleccion=input("Elija el valor de preferencia para su As (1 o 11): ")
                if eleccion =="1" or eleccion=="11":
                    break
                else:
                    print("Elija una opción válida")
            cartav_j[i]=int(eleccion)
                
    print("Total:",sum(cartav_j))
    #Si cuando se reparten las cartas se logra blackjack muestra el siguiente mensaje
    if sum(cartav_j)==21:
        print("\n¡¡¡¡¡FELICIDADES HAS GANADO!!!!!\n")

    if sum(cartav_c)==21:
        print("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")

#Decisiones para seleccionar un ganador    
def ganador(cartv_c,cartv_j):
    cont_jugador=0
    cont_crupier=0
    if sum(cartv_c)>21 and sum(cartv_j)<21:
        mensaje=("\n¡¡¡¡¡FELICIDADES HAS GANADO!!!!!\n")
        cont_crupier+=0
        cont_jugador+=1
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)<sum(cartv_j) and sum(cartv_j)<21:
        mensaje=("\n¡¡¡¡¡FELICIDADES HAS GANADO!!!!!\n")
        cont_crupier+=0
        cont_jugador+=1
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_j)==21:
        mensaje=("\n¡¡¡¡¡FELICIDADES HAS GANADO!!!!!\n")
        cont_crupier+=0
        cont_jugador+=1
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)<21 and sum(cartv_j)>21:
        mensaje=("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")
        cont_crupier+=1
        cont_jugador+=0
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)>sum(cartv_j) and sum(cartv_c)<21:
        mensaje=("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")
        cont_crupier+=1
        cont_jugador+=0
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)==21:
        mensaje=("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")
        cont_crupier+=1
        cont_jugador+=0
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)>21 and sum(cartv_j)>21:
        mensaje=("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")
        cont_crupier+=1
        cont_jugador+=0
        control=1
        return mensaje,cont_crupier,cont_jugador,control
    elif sum(cartv_c)==sum(cartv_j):
        mensaje=("\n¡¡¡¡¡EL CRUPIER HA GANADO!!!!!\n")
        cont_crupier+=1
        cont_jugador+=0
        control=1
        return mensaje,cont_crupier,cont_jugador,control
   
#Inicia el main del programa         
bienvenida()
#Si el usuario presiona salir se deja de ejecutar el programa
while cn!="S":
    print("Rondas Ganadas")
    print("Jugador:",cont_ju_com,"       Crupier:",cont_cru_com,"\n")
    contr=0
    cartas_crupier=[]
    cartas_jugador=[]
    cartav_c=[]
    cartav_j=[]
    cartas_repartir()
    mostrar_repartir()
    if sum(cartav_j)==21:
        cont_ju_com+=1
        contr=1
    if sum(cartav_c)==21:
        cont_cru_com+=1
        contr=1
    while contr==0:
        #Si el crupier tiene un total de cartas igual o menor a 16 el crupier esta obligado a tomarotra carta
        if sum(cartav_c)<=16:
            carta_c=crear_carta_aleatoria(cartas,cartas_tipo,cartas_completa)
            cartas_crupier.append(carta_c)
            cartav_c=[]
            cartav_j=[]
            valor_cartas(cartas_crupier,cartas_jugador)
            for i in range(len(cartav_j)):
                if cartav_j[i]==1:
                    cartav_j[i]=11
            for i in range(len(cartav_c)):
                if cartav_c[i]==1 and sum(cartav_c)<=11:
                    cartav_c[i]=11
        #Opciones que tiene el usuario en el juego
        op=input("\nPlantarse (P) Pedir Carta (C) Salir (S): ")
        #Opción de quedarse
        if op.upper()=="P":
            print("\nCartas del Crupier: ")
            for i in cartas_crupier:
                print("-",i)
            print("Total:",sum(cartav_c))
            print("\nSus cartas: ")
            for i in cartas_jugador:
                print("-",i)
            print("Total:",sum(cartav_j))
            men,cont_cru,cont_ju,contr=ganador(cartav_c,cartav_j)
            if cont_ju>0:
                cont_ju_com+=cont_ju
            if cont_cru>0:
                cont_cru_com+=cont_cru
            print(men)
         #Opción de pedir otra carta   
        elif op.upper()=="C":
            carta_j=crear_carta_aleatoria(cartas,cartas_tipo,cartas_completa)
            cartas_jugador.append(carta_j)
            cartav_c=[]
            cartav_j=[]
            valor_cartas(cartas_crupier,cartas_jugador)
            for i in range(len(cartav_c)):
                if cartav_c[i]==1 and sum(cartav_c)<=11:
                    cartav_c[i]=11
            print("Cartas del Crupier: ")
            print("-",cartas_crupier[0])
            print("\nSus cartas: ")
            for i in cartas_jugador:
                print("-",i)
            for i in range(len(cartav_j)):
                if cartav_j[i]==1:
                    while True:
                        elec=input("Elija el valor de preferencia para su As (1 o 11): ")
                        if elec =="1" or elec=="11":
                            break
                        else:
                            print("Elija una opción válida")
                    cartav_j[i]=int(elec)
            print("Total:",sum(cartav_j))
            if sum(cartav_j)>21:
                men,cont_cru,cont_ju,contr=ganador(cartav_c,cartav_j)
                if cont_ju>0:
                    cont_ju_com+=cont_ju
                else:
                    cont_cru_com+=cont_cru
                print(men)
        #Opción de salir del juego     
        elif op.upper()=="S":
            cn="S"
            break
        
        else:
            print("Ingrese una opción válida")
        