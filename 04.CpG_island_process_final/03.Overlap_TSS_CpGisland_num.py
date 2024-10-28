#!/usr/bin/env python3
#-*- coding:utf8 -*-
import sys

def main():
    CpGislandgff_file,annotation_file = sys.argv[1:3]

    cpg_islands = {}
    with open(CpGislandgff_file,'r') as f:
        for line in f:
            cols = line.strip().split('\t')
            chrom = cols[0]
            start = int(cols[3])
            end = int(cols[4])
            if chrom not in cpg_islands:
                cpg_islands[chrom] = []
            cpg_islands[chrom].append((start,end))


    genes = {}
    with open(annotation_file,'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if parts[2] == 'mRNA':
                chrom = parts[0]
                start = int(parts[3])
                end = int(parts[4])
                strand = parts[6]
                if chrom not in genes:
                    genes[chrom] = []
                if strand == '+':
                    tss = start
                elif strand == '-':
                    tss = end

                genes[chrom].append(tss)


    distances = range(0,200*41,200) 
    count_downstream = 0
    count_upstream = 0
    
    
    for distance in distances:
        count_downstream = 0
        count_upstream = 0


        for chrom in genes.keys():
            if chrom in cpg_islands.keys():
                for island_start,island_end in cpg_islands[chrom]:
                    for tss  in genes[chrom]:
                        if island_start <= tss + distance  <= island_end:
                            count_downstream += 1
                            break
                    for tss  in genes[chrom]:
                        if island_start <= tss - distance  <= island_end:
                            count_upstream += 1
                            break

        print( distance , count_downstream)
        print( -distance , count_upstream)

if __name__ == "__main__":
    main()
