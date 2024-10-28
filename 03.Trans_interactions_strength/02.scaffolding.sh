#!/bin/bash

#### Please install yahs (https://github.com/c-zhou/yahs)

YAHS="/path/to/your/yahs"
REFERENCE_GENOME="/path/to/your/chromosome_genome.fasta" ##${REFERENCE_GENOME} is the same as the reference genome used for alignment
BED_FILE="scaffolding_input.bed"
SAMTOOLS="/path/to/your/samtools"
JUICER_TOOLS_JAR="/path/to/your/juicer_tools_1.22.01.jar"

echo start at `date`

${YAHS}/yahs --no-contig-ec --no-scaffold-ec ${REFERENCE_GENOME} ${BED_FILE}

${SAMTOOLS} faidx ${REFERENCE_GENOME}

less ${REFERENCE_GENOME}.fai | sort -k2 -nr | awk '{print "Chr"NR"\t1\t"$2"\t1\tW\t"$1"\t1\t"$2"\t+"}' > yahs.out_scaffolds_final.agp

juicer pre -o out_JBAT yahs.out.bin yahs.out_scaffolds_final.agp ${REFERENCE_GENOME}.fai
echo "$?: juicer pre -o out_JBAT yahs.out.bin yahs.out_scaffolds_final.agp ${REFERENCE_GENOME}.fai"

less yahs.out_scaffolds_final.agp | awk '{print $1"\t"$3}' > genomeSize.txt

mkdir sort
cd sort

cut -f1 ../yahs.out_scaffolds_final.agp |while read line
do
    echo "echo start at \`date\`" > ${line}.sh
    echo "less ../out_JBAT.txt | awk '\$2 == \"${line}\"' | sort -k6,6d > ${line}.txt" >> ${line}.sh
    echo "echo end at \`date\`" >> ${line}.sh
    sh ${line}.sh
done

cut -f1 ../yahs.out_scaffolds_final.agp |while read line
do
    cat ${line}.txt >> out_JBAT.sort.txt
done

cd ..

java -Xmx800G -jar ${JUICER_TOOLS_JAR} pre --threads 60 sort/out_JBAT.sort.txt out_JBAT.hic genomeSize.txt
echo "$?: java -Xmx800G -jar ${JUICER_TOOLS_JAR} pre --threads 60 sort/out_JBAT.sort.txt out_JBAT.hic genomeSize.txt"

echo end at `date`
