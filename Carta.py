#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Clase Carta

class Carta:
	
	#Constructor clase Carta formada por los atributos tipo, palo y valor
	def __init__(self, tipo, palo, valor):
		
		self.tipo = tipo #K, Q, J, 10, ... , 1
		self.palo = palo #Picas, tréboles, corazones, diamantes
		self.valor = valor #10, 9, ... , 2, -1
		
	#Getters y Setters
		
	def getTipo(self):
		return self.tipo
		
	def getPalo(self):
		return self.palo
		
	def getValor(self):
		return self.valor
	
	def setTipo(self, tipo):
		self.tipo = tipo
		
	def setPalo(self, palo):
		self.palo = palo
		
	def setValor(self, valor):
		self.valor = int (valor)