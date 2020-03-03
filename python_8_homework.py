class RNA:
    def __init__(self, rna: str):
        flag = True
        rna.upper()
        for nucleotide in rna:
            if len(rna) <= 1 or nucleotide not in "AGUC":
                flag = False
                break
        if flag:
            self.rna = rna
        else:
            self.rna = None
        self.current_index = 0

    def gc_content(self):
        if self.rna is None:
            return None
        count_gc = 0
        for nucleotide in self.rna:
            if nucleotide in ["G", "C"]:
                count_gc += 1
        return count_gc / len(self.rna)

    def reverse_complement(self):
        if self.rna is None:
            return None
        complement_chain = ""
        complement_rule = {"A": "U", "U": "A", "G": "C", "C": "G"}
        for nucleotide in self.rna:
            complement_chain += complement_rule[nucleotide]
        return complement_chain

    def __next__(self):
        if self.rna is None:
            return None
        if self.current_index < len(self.rna):
            current_nucleotide = self.rna[self.current_index]
            self.current_index += 1
            return current_nucleotide
        else:
            raise StopIteration

    def __iter__(self):
        self.current_index = 0
        return self

    def __eq__(self, other):
        return isinstance(other, DNA) and self.gc_content() == self.gc_content()

    def __hash__(self):
        return hash(self.rna)


class DNA:
    def __init__(self, dna: str):
        flag = True
        dna.upper()
        for nucleotide in dna:
            if len(dna) <= 1 or nucleotide not in "AGTC":
                flag = False
                break
        if flag:
            self.dna = dna
        else:
            self.dna = None
        self.current_index = 0

    def gc_content(self):
        if self.dna is None:
            return None
        count_gc = 0
        for nucleotide in self.dna:
            if nucleotide in ["G", "C"]:
                count_gc += 1
        return count_gc / len(self.dna)

    def reverse_complement(self):
        if self.dna is None:
            return None
        complement_chain = ""
        complement_rule = {"A": "T", "T": "A", "G": "C", "C": "G"}
        for nucleotide in self.dna:
            complement_chain += complement_rule[nucleotide]
        return complement_chain

    def __next__(self):
        if self.dna is None:
            return None
        if self.current_index < len(self.dna):
            current_nucleotide = self.dna[self.current_index]
            self.current_index += 1
            return current_nucleotide
        else:
            raise StopIteration

    def __iter__(self):
        self.current_index = 0
        return self

    def __eq__(self, other):
        return isinstance(other, DNA) and self.gc_content() == self.gc_content()

    def __hash__(self):
        return hash(self.dna)

    def transcribe(self):
        if self.dna is None:
            return None
        m_rna = ""
        transcription_rule = {"A": "U", "T": "A", "G": "C", "C": "G"}
        for nucleotide in self.dna:
            m_rna += transcription_rule[nucleotide]
        return RNA(rna=m_rna)


if __name__ == "__main__":
    exampleDNA = DNA(dna="AGTC")
    exampleRNA = RNA(rna="AGUC")
    brokenExampleDNA = DNA(dna="A")
    brokenExampleRNA = RNA(rna="AGTC")
    print(exampleDNA.gc_content())
    print(exampleDNA.reverse_complement())
    print(exampleDNA.transcribe())
    print(exampleRNA.gc_content())
    print(exampleRNA.reverse_complement())
    print(next(exampleRNA))
    print(next(exampleDNA))
    print(exampleDNA.__eq__(exampleRNA))
    print(exampleRNA.__eq__(exampleRNA))
    print(brokenExampleDNA.gc_content())
    print(brokenExampleDNA.reverse_complement())
    print(brokenExampleDNA.transcribe())
    print(brokenExampleRNA.gc_content())
    print(brokenExampleRNA.reverse_complement())
    nucleous = set()
    nucleous.add(exampleRNA)
    nucleous.add(exampleDNA)
    print(exampleRNA in nucleous)
    print(exampleDNA in nucleous)
