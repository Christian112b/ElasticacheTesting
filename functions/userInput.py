def userInput(inputString, inputOption):
    try:
        print(f"{inputString}")
        for i in range(len(inputOption)):
            print(f"{i} - {inputOption[i]}")

        option = int(input())

        if option < 0 or option >= len(inputOption):
            print("Opción no válida, intente de nuevo.")
            return userInput(inputString, inputOption) 

        return option 

    except ValueError:
        print("Respuesta no válida. Debes ingresar un número entero.")
        return userInput(inputString, inputOption)  

