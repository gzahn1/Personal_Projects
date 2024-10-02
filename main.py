from functions import *

def main():
    dna_sequence_1 = input_sequence()
    dna_sequence_2 = input_sequence()
    print()

    #get nucleotide freq for each sequence
    print("DNA sequence 1 nucleotide frequency: " + str(nucleotide_freq(dna_sequence_1)))
    print("DNA sequence 2 nucleotide frequency: " + str(nucleotide_freq(dna_sequence_2)))
    print()

    #get reverse complement for each sequence
    print("The reverse complement of DNA sequence 1 is " + str(rev_complement(dna_sequence_1)))
    print("The reverse complement of DNA sequence 2 is " + str(rev_complement(dna_sequence_2)))
    print()

    #get codons for each sequence
    print("DNA sequence 1 codons: " + str(get_codons(dna_sequence_1)))
    print("DNA sequence 2 codons: " + str(get_codons(dna_sequence_2)))
    print()

    sequence_codon_comparison(dna_sequence_1, dna_sequence_2) #compare

if __name__ == "__main__":
    main()