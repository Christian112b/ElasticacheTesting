import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))

#Functions
from functions.userInput import userInput
from functions.browseCategories import browseCategories
from functions.getElasticacheInfo import getElasticacheInfo

if __name__ == "__main__":

    bandera = False

    while not bandera:
        inputString = "Ingrese una opcion."
        inputOption = ["Buscar Pelicula por categoria", "Informacion guardada en Elasticache","Salir"]
        inputUser = userInput(inputString, inputOption)

        if inputUser == 0:
            browseCategories()
        elif inputUser == 1:
            getElasticacheInfo()
        elif inputUser == 2:
            print("Saliendo")
            bandera = True


