#!/usr/bin/bash

#### Adjacent fragment pairs were extracted from wf-pore-c output file <null.ns.bam>
#### Wf-pore-c output file <null.ns.bam> is in the output/bams directory of wf-pore-c output results

SAMTOOLS="/path/to/your/samtools"
EXTRACT_SCRIPT="02.Cyclone_based_Pore-c_extract_pairs.py"
INPUT_BAM="output/bams/null.ns.bam"
FILTERED_BAM="null.ns.filtered.bam"
OUTPUT_BED="scaffolding_input.bed

echo start at `date`

${SAMTOOLS} view -F 4 -bh ${INPUT_BAM} > ${FILTERED_BAM}
python3 ${EXTRACT_SCRIPT} ${FILTERED_BAM} > ${OUTPUT_BED}

echo end at `date`
