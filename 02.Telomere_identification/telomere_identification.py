#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import re
import argparse
import os

def merge_region_list(region_list):
    """合并相邻的区域"""
    merged_region_list = []

    region_sort_list = sorted(region_list, key=lambda x: (x[0], x[1]))
    if region_sort_list:
        start, end = region_sort_list[0]
        for region in region_sort_list[1:]:
            if region[0] <= end + 1000:
                end = max(end, region[1])
            else:
                merged_region_list.append([start, end])
                start, end = region
        merged_region_list.append([start, end])

    return merged_region_list

def reverse_complement(seq):
    """生成序列的反向互补序列"""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='Identify telomeric regions in a genome sequence.')
    parser.add_argument('genome_file', help='The genome file in FASTA format.')
    parser.add_argument('-m', '--motif', default='TTAGGG',
                        help='Telomeric motif to search for (default: %(default)s).')
    parser.add_argument('-o', '--output', default=None,
                        help='Output file to write the results. If not provided, a default name will be generated based on the genome file name.')
    parser.add_argument('--min_length', type=int, default=1000,
                        help='Minimum length of telomeric regions to consider (default: %(default)s).')
    parser.add_argument('--min_repeats', type=int, default=50,
                        help='Minimum number of repeats in a region to consider (default: %(default)s).')
    parser.add_argument('--buffer', type=int, default=100000,
                        help='Buffer distance from chromosome ends (default: %(default)s).')
    return parser.parse_args()

def main():
    args = parse_args()

    # Generate the list of motifs including reverse, complement, and reverse complement
    motif = args.motif.upper()
    reverse_motif = motif[::-1]
    complement_motif = reverse_complement(motif)
    reverse_complement_motif = reverse_complement(reverse_motif)
    telo_motif = [motif, reverse_motif, complement_motif, reverse_complement_motif]

    # If no output file is specified, generate a default file name based on the genome file name
    output_file = args.output if args.output else os.path.splitext(args.genome_file)[0] + "_telomere.out"

    genome_dict, seq = {}, ''
    with open(args.genome_file) as f_in:
        for line in f_in:
            if line.startswith('>'):
                if seq:
                    genome_dict[seq_id] = seq
                seq_id = line.split()[0].lstrip('>')
                seq = ''
            else:
                seq += line.rstrip('\n')
        genome_dict[seq_id] = seq
    print(genome_dict.keys())

    motif_patterns = {motif: re.compile('(?=' + motif + ')') for motif in telo_motif}

    with open(output_file, 'w') as f_out:
        for seq_id, sequence in genome_dict.items():
            print(seq_id)
            chr_len = len(sequence)
            for motif, pattern in motif_patterns.items():
                motif_region_list = [(m.start() + 1, m.start() + len(motif)) for m in pattern.finditer(sequence)]
                merged_motif_region_list = merge_region_list(motif_region_list)

                for start, end in merged_motif_region_list:
                    if end - start < args.min_length:
                        continue
                    motif_num = sequence[start:end].count(motif)
                    if motif_num <= args.min_repeats or (args.buffer < end < chr_len - args.buffer):
                        continue
                    f_out.write(f'{seq_id}\t{motif}\t{start}\t{end}\t{motif_num}\n')

if __name__ == "__main__":
    main()

