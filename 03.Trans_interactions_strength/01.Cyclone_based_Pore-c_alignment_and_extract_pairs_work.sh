#!/usr/bin/bash

#### Mapping Cyclone based Pore-C reads to the input chromosome_genome.fa
#### The process used for mapping is wf-pore-c (https://github.com/epi2me-labs/wf-pore-c)
#### Please install wf-pore-c before mapping
#### Adjacent fragment pairs were extracted from wf-pore-c output file <null.ns.bam>
#### Wf-pore-c output file <null.ns.bam> is in the output/bams directory of wf-pore-c output results

WORKFLOW_DIR="/path/to/your/wf-pore-c-1.1.0"
FASTQ_FILE="/path/to/your/Cyclone_based_Pore-C_read.fq.gz"
REFERENCE_GENOME="/path/to/your/chromosome_genome.fasta"
CUTTER="NlaIII" #Modify cutter according to the restriction enzyme actually used
THREADS=8 #The minimum requirement for wf-pore-c : CPUs = 8 , Memory = 32GB
SAMTOOLS="/path/to/your/samtools"
EXTRACT_SCRIPT="/Genome_scaffolding/02.Cyclone_based_Pore-c_extract_pairs.py"
INPUT_BAM="output/bams/null.ns.bam"
FILTERED_BAM="null.ns.filtered.bam"
OUTPUT_BED="scaffolding_input.bed

echo align start at `date`

nextflow run ${WORKFLOW_DIR} \
    --fastq ${FASTQ_FILE} \
    --ref ${REFERENCE_GENOME} \
    -profile local \
    -resume \
    --cutter ${CUTTER} \
    --threads ${THREADS} \
    --hi_c \
    --mcool \
    --paired_end

echo "$?: wf-pore-c alignment"
echo align end at `date`

echo extract pairs start at `date`

${SAMTOOLS} view -F 4 -bh ${INPUT_BAM} > ${FILTERED_BAM}
python3 ${EXTRACT_SCRIPT} ${FILTERED_BAM} > ${OUTPUT_BED}

echo extract pairs end at `date`
