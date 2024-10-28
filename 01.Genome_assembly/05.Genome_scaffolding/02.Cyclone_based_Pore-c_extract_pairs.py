#!/usr/bin/env python3

import sys
import pysam

if len(sys.argv) != 2:
    sys.exit('python3 %s <nameSorted.bam>' % (sys.argv[0]))

inFile = sys.argv[1]

if inFile.endswith('.bam'):
    samfile = pysam.AlignmentFile(inFile, "rb")
else:
    samfile = pysam.AlignmentFile(inFile, "r")

readID = ''
last_rid = ''
last_start = 0
last_end = 0
last_strand = ''
last_mapq = 0
idx = 0

for read in samfile:
    if read.is_mapped:
        if read.query_name.split(':')[0] == readID and last_rid != None:
            print(f'{last_rid}\t{last_start}\t{last_end}\t{readID}#{idx}\t{last_mapq}\t{last_strand}')
            readID = read.query_name.split(':')[0]
            if read.is_reverse:
                strand = '-'
            else:
                strand = '+'
            print(f'{read.reference_name}\t{read.reference_start}\t{read.reference_end}\t{readID}#{idx}\t{read.mapping_quality}\t{strand}')
            idx += 1
    readID = read.query_name.split(':')[0]
    last_rid = read.reference_name
    last_start = read.reference_start
    last_end = read.reference_end
    last_mapq = read.mapping_quality
    if read.is_reverse:
        last_strand = '-'
    else:
        last_strand = '+'
    if not read.is_mapped: idx = 0
