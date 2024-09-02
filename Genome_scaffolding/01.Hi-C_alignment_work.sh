#!/usr/bin/bash

CHROMAP="path/to/your/chromap"
REFERENCE_GENOME="path/to/your/contig_genome.fasta"
FASTQ1_FILE="path/to/your/Hi-C_Reads.1.fastq.gz"
FASTQ2_FILE="path/to/your/Hi-C_Reads.2.fastq.gz"
SAMTOOLS="path/to/your/samtools"
BEDTOOLS="path/to/your/bedtools"

echo start at `date`

${CHROMAP} -i -r ${REFERENCE_GENOME} -o contigs.index

${CHROMAP} --preset hic \
    -r ${REFERENCE_GENOME} \
    -x contigs.index \
    --remove-pcr-duplicates \
    -1 ${FASTQ1_FILE} \
    -2 ${FASTQ2_FILE} \
    --SAM \
    -o chromap.sam \
    -t 10

echo "$?: chromap alignment"

${SAMTOOLS} view -@ 10 -bh chromap.sam | ${SAMTOOLS} sort -@ 10 -n > chromap.bam
echo "$?: ${SAMTOOLS} view -@ 10 -bh chromap.sam | ${SAMTOOLS} sort -@ 10 -n > chromap.bam"

${SAMTOOLS} view -bh -u -F0xF0C -q 10 chromap.bam | ${BEDTOOLS} bamtobed | awk -v OFS='\t' '{$4=substr($4,1,length($4)-2); print}' > scaffolding_input.bed
echo "$?: ${SAMTOOLS} view -bh -u -F0xF0C -q 10 chromap.bam | ${BEDTOOLS} bamtobed | awk -v OFS='\t' '{$4=substr($4,1,length($4)-2); print}' > scaffolding_input.bed"

rm -f chromap.sam chromap.bam

echo end at `date`
