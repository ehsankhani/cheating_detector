import random

def mutate_dna_with_map(dna_sequence, mutation_rate=0.01):
    nucleotides = ['A', 'T', 'C', 'G']
    mutated_sequence = list(dna_sequence)
    mutation_map = []
    
    for i in range(len(mutated_sequence)):
        if random.random() < mutation_rate:
            old_base = mutated_sequence[i]
            new_base = random.choice(nucleotides)
            mutated_sequence[i] = new_base
            mutation_map.append((i, old_base, new_base))
    
    return ''.join(mutated_sequence), mutation_map

def main():
    dna_sequence = "ATGCTAGCTAGT"
    mutated_sequence, mutation_map = mutate_dna_with_map(dna_sequence, mutation_rate=0.05)
    print("Original DNA sequence:", dna_sequence)
    print("Mutated DNA sequence:", mutated_sequence)
    print("Mutation map:", mutation_map)

if __name__ == "__main__":
    main()
