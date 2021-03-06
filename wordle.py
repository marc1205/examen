import random

def choose_secret(fichero):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    """llegim el fitxer de text, i guardem les paraules en una llista"""

    """fichero = "palabras_reduced.txt"""
    f = open(fichero, mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    f.close()
    """agafem una paraula random de la llista"""
    palabra = random.choice(lista_lineas)
    """transformem la paraula en majúscula"""
    palabraMajuscula = palabra.upper()
    return palabraMajuscula
    
def compare_words(word):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen 
        en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    for i in range(4):
      if word[i] == secret[i]:
        same_position = word[i]

    same_letter = []
    for i in range(4):
      for j in range(4):
        if word[i] == secret[j]:
          same_letter = word[i]
    return same_position, same_letter

def print_word(word, same_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan 
        en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra 
        que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    palabra = []
    for i in range(4):
      if word[i] == same_position[i]:
        palabra[i] = word[i].upper()
      if word[i] == same_letter[i]:
        palabra[i] = word.lower()
      else:
        palabra[i] = "-"
    return palabra


def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). 
      De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, 
      se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
 
def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """

if __name__ == "__main__":
    secret=choose_secret("palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
