#!/usr/bin/env python3
#--*-- Coding:utf8 --*--

import sys

def main():

    TSSfile,CPGfile =sys.argv[1:3]

    TSS_dt = {}
    with open(TSSfile) as f:
        for line in f:
            cols = line.strip().split('\t')
            chrom = cols[0]
            tss = int(cols[1])
            if chrom not in TSS_dt:
                TSS_dt[chrom] = []
            TSS_dt[chrom].append(tss)


    CpG_dt = {}
    with open(CPGfile) as f:
        for line in f:
            line = line.strip().split('\t')
            chrom = line[0]
            start = int(line[1])
            end = int(line[2])
            if chrom not in CpG_dt:
                CpG_dt[chrom] = []
            CpG_dt[chrom].append((start,end))


    for chrom in TSS_dt:
        if chrom in CpG_dt:
            tsss = TSS_dt[chrom]
            CpG_island = CpG_dt[chrom]

            for tss in tsss:
                min_distance = float('inf')
                closest_cpg = None
                for start,end in CpG_island:

                    if tss < start:
                        distance = start -tss
                    if tss > end:
                        distance = end - tss
                    if start <= tss <= end:
                        distance = 0

                    if abs(distance) < abs(min_distance):
                        min_distance = distance
                        closest_cpg = (start, end)


                print(f"{chrom}\t{tss}\t{closest_cpg}\t{min_distance}")


if __name__ == "__main__":
    main()
