import random


def dna_mutation_with_log(sequence, rate=0.01):
    bases = ['A', 'T', 'C', 'G']
    new_sequence = list(sequence)
    mutation_log = []

    for idx in range(len(new_sequence)):
        if random.random() < rate:
            original_base = new_sequence[idx]
            altered_base = random.choice(bases)
            new_sequence[idx] = altered_base
            mutation_log.append((idx, original_base, altered_base))

    return ''.join(new_sequence), mutation_log


def run_simulation():
    original_sequence = "ATGCTAGCTAGT"
    mutated_sequence, mutation_log = dna_mutation_with_log(original_sequence, rate=0.05)
    print("Original Sequence:", original_sequence)
    print("Mutated Sequence:", mutated_sequence)
    print("Mutation Log:", mutation_log)


if __name__ == "__main__":
    run_simulation()
