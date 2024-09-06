import random

def mutate_dna_sequence(dna_seq, mutation_prob=0.02):
    bases = ['A', 'T', 'C', 'G']
    sequence = list(dna_seq)
    
    for i in range(len(sequence)):
        if random.random() < mutation_prob:
            sequence[i] = random.choice(bases)
    
    return ''.join(sequence)

def main():
    dna_seq = "ATGCTAGCTAGT"
    mutated_seq = mutate_dna_sequence(dna_seq, mutation_prob=0.05)
    print("Original DNA sequence:", dna_seq)
    print("Mutated DNA sequence:", mutated_seq)

if __name__ == "__main__":
    main()
