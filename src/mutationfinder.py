# Paso 1: Función para cargar secuencia desde archivo FASTA

import csv

def load_fasta(file_path):
    """
    Carga un archivo FASTA y devuelve la secuencia concatenada sin headers.

    Parameters
    ----------
    file_path : str
        Ruta al archivo FASTA.

    Returns
    -------
    str
        Secuencia biológica como una cadena (A, C, G, T).
    """
    sequence = ""
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

# Paso 2: Detectar mutaciones entre dos secuencias

def find_mutations(seq1, seq2):
    """
    Compara dos secuencias y devuelve una lista de mutaciones puntuales.

    Parameters
    ----------
    seq1 : str
        Secuencia de referencia.
    seq2 : str
        Secuencia mutada.

    Returns
    -------
    list of tuples
        Lista de mutaciones en el formato:
        (posición, base original, base mutada)
        La posición se entrega en notación 1-based.
    """
    mutations = []
    min_len = min(len(seq1), len(seq2))

    for i in range(min_len):
        if seq1[i] != seq2[i]:
            mutations.append((i+1, seq1[i], seq2[i]))

    return mutations

# Paso 3: Mostrar mutaciones en formato tabla
def print_mutations_table(mutations):
    """
    Imprime las mutaciones detectadas en formato tabla.

    Parameters
    ----------
    mutations : list of tuples
        Lista de mutaciones encontradas.
    """
    if not mutations:
        print("No se encontraron mutaciones.")
        return
    
    print("\nPosición | Original | Mutada")
    print("----------------------------")
    for pos, orig, mut in mutations:
        print(f"{pos:^8} |    {orig}     |    {mut}")

#Paso 4: Exportar a un archivo TXT generado

def exportar_resultados(mutations, seq1, seq2):
    """
    Exporta los resultados completos en formato TXT.

    Parameters
    ----------
    mutations : list of tuples
        Lista de mutaciones.
    seq1 : str
        Secuencia de referencia.
    seq2 : str
        Secuencia mutada.
    """
    filename = "data/output/Reporte_MutationFinder.txt"

    with open(filename, "w") as f:
        f.write("=== REPORTE DE MUTACIONES – MutationFinder ===\n")
        f.write("Autor: Khevin Flores Olivares\n\n")

        f.write(">> Secuencia 1 (Referencia):\n")
        f.write(seq1 + "\n\n")

        f.write(">> Secuencia 2 (Mutada):\n")
        f.write(seq2 + "\n\n")

        f.write("=== RESULTADOS ===\n")
        f.write(f"Total mutaciones detectadas: {len(mutations)}\n\n")

        if not mutations:
            f.write("No se detectaron mutaciones.\n")
        else:
            f.write("Posición | Original | Mutada\n")
            f.write("--------------------------------\n")
            for pos, orig, mut in mutations:
                f.write(f"{pos:^8} |    {orig}     |    {mut}\n")

    print(f"\n✔ Archivo TXT generado: {filename}")


# Paso 5: Exportar a un archivo CSV
def exportar_csv(mutations):
    """
    Exporta las mutaciones en formato CSV (Excel/Sheets).

    Parameters
    ----------
    mutations : list of tuples
        Lista de mutaciones.
    """
    filename = "data/output/Mutaciones.csv"

    headers = ["Posición", "Original", "Mutada"]

    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for pos, orig, mut in mutations:
            writer.writerow([pos, orig, mut])

    print(f"✔ Archivo CSV generado: {filename}")


# Paso 6: Menú principal

def menu():
    """
    Muestra el menú principal del programa e interactúa con el usuario.
    """
    seq1 = None
    seq2 = None
    mutations = []

    while True:
        print("\n=== MutationFinder ===")
        print("1. Cargar secuencia 1 (FASTA)")
        print("2. Cargar secuencia 2 (FASTA)")
        print("3. Comparar secuencias")
        print("4. Mostrar mutaciones encontradas")
        print("5. Exportar resultados detallados (TXT)")
        print("6. Exportar mutaciones a CSV")
        print("7. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            path = input("Ingrese el archivo FASTA de la secuencia 1: ")
            seq1 = load_fasta(path)
            print("✔ Secuencia 1 cargada correctamente.")

        elif choice == "2":
            path = input("Ingrese el archivo FASTA de la secuencia 2: ")
            seq2 = load_fasta(path)
            print("✔ Secuencia 2 cargada correctamente.")

        elif choice == "3":
            if seq1 is None or seq2 is None:
                print("⚠ Debe cargar ambas secuencias primero.")
            else:
                mutations = find_mutations(seq1, seq2)
                print(f"\n✔ Comparación completada. Se encontraron {len(mutations)} mutaciones.")

        elif choice == "4":
            if not mutations:
                print("⚠ Primero debe comparar las secuencias (opción 3).")
            else:
                print_mutations_table(mutations)

        elif choice == "5":
            if not mutations:
                print("⚠ Primero debe comparar las secuencias (opción 3).")
            else:
                exportar_resultados(mutations, seq1, seq2)

        elif choice == "6":
            if not mutations:
                print("⚠ Primero debe comparar las secuencias (opción 3).")
            else:
                exportar_csv(mutations)

        elif choice == "7":
            print("\n👋 Saliendo del programa...")
            break

        else:
            print("⚠ Opción inválida. Intente nuevamente.")


# Paso 7: Ejecución del programa

if __name__ == "__main__":
    print("=== MutationFinder listo para trabajar ===")
    menu()



