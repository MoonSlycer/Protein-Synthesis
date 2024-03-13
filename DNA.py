#this function returns a list of codons or anticodons of a string input
def StringToCodonList(string):
    x = [string[i:i+3] for i in range(0, len(string), 3)]
    return x
#this function returns the complementary string of a string input
def Complement(string):
    xList = []
    for i in string:
        if i == "A":
            xList.append("U")
        if i == "T":
            xList.append("A")
        if i == "U":
            xList.append("A")
        if i == "G":
            xList.append("C")
        if i == "C":
            xList.append("G")
    xString = ""
    for i in xList:
        xString += i
    return StringToCodonList(xString)
#converts list mRNA to list corresponding Amino Acids
def Translate(mRnaList):
    codonChart = {
        'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }
    aminoAcids = []
    for codon in mRnaList:
        aminoAcids.append(codonChart.get(codon, 'Unknown'))
    return aminoAcids
def ListToString(xList):
    return (" ".join(xList))
def ProteinSynthesis():
    inputDna = input("DNA:         ")
    mRna = Complement(inputDna)
    print("mRNA:        " + ListToString(mRna))
    tRna = Complement(ListToString(mRna))
    print("tRNA:        " + ListToString(tRna))
    aminoAcids = Translate(mRna)
    print("Amino Acids: " + ListToString(aminoAcids))
    choice = input("press enter to restart or type 'learn' to do it yourself! ")
    if choice == "learn" or choice == "Learn":
        print("---------------------------------")
        print("Transcription: Converts DNA to mRNA.")
        print("     1) change every Thymine to an Adenine.")
        print("     2) change every Adenine to a Uracil.")
        print("     3) change every Guanine to a Cytosine.")
        print("     4) change every Cytosine to a Guanine.")
        print("Translation: Converts mRNA to Proteins.")
        print("     To find a tRNA's anticodon that corresponds to an mRNA's codon:")
        print("          1) change every Uracil to an Adenine.")
        print("          2) change every Adenine to a Uracil.")
        print("          3) change every Guanine to a Cytosine.")
        print("          4) change every Cytosine to a Guanine.")
        print("     Once you find the tRNA's anticodon, you need to find the amino acid that is attatched to this tRNA.")
        print("     Do this by searching for its complementary codon in a codon chart. There is a codon chart in the folder included with this program.")
        print("---------------------------------")
        ProteinSynthesis()
    if choice == "":
        print("---------------------------------")
        ProteinSynthesis()
ProteinSynthesis()