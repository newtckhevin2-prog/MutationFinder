from src.mutationfinder import find_mutations


def test_find_mutations():
    """
    Testea que find_mutations detecte correctamente
    mutaciones puntuales entre dos secuencias.
    """

    seq1 = "ATGCGTAC"
    seq2 = "ATGAGTAT"

    expected = [
        (4, "C", "A"),
        (8, "C", "T")
    ]

    result = find_mutations(seq1, seq2)

    assert result == expected
