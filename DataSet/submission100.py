def rna_to_protein(rna_sequence):
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
        'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
        'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T',
        'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A',
        'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C',
        'UGC': 'C', 'UGG': 'W', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N',
        'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'UGA': 'Stop', 'UAA': 'Stop', 'UAG': 'Stop'
    }
    
    protein_sequence = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        protein_sequence += codon_table.get(codon, '')
    return protein_sequence

def main():
    rna_sequence = "AUGUUUCUAUAG"
    protein = rna_to_protein(rna_sequence)
    print("Original RNA sequence:", rna_sequence)
    print("Translated protein sequence:", protein)

if __name__ == "__main__":
    main()
