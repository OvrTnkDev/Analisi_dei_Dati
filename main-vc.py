'''
Andare a creare un sistema che prenda in input dei file txt o csv (anche o uno o l'altro).
Deve poter eseguire una o più di tutti i tipi di analisi che sono presenti nella parte a destra,
quelle coerenti col tipo di dato fornito.
Alla fine deve POTER salvare un file dello stesso tipo o di tipo TXT (anche solo uno dei due)
Deve Potersi ripetere.
Extra: Andare ad isolare le singole tipologie di analisi e renderle applicabili su dati
di tipo non coerente.

Analisi su array monodimensionali (1D)
- Statistiche di base (min, max, media, deviazione)
Su un array 1D è possibile calcolare rapidamente diversi indicatori statistici fondamentali:
- np.min(arr): valore minimo
- np.max(arr): valore massimo
- np.mean(arr): media
- np.std(arr): deviazione standard

- Analisi posizionale (ricerche, argmin, argmax, percentili)
Si possono analizzare le posizioni relative dei valori:
- np.argmin(arr): indice del valore minimo
- np.argmax(arr): indice del valore massimo
- np.percentile(arr, 50): mediana
- np.searchsorted(arr, x): trovare posizione ordinata di inserimento

Analisi su array multidimensionali (2D o superiori)
- Analisi per assi (somme, medie, aggregazioni

In array multi-dimensione è possibile calcolare aggregazioni lungo assi specifici:
- np.sum(matrix, axis=0): somma per colonne
- np.sum(matrix, axis=1): somma per righe
- np.mean(matrix, axis=0): media colonnare
- np.mean(matrix, axis=1): media riga per riga

- Operazioni matriciali e albebriche (dot, transpose, norme)
Gli array multidimensionali permettono analisi strutturali complesse:
- np.dot(A, B): prodotto matriaciale
- np.transpose(A): trasposizione
- np.linalg.norm(A): norma della matrice
- np.cov(A.T): matrice di covarianza.
'''

import numpy as np

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