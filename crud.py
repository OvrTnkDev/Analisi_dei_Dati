import numpy as np

#creazione dei path dei file
FILE_PATH1 = r"dataset/random1d.csv"
FILE_PATH2 = r"dataset/random2d.csv"

#creazione del file
def w_file(filepath, data):
    with open(filepath, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
            
#lettura del file
def r_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return data

#aggiornamento del file
def u_file(filepath, data):
    with open(filepath, 'a') as f:
        for item in data:
            f.write(f"{item}\n")


#creazione dei due file iniziali
#creazione del primo file con 100 numeri casuali
random_numbers = np.random.rand(100)
w_file(FILE_PATH1, random_numbers)

#creazione 2d con 20 righe e 4 colonne
random_2d = np.random.rand(20, 4)
w_file(FILE_PATH2, random_2d)