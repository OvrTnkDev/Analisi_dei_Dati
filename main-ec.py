import numpy as np

def analyze_1D(arr):
    results = {}

    print("\nAnalisi disponibili per array 1D:")
    print("1 - Statistiche di base")
    print("2 - Analisi posizionale")
    print("3 - Tutte")

    choice = input("Scelta: ")

    if choice in ["1", "3"]:
        results["min"] = np.min(arr)
        results["max"] = np.max(arr)
        results["media"] = np.mean(arr)
        results["deviazione_std"] = np.std(arr)

    if choice in ["2", "3"]:
        results["indice_min"] = np.argmin(arr)
        results["indice_max"] = np.argmax(arr)
        results["mediana"] = np.percentile(arr, 50)
        x = float(input("Valore per searchsorted: "))
        results["posizione_inserimento"] = np.searchsorted(np.sort(arr), x)

    return results



