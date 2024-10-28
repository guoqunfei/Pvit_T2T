#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

file1 = sys.argv[1]

def gc_content(seq):
    seq = seq.upper()
    gc = (seq.count('G') + seq.count('C')) * 100 / len(seq)
    return gc

def o_e_ratio(seq):
    seq = seq.upper()
    o_e = (seq.count("CG") * len(seq)) / (seq.count("C") * seq.count("G")) if seq.count("C") * seq.count("G") > 0 else 0
    return o_e

def find_cpg_islands(file1):
    sequences = []
    seq = ""
    ID = ""
    with open(file1, "rt") as f:
        for line in f:
            if line.startswith(">"):
                if seq:
                    sequences.append((ID,seq))
                ID = line.strip("\n")
                seq = ""
            else:
                seq += line.strip("\n")
        if seq:
            sequences.append((ID,seq))

    results= []
    for ID,seq in sequences:
        cpg_island_count = 0
        cpg_islands = []
        for i in range(0, len(seq), 200):
            subseq = seq[i:i+200]
            gc = gc_content(subseq)
            o_e = o_e_ratio(subseq)
            if o_e > 0.6 and gc > 50:
                cpg_island_count += 1
                start = i + 1
                end = i + len(subseq)
                cpg_islands.append((start,end,gc,o_e))
        results.append((ID,cpg_island_count,seq,o_e_ratio(seq),gc_content(seq),cpg_islands))
    return results

def write_gff(results,output_file):
    with open(output_file,"w") as f:
        for ID, cpg_island_count, seq, o_e, gc, cpg_islands in results:
            for island in cpg_islands:
                start,end,gc_island,o_e_island = island
                f.write(f"{ID[1:]}\t.\tCpG_island\t{start}\t{end}\t.\t.\t.\tID=CpG_island_{ID[1:]}_{start}_{end};GC_content={gc_island:.2f};CpG_OE_ratio={o_e_island:.2f}\n")

if __name__ == "__main__":
    results = find_cpg_islands(file1)
    for ID, cpg_island_count, seq, o_e, gc, cpg_islands in results:
        print(ID + "\t" + str(cpg_island_count) + "\t" + str(o_e) + "\t" + str(gc))
    
    output_gff = "CpG_island.gff"
    write_gff(results,output_gff)
    
    #print("ID\tCpG Island Count\tO/E Ratio\tGC Content")
    #output = "{}\t{}\t{}\t{}".format(ID, str(cpg_island_count), o_e, gc)
    #print(output)

    #coordinates = "\t".join("[{},{}]".format(island[0], island[1]) for island in cpg_islands)
    #print(coordinates)


