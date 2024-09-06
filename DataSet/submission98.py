def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_sequence = dna_sequence[::-1]
    return ''.join(complement[base] for base in reversed_sequence)

def main():
    dna_sequence = "ATGCTAGCTAGT"
    rev_complement = reverse_complement(dna_sequence)
    print("Original DNA sequence:", dna_sequence)
    print("Reverse complement:", rev_complement)

if __name__ == "__main__":
    main()
