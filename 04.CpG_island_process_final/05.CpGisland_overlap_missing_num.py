#!/usr/bin/env python3
#--*-- Coding:utf8 --*--


import sys


def main():
    CpG_file,miss_file = sys.argv[1:3]


    cpg_dt = {}
    with open(CpG_file) as f:
        for line in f:
            cols = line.strip().split('\t')
            chrom = cols[0]
            cpg_start = int(cols[1]) 
            cpg_end = int(cols[2])
            if chrom not in cpg_dt:
                cpg_dt[chrom] = []
            cpg_dt[chrom].append((cpg_start,cpg_end))

    miss_dt = {}
    with open(miss_file) as f:
        for line in f:
            parts = line.strip().split('\t')
            chrom = parts[0]
            miss_start = int(parts[1])
            miss_end = int(parts[2])
            if chrom not in miss_dt:
                miss_dt[chrom] = []
            miss_dt[chrom].append((miss_start,miss_end))

    fully_covered_cpg = 0
    part_covered_cpg = 0
    cover_ratio_counts = {
            '>0.9':0,
            '>0.8':0,
            '>0.7':0,
            '>0.6':0,
            '>0.5':0,
            '>0.4':0,
            '>0.3':0,
            '>0.2':0,
            '>0.1':0,
            '>0':0
            }

    for chrom in cpg_dt.keys():
        if chrom in miss_dt:
            for cpg_start,cpg_end in cpg_dt[chrom]:
                length = cpg_end - cpg_start
                fully_covered = False
                part_covered = False
                final_cover_length = 0
                for miss_start,miss_end in miss_dt[chrom]:
                    if miss_start <=  cpg_start and miss_end >= cpg_end:
                        fully_covered = True
                        final_cover_length = length
                        break
                    elif miss_start < cpg_end and miss_end > cpg_start:
                        part_covered = True
                        cover_length = min(miss_end,cpg_end) - max(cpg_start,miss_start)
                        final_cover_length += cover_length

                if fully_covered:
                    fully_covered_cpg += 1
                elif part_covered:
                    part_covered_cpg += 1
                cover_ratio = final_cover_length / length if length > 0 else 0

                for threshold in [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0]:
                    if cover_ratio > threshold:
                        cover_ratio_counts[f'>{threshold}'] += 1



    print(f"fully_covered_cpg：{fully_covered_cpg}")
    print(f"part_covered_cpg:{part_covered_cpg}")
    for threshold in [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0]:
        print(f"covered_ratio > {threshold} cpgs: {cover_ratio_counts[f'>{threshold}']}")
if __name__ == "__main__":
    main()


