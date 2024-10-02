from Bio.Seq import Seq

def input_sequence(): #takes user input to form a dna sequence
    sequence = input("Enter a sequence: ").upper()
    if valid_sequence(sequence): # helper function
        return sequence
    else:
        print("Invalid sequence. Please enter only A, T, C, or G.")

def valid_sequence(sequence): #helper method checks if the user input is a valid dna sequence
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    return all(nucleotide in valid_nucleotides for nucleotide in sequence)

def nucleotide_freq(sequence): #displays the frequency of each nucleotide in the sequence
    freq = {
        'A' : sequence.count('A'),
        'T' : sequence.count('T'),
        'C' : sequence.count('C'),
        'G' : sequence.count('G'),
    }
    #print(sequence + " nucleotide frequency: " + str(freq))
    return freq

def rev_complement(sequence): #displays the reverse complement of a dna sequence
    seq_obj = Seq(sequence) #converts to Seq object to allow method calls
    reverse_complement = seq_obj.reverse_complement()
    #print("The reverse complement of " + sequence + " is " + str(reverse_complement))
    return reverse_complement

# codon func here
def get_codons(sequence): #converts the dna sequence into a list of codons
    valid_length = len(sequence) - (len(sequence) % 3) #valid codons are a length of 3, so list must be divisible by 3
    codons = [sequence[i:i+3] for i in range(0, valid_length, 3)]
   # print(sequence + " codons: " + str(codons))
    return codons


def sequence_codon_comparison(sequence1, sequence2): #various comparisons of codon list
    codons1 = get_codons(sequence1)
    codons2 = get_codons(sequence2)
    if codons1 == codons2: #checks for match
        print('Codon Sequence 1 and Codon Sequence 2 match.')
    if codons1 != codons2: #checks for index of mismatch
        min_length = min(len(codons1), len(codons2))
        for i in range(min_length):
            if codons2[i] != codons1[i]:
                print(f"Codon sequences do not match at index {i},  {codons1[i]} != {codons2[i]}")
    if len(codons1) != len(codons2): #prints to console statement on longer codon sequence
        if len(codons1) > len(codons2):
            print("Codon sequence 1 is longer than Codon Sequence 2.")
        else:
            print("Codon sequence 2 is longer than Codon Sequence 1.")


