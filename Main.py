#!/usr/bin/env python
# -*- coding: utf-8 -*-

########
########
#Imports
########
########

from Carta import Carta
from random import randint
import time

########################
########################
#Definición de funciones
########################
########################


###################################################
#Función para repartir una carta aleatoria del mazo
###################################################

def repartir_carta(turno, mazo, cartas):
	num_carta = randint(0,len(mazo))
	carta = mazo[num_carta]
	actualizar_mazo(num_carta, mazo)
	actualizar_mano(carta, turno, cartas)
	print("Cartas repartidas:")
	for carta in cartas:
		print ("[" + carta.getTipo() + " " + carta.getPalo() + "]\n")
		time.sleep(1) # delays for 1 seconds
	
##################################################
#Función para eliminar la carta repartida del mazo
##################################################

def actualizar_mazo(num_carta, mazo):
	mazo.pop(num_carta)

###########################################################
#Función para actualizar el valor de las cartas del jugador
###########################################################

def actualizar_mano(carta, turno, cartas):
	if(turno == "Jugador"):
		cartas_jugador.append(carta)	
	else:
		cartas_banca.append(carta)	
			

#########################################################
#Comprobar si el jugador puede seguir jugando o se ha superado 21
#########################################################

def comprobar_cartas(cartas):
	
	puntos = 0
	num_ases = 0

	#Contar los puntos
	for carta in cartas:
		if (carta.getValor() == -1):
			num_ases = num_ases + 1
		else:
			puntos = puntos + carta.getValor()
	#Sólo puede haber un as que valga 11
	if(num_ases == 0):
		print("El valor total de las cartas es de: " + str(puntos))
		return puntos
	elif(num_ases == 1):
		#Si una de las dos sumas es viable
		if((puntos + 11 <= 21) or (puntos + 1 <= 21)):
			if(max(puntos + 11, puntos + 1) <= 21):
				print("El valor total de las cartas es de: " + str(max(puntos + 11, puntos + 1)))
				return max(puntos + 11, puntos + 1)	
			else:
				print("El valor total de las cartas es de: " + str(min(puntos + 11, puntos + 1)))
				return min(puntos + 11, puntos + 1)
		else:
			print("El valor total de las cartas es superior a 21")
			return puntos + 1
	else:
		puntos_max = puntos + 11
		i = 1
		while(i < num_ases):
			puntos_max = puntos_max + 1	
		puntos_min = puntos
		i=0
		while(i < num_ases):
			puntos_min = puntos_min + 1
		#Si una de las dos sumas es viable
		if((puntos_max <= 21) or (puntos_min <= 21)):
			if(puntos_max <= 21):
				print("El valor total de las cartas es de: " + str(puntos_max))
				return puntos_max
			else:
				print("El valor total de las cartas es de: " + str(puntos_min))
				return puntos_min
		else:
			print("El valor total de las cartas es superior a 21")
			return puntos_min				
			
#Actualizar el valor de un as en las cartas del 	
def actualizar_as(pos_as, cartas, valor_as):

	cartas[pos_as].setValor(valor_as)
		

#Función para actualizar la puntuación total del jugador
#def actualizar_puntuacion():

################################################
#Función para juntar todas las cartas en el mazo
################################################

def juntar_mazo():
	
	del mazo[:]
	return crear_mazo()

#############################################################
#Función que devuelve una lista con todas las cartas del mazo
#############################################################

def crear_mazo():
	
	cont_carta = 1
	cont_palo = 1
	tipos = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K" }
	palos = {1: "Treboles", 2: "Picas", 3: "Corazones", 4: "Diamantes"}
	mazo = []
	
	#Ases
	while (cont_palo <= 4):	
		carta = Carta(tipos[cont_carta], palos[cont_palo], -1)
		mazo.append(carta)
		cont_palo = cont_palo + 1
	
	cont_carta = 2
	cont_palo = 1
	
	#Cartas del 2 al 10
	while (cont_carta <= 10):
		while (cont_palo <= 4):
			carta = Carta(tipos[cont_carta], palos[cont_palo], cont_carta)
			mazo.append(carta)
			cont_palo = cont_palo + 1
		cont_carta = cont_carta + 1
		cont_palo = 1
	
	cont_carta = 11
	cont_palo = 1	
	
	#Figuras
	while (cont_carta <= 13):
		while (cont_palo <= 4):	
			carta = Carta(tipos[cont_carta], palos[cont_palo], 10)
			mazo.append(carta)
			cont_palo = cont_palo + 1
		cont_carta = cont_carta + 1	
		cont_palo = 1
	return mazo				

#######################
#######################	
#Variables y constantes
#######################
#######################

mazo = crear_mazo() #Mazo del que se extraen cartas

cartas_jugador = [] #Cartas que va sacando el jugador

cartas_banca = [] #Cartas que va sacando la banca

puntos_jugador = 0

puntos_banca = 0

hay_juego = True

juego_banca = True

opciones = ['S', 's', 'N', 'n']

continuar = "a"

######
######	
#Juego
######
######
print ("──────▄▀▄─────▄▀▄")
print ("─────▄█░░▀▀▀▀▀░░█▄")
print ("─▄▄──█░░░░░░░░░░░█──▄▄")
print ("█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")

print ("###################################")

print ("BIENVENIDO AL JUEGO BLACKJACK! ♠ ♣ ♥ ♦")

print ("Crédito: https://bitbucket.org/karatekat/")

print ("###################################")

raw_input ("Pulsa enter para empezar a jugar:")

print ("Repartiendo carta...")
time.sleep(1) # delays for 1 seconds

while(hay_juego):

	repartir_carta("Jugador", mazo, cartas_jugador)
		
	puntos_jugador = comprobar_cartas(cartas_jugador)	
	if(puntos_jugador <= 21):
	
		while(continuar not in opciones):
			continuar = raw_input ("¿Quieres continuar? (S/N): ")
			
		if((continuar == "N") or (continuar == "n")):
			print("Te has plantado.")
			time.sleep(1) # delays for 1 seconds
			hay_juego = False
			
		continuar = "a"			
	else:
		print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
		print ("Resultado final")
		print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
		print ("Has perdido :(")
		print ("Tú: " + str(puntos_jugador))
		print ("Banca: " + str(puntos_banca))
		exit()
print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
print ("TURNO DE LA BANCA")
print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
time.sleep(1) # delays for 1 seconds
while(juego_banca):
	repartir_carta("Banca", mazo, cartas_banca)
	puntos_banca = comprobar_cartas(cartas_banca)
	if(puntos_banca <= 21):
		if(puntos_banca >= 17):
			juego_banca = False
		else:
			raw_input ("Pulsa enter para cotinuar:")
			print("Repartiendo otra carta...")
			time.sleep(1) # delays for 1 seconds
	else:
		juego_banca = False
		print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
		print ("RESULTADO FINAL")
		print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
		print ("Has ganado!!! :)")
		print ("Tú: " + str(puntos_jugador))
		print ("Banca: " + str(puntos_banca))
		exit()
print("La banca ha terminado")

if((puntos_jugador <= 21) and (puntos_banca <= 21)):
	print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
	print ("RESULTADO FINAL")
	print ("♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦ ♠ ♣ ♥ ♦")
	if(puntos_jugador >= puntos_banca):
		print ("Has ganado!!! :)")
		print ("Tú: " + str(puntos_jugador))
		print ("Banca: " + str(puntos_banca))
	else:
		print ("Has perdido :(")
		print ("Tú: " + str(puntos_jugador))
		print ("Banca: " + str(puntos_banca))
exit()






