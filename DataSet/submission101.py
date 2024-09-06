import random

def mutate_dna(dna_sequence, mutation_rate=0.01):
    nucleotides = ['A', 'T', 'C', 'G']
    mutated_sequence = list(dna_sequence)
    
    for i in range(len(mutated_sequence)):
        if random.random() < mutation_rate:
            mutated_sequence[i] = random.choice(nucleotides)
    
    return ''.join(mutated_sequence)

def main():
    dna_sequence = "ATGCTAGCTAGT"
    mutated_sequence = mutate_dna(dna_sequence, mutation_rate=0.05)
    print("Original DNA sequence:", dna_sequence)
    print("Mutated DNA sequence:", mutated_sequence)

if __name__ == "__main__":
    main()
