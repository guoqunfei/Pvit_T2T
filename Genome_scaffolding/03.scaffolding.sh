#!/bin/bash

#### Please install yahs (https://github.com/c-zhou/yahs)

YAHS="/path/to/your/yahs"
REFERENCE_GENOME="/path/to/your/contig_genome.fasta"
BED_FILE="scaffolding_input.bed"
SAMTOOLS="/path/to/your/samtools"
JUICER_TOOLS_JAR="/path/to/your/juicer_tools_1.22.01.jar"

echo start at `date`

${YAHS}/yahs --no-contig-ec --no-scaffold-ec ${REFERENCE_GENOME} ${BED_FILE}

${SAMTOOLS} faidx ${REFERENCE_GENOME}

juicer pre -a -o out_JBAT yahs.out.bin yahs.out_scaffolds_final.agp ${REFERENCE_GENOME}.fai
echo "$?: juicer pre -a -o out_JBAT yahs.out.bin yahs.out_scaffolds_final.agp ${REFERENCE_GENOME}.fai"

ASM_SIZE=$(awk '{s+=$2} END{print s}' ${REFERENCE_GENOME}.fai)
GENOME_ID="assembly ${ASM_SIZE}"

java -Xmx800G -jar ${JUICER_TOOLS_JAR} pre --threads 60 out_JBAT.txt out_JBAT.hic ${GENOME_ID}
echo "$?: java -Xmx800G -jar ${JUICER_TOOLS_JAR} pre --threads 60 out_JBAT.txt out_JBAT.hic ${GENOME_ID}"

echo end at `date`

# Download <out_JBAT.assembly> <out_JBAT.hic>
# Use juicebox to open <out_JBAT.hic> and import <out_JBAT.assembly>
# Adjust
# Export <new.assembly>
