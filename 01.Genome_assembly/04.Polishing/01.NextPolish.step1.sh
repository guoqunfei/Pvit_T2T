echo start at `date`

# the file sgs.sort.bam generated from the third step 
bam=path/to/sgs.sort.bam

# the file curated fasta generated from the third step
genome=path/to/curated.fasta

python path/to/NextPolish/lib/nextpolish1.py -g ${genome} -t 1 -p 30 -s ${bam} > genome.nextpolish1.fa

path/to/bwa index genome.nextpolish1.fa

echo end at `date`
