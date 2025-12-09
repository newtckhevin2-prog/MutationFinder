import os
from src.mutationfinder import load_fasta


def test_load_fasta(tmp_path):
    """
    Testea que load_fasta cargue correctamente
    una secuencia FASTA y ignore el header.
    """

    # Crear archivo FASTA temporal
    fasta_content = ">seq1\nATGCGTAC\n"
    file_path = tmp_path / "test.fasta"

    with open(file_path, "w") as f:
        f.write(fasta_content)

    # Ejecutar función
    seq = load_fasta(str(file_path))

    # Validar resultado
    assert seq == "ATGCGTAC"
