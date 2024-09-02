#!/usr/bin/bash

#### Mapping Cyclone based Pore-C reads to the input contig_genome.fa
#### The process used for mapping is wf-pore-c (https://github.com/epi2me-labs/wf-pore-c)
#### Please install wf-pore-c before mapping

WORKFLOW_DIR="/path/to/your/wf-pore-c-1.1.0"
FASTQ_FILE="/path/to/your/Cyclone_based_Pore-C_read.fq.gz"
REFERENCE_GENOME="/path/to/your/contig_genome.fasta"
CUTTER="NlaIII" #Modify cutter according to the restriction enzyme actually used
THREADS=8 #The minimum requirement for wf-pore-c : CPUs = 8 , Memory = 32GB

echo start at `date`

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

echo end at `date`
