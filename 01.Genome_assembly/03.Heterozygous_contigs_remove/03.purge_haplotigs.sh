echo start at `date`

# The contig-level genome assembled by NextDenovo
genome=path/to/nd.asm.fasta

path/to/purge_haplotigs  contigcov  -i sgs.sort.bam.genocov -o coverage_stats.csv  -l 10  -m 53 -h 120

path/to/purge_haplotigs purge  -g ${genome} -c coverage_stats.csv -t 60

# Finally, the file named "curated.fasta" that removing heterozygous contigs

echo end at `date`
