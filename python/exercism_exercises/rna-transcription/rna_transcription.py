DNA_TO_RNA_MAPPER = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand):
    generator = (DNA_TO_RNA_MAPPER[character] for character in dna_strand)
    return "".join(generator)