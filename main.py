import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))

#Functions
from functions.userInput import userInput
from functions.browseCategories import browseCategories

if __name__ == "__main__":

    inputString = "Ingrese una opcion."
    inputOption = ["Buscar Pelicula por categoria"]
    input = userInput(inputString, inputOption)

    if input == 0:
        consultarCategorias()
