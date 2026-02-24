import numpy as np
import os

# PATH FILE
FILE_PATH1 = r"dataset/random1d.csv"
FILE_PATH2 = r"dataset/random2d.csv"

# FUNZIONI FILE 
def w_file(filepath, data):
    with open(filepath, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

def r_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return data

def u_file(filepath, data):
    with open(filepath, 'a') as f:
        for item in data:
            f.write(f"{item}\n")

# Creazioni file iniziali
os.makedirs("dataset", exist_ok=True)

random_numbers = np.random.rand(100)
w_file(FILE_PATH1, random_numbers)

random_2d = np.random.rand(20, 4)
w_file(FILE_PATH2, random_2d)

# Conversione dati letti in array
def convert_to_array(data_lines):
    # Se contiene più valori per riga → 2D
    if "[" in data_lines[0]:
        matrix = []
        for row in data_lines:
            clean_row = row.replace("[", "").replace("]", "")
            numbers = [float(x) for x in clean_row.split()]
            matrix.append(numbers)
        return np.array(matrix)
    else:
        return np.array([float(x) for x in data_lines])

# analisi matrice 1D
def analyze_1D(arr):
    #funzione che fa analisi statistiche su array 1D e li salva in un dizionario
    results = {}

    print("\nAnalisi disponibili per array 1D:")
    print("1 - Statistiche di base")
    print("2 - Analisi posizionale")
    print("3 - Tutte")

    choice = input("Scelta: ")

    # analisi statistiche
    if choice in ["1", "3"]:
        results["min"] = np.min(arr)
        results["max"] = np.max(arr)
        results["media"] = np.mean(arr)
        results["deviazione_std"] = np.std(arr)

    # analisi posizionali
    if choice in ["2", "3"]:
        results["indice_min"] = np.argmin(arr)
        results["indice_max"] = np.argmax(arr)
        results["mediana"] = np.percentile(arr, 50)
        x = float(input("Valore per searchsorted: "))
        results["posizione_inserimento"] = np.searchsorted(np.sort(arr), x)

    return results


# ANALISI 2D
def analyze_2D(matrix):
    results = {}
    
    print("Analisi disponibili per array 2D:")
    print("1. Analisi per assi (somme, medie")
    print("2. Operazioni matriciali e algebriche")
    print("3. Tutte le analisi")

    choice = input("Scelta: ")

    if choice in ["1", "3"]:
        results["somma_colonne"] = np.sum(matrix, axis=0)
        results["somma_righe"] = np.sum(matrix, axis=1)
        results["media_colonne"] = np.mean(matrix, axis=0)
        results["media_righe"] = np.mean(matrix, axis=1)
    
    if choice in ["2", "3"]:
        results["prodotto_dot"] = np.dot(matrix, np.transpose(matrix))
        results["trasposta"] = np.transpose(matrix)
        results["norma"] = np.linalg.norm(matrix)
        results["covarianza"] = np.cov(matrix.T)
    
    return results

# MAIN 
while True:
    filepath = input("\nInserisci path file (es: dataset/random1d.csv): ")

    if not os.path.exists(filepath):
        print("File non trovato.")
        continue

    data_lines = r_file(filepath)
    data = convert_to_array(data_lines)

    print(f"Array rilevato: {data.ndim}D")

    if data.ndim == 1:
        results = analyze_1D(data)
    else:
        results = analyze_2D(data)

    print("\nRisultati:")
    for k, v in results.items():
        print(k, ":\n", v)

    output_path = input("\nInserisci nome file output (es: dataset/output.txt): ")

    formatted_results = [f"{k}: {v}" for k, v in results.items()]
    w_file(output_path, formatted_results)

    repeat = input("\nVuoi ripetere? (s/n): ")
    if repeat.lower() != "s":
        break