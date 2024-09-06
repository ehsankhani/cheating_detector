import random

def mutate_dna_enhanced(dna_sequence, mutation_rate=0.01):
    nucleotides = ['A', 'T', 'C', 'G']
    preferences = {
        'A': ['T', 'C'],  # A mutates more often to T or C
        'T': ['A', 'G'],  # T mutates more often to A or G
        'C': ['G', 'A'],  # C mutates more often to G or A
        'G': ['C', 'T']   # G mutates more often to C or T
    }
    mutated_sequence = list(dna_sequence)
    
    for i in range(len(mutated_sequence)):
        if random.random() < mutation_rate:
            old_base = mutated_sequence[i]
            mutated_sequence[i] = random.choice(preferences[old_base])
    
    return ''.join(mutated_sequence)

def main():
    dna_sequence = "ATGCTAGCTAGT"
    mutated_sequence = mutate_dna_enhanced(dna_sequence, mutation_rate=0.05)
    print("Original DNA sequence:", dna_sequence)
    print("Mutated DNA sequence:", mutated_sequence)

if __name__ == "__main__":
    main()
