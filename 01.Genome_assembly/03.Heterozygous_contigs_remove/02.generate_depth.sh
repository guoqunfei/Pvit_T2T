echo start at `date`

# The contig-level genome assembled by NextDenovo
genome=path/to/nd.asm.fasta

path/to/samtools faidx ${genome}

bam=path/to/sgs.sort.bam

less ${genome}.fai | awk '{print $1}' |  while read p;do path/to/samtools depth  -@ 8 -a -r ${p} ${bam} | awk '{print $3}' | sort | uniq -c | sort -k2 -n | awk '{if(NR <= 200) print "'${p}'\t"$2"\t"$1; else if(NR >= 200) {sum +=$1; print "'${p}'\t200\t"sum}}' | awk 'FNR <= 200 {print} END {print}' >> sgs.sort.bam.genocov;done

seq 1 200 | while read p;do less sgs.sort.bam.genocov | awk '$2 == "'${p}'" {sum += $3};END{print "genome\t'${p}'\t"sum}';done >> sgs.sort.bam.genocov

echo end at at `date`
