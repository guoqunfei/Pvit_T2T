echo start at `date`

# The genome file genome.nextpolish1.fa generated from the previous step
genome=path/to/genome.nextpolish1.fa

# The short paired-end whole-genome reads sequencing by DNBSEQ platform
read1=fq1.gz
read2=fq2.gz

path/to/bwa mem -t 6 ${genome} ${read1} ${read2} | samtools view --threads 6 -F 0x4 -b - | samtools fixmate -m --threads 6 - - | samtools sort -m 2g --threads 6 - | samtools markdup --threads 6 -r - nextpolish2.bam

bam=nextpolish2.bam

python path/to/NextPolish/lib/nextpolish1.py -g ${genome} -t 2 -p 30 -s ${bam} > genome.nextpolish2.fa

echo end at `date`
