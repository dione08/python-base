#!/usr/bin/env python3
"""
Comentários multlinhas do Python
Considerado a documentação do seu programa
Python considera esse conteúdo como comentário
"""
#Dunder
__version__ = "0.0.1"
__author__ = "Dione Ribeiro"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"


# Aqui aplicamos a condicional

if current_language == "pt_BR":
	msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
	msg = "Bonjour, Monde!"

print(msg)