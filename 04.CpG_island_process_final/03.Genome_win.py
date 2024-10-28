
import sys

input_file = sys.argv[1]
def gc_content(seq) :
    g_count = seq.count('G')
    c_count = seq.count('C')
    gc  = (g_count + c_count) * 100 / len(seq)
    return gc

def oe_ratio(seq):
    seq = seq.upper()
    o_e = (seq.count("CG") * len(seq)) / (seq.count("C") * seq.count("G")) if seq.count("C") * seq.count("G") > 0 else 0
    return o_e
def process_genome(input_file,win_size=200,output_file='win.gff_200bp.gff'):
    with open(input_file,'r') as f,open(output_file,'w') as out_file:
        out_file.write("##gff-version 3\n")
        chrom = None
        seq = ''

        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if chrom:
                    pro_genome(chrom,seq,win_size,out_file)
                    seq = ''
                    
                chrom = line[1:]
            else:
                seq += line
        if chrom:
            pro_genome(chrom,seq,win_size,out_file)

def pro_genome(chrom,seq,win_size,out_file):
    seq_length = len(seq)
    
    position = 0

    while position + win_size <= seq_length:
        win_seq = seq[position:position + win_size]
        gc = gc_content(win_seq)
        oe = oe_ratio(win_seq)

        start = position + 1
        end = position + win_size

        attributes = f"GC_Content={gc:.4f};CpG_OE={oe:.4f}"
        gff_line = f"{chrom}\t.\twin\t{start}\t{end}\t.\t.\t.\t{attributes}\n"

        out_file.write(gff_line)
        position += win_size

if __name__ == "__main__":
    process_genome(input_file)


