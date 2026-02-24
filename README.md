# Analisi dei Dati

Andare a creare un sistema che prenda in input dei file txt o csv (anche o uno o l’altro).

Deve poter eseguire una o più di tutti i tipi di analisi che sono presenti nella parte a destra, quelle coerenti col tipo di dato fornito.

Alla fine deve POTER salvare un file dello stesso tipo o di tipo TXT (anche solo uno dei due)
Deve Potersi ripetere.


EXTRA: Andare ad isolare le singole tipologie di analisi e renderle applicabili su dati di tipo non coerente


## Analisi su array monodimensionali (1D)

Statistiche di base (min, max, media, deviazione)
Su un array 1D è possibile calcolare rapidamente diversi indicatori statistici fondamentali:

- np.min(arr) → valore minimo
- np.max(arr) → valore massimo
- np.mean(arr) → media
- np.std(arr) → deviazione standard


## Analisi posizionale (ricerche, argmin, argmax, percentili)
Si possono analizzare le posizioni relative dei valori:

- np.argmin(arr) → indice del valore minimo
- np.argmax(arr) → indice del valore massimo
- np.percentile(arr, 50) → mediana
- np.searchsorted(arr, x) → trovare posizione ordinata di inserimento



# Analisi su array multidimensionali (2D o superiori)

## Analisi per assi (somme, medie, aggregazioni)
In array multi-dimensione è possibile calcolare aggregazioni lungo assi specifici:

- np.sum(matrix, axis=0) → somma per colonne
- np.sum(matrix, axis=1) → somma per righe
- np.mean(matrix, axis=0) → media colonnare
- np.mean(matrix, axis=1) → media riga per riga


# Operazioni matriciali e algebriche (dot, transpose, norme)
Gli array multidimensionali permettono analisi strutturali complesse:

- np.dot(A, B) → prodotto matriciale
- np.transpose(A) → trasposizione
- np.linalg.norm(A) → norma della matrice
- np.cov(A.T) → matrice di covarianza