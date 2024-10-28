echo start at `date`

# The contig-level genome assembled by NextDenovo
genome=path/to/nd.asm.fasta

# The short paired-end whole-genome reads sequencing by DNBSEQ platform
read1=fq1.gz
read2=fq2.gz

path/to/bwa mem -t 6 ${genome} ${read1} ${read2} | samtools view --threads 6 -F 0x4 -b - | samtools fixmate -m --threads 6 - - | samtools sort -m 2g --threads 6 - | samtools markdup --threads 6 -r - sgs.sort.bam

echo end at `date`
