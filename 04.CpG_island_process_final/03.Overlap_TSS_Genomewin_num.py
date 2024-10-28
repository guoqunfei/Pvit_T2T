#!/usr/bin/env python3
#-*- coding:utf8 -*-
import sys

def main():
    Genomewin_file,annotation_file = sys.argv[1:3]


    wins = {}
    with open(Genomewin_file,'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            chrom = parts[0]
            start = int(parts[3])
            end = int(parts[4])
            if chrom not in wins:
                wins[chrom] = []
            wins[chrom].append((start,end))


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


        for chrom in wins.keys():
            if chrom in wins.keys():
                for win_start,win_end in wins[chrom]:
                    for tss  in genes[chrom]:
                        if win_start <= tss + distance  <= win_end:
                            count_downstream += 1
                            break
                    for tss  in genes[chrom]:
                        if win_start <= tss - distance  <= win_end:
                            count_upstream += 1
                            break

        print( distance , count_downstream)
        print( -distance , count_upstream)


if __name__ == "__main__":
    main()
