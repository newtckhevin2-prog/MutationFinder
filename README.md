## 🧬 MutationFinder

MutationFinder es una librería en Python para identificar mutaciones puntuales (SNPs) entre dos secuencias de ADN en formato FASTA.
Está diseñada para ser simple, reproducible y extensible, con un enfoque educativo en Bioinformática y Biología Computacional.

Este proyecto forma parte del curso BIO210B – Biología Computacional, y tiene como objetivo presentar una herramienta funcional capaz de:

✔ Cargar secuencias en formato FASTA
✔ Comparar las secuencias base a base
✔ Detectar diferencias en la secuencia (A, T, C, G)
✔ Generar una tabla de mutaciones con posición y tipo
✔ Exportar resultados
✔ Asegurar reproducibilidad mediante pruebas automatizadas

## 📌 Motivación del proyecto

Las mutaciones en secuencias génicas permiten estudiar, entre otros aspectos:

✔ Variación genética entre individuos
✔ Evolución molecular
✔ Posibles efectos fenotípicos de un SNP
✔ Análisis de secuencias experimentales
✔ Control de calidad en secuenciación

Este programa funciona como una herramienta inicial para detectar mutaciones y como base para proyectos más complejos en Bioinformática.

## 📁 Estructura del repositorio

MutationFinder/
│── data/
│   ├── input/      # Archivos FASTA de ejemplo
│   └── output/     # Resultados generados
│
│── docs/
│   └── InformeProyecto.docx
│
│── notebooks/
│   └── Proyecto Final.ipynb
│
│── src/
│   ├── mutationfinder.py
│   └── __init__.py
│
│── tests/
│   ├── test_load_fasta.py
│   ├── test_find_mutations.py
│   └── __init__.py
│
│── README.md
│── requirements.txt


Esta estructura permite:

✔ Reproducibilidad
✔ Organización clara
✔ Testing automatizado
✔ Separación de código, datos y documentación

## ⚙️ Instalación y requisitos
🔹 Requisitos mínimos

✔ Python 3.10 o superior
✔ pytest para testing (recomendado)

🔹 Instalar dependencias
✔ pip install -r requirements.txt (si es que aplica)

## ▶️ Ejecución del programa

Ejecutar MutationFinder desde la terminal:

python src/mutationfinder.py


Esto abrirá un menú donde se podrá:

✔ Ingresar dos archivos .fasta
✔ Comparar las secuencias
✔ Visualizar las mutaciones detectadas
✔ Exportar los resultados a un archivo de salida (TXT y/o CSV)

## 🧪 Testing automatizado

Este proyecto incluye pruebas unitarias usando pytest.

Ejecutarlas:

pytest


Ejemplo de salida:

================== test session starts ==================
collected 2 items

tests/test_load_fasta.py ...                       ✓
tests/test_find_mutations.py ...                   ✓

=================== 2 passed in 0.05s ===================

## 🧾 Ejemplo de uso
Secuencia A
ATGCGTAC

Secuencia B
ATGAGTAT

Resultado esperado
Posición	Ref	Alt
4	C	A
7	A	T

Esto indica que existen dos mutaciones puntuales entre ambas secuencias. Se ejemplificia mediante un diagrama simple:

FASTA1 -----
            \
             --> find_mutations --> result list --> export TXT/CSV
            /
FASTA2 -----


## 📌 Resultados y exportación

Los resultados se almacenan automáticamente en:

data/output/


El archivo generado contiene:

✔ posición de la mutación
✔ base original
✔ base mutada

## 👤 Autor

Proyecto desarrollado por:
Khevin Olivares
BIO210B – Biología Computacional
Pontificia Universidad Católica de Chile

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT, permitiendo su uso, modificación y distribución con fines educativos y académicos.
