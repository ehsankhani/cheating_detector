def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

def main():
    dna_sequence = "ATGCTAGCTAGT"
    gc_percentage = gc_content(dna_sequence)
    print("DNA sequence:", dna_sequence)
    print("GC content (%):", gc_percentage)

if __name__ == "__main__":
    main()
