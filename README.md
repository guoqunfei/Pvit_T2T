# Pvit_T2T
This page demonstrates all the analyses in the paper, titled "A near-complete genome assembly of the bearded dragon Pogona vitticeps provides insights into the origin of Pogona sex chromosomes".

## Genome assembly
```
1) Removing the chimeric reads of CycloneSEQ long reads by using Yacrd v1.0.0
# To merge all CycloneSEQ data into a single file named cyclone.fa and then use minimap2 for pairwise alignment of all reads
    bash ./01.Chimeric_reads_filter/01.minimap2.sh
# Using yacrd to filter chimeric reads
    bash ./01.Chimeric_reads_filter/02.yacrd.sh
2) Contig-level assembly
# Using NextDenovo to do the contig-level assembly
    bash ./02.Cyclone_contig_assembly/NextDenovo.sh
3) Removing heterozygous contigs
# To make the short reads align to the contig-level genome
    bash ./03.Heterozygous_contigs_remove/01.DNBSEQ_reads_alignment.sh
# To generate the genome sequencing depth distribution file : sgs.sort.bam.genocov
    bash ./03.Heterozygous_contigs_remove/02.generate_depth.sh
# To generate the genome file that removing heterozygous contigs : curated.fasta
    bash ./03.Heterozygous_contigs_remove/03.purge_haplotigs.sh
4) Polishig by short paired-end whole genome reads sequencing by DNBSEQ platform
# The first step to polish
    bash ./04.Polishing/01.NextPolish.step1.sh
# The second step to polish
    bash ./04.Polishing/02.NextPolish.step2.sh
5) Genome scaffolding with Cyclone based Pore-C reads and Hi-C reads.
# For Hi-C reads, please follow those steps:
# step1: 
    bash ./05.Genome_scaffolding/01.Hi-C_alignment_work.sh
# step2: 
    bash ./05.Genome_scaffolding/03.scaffolding.sh
# For Cyclone based Pore-C reads, please follow those steps:
# step1: 
    bash ./05.Genome_scaffolding/01.Cyclone_based_Pore-c_alignment_work.sh
# step2: 
    bash ./05.Genome_scaffolding/02.Cyclone_based_Pore-c_extract_pairs.sh
# step3: 
    bash ./05.Genome_scaffolding/03.scaffolding.sh
# Using juicerbox for manually correction
```

## Telomere identification
```
# To find the simple telomeric repeat unit in the genome provided
python 02.Telomere_identification/telomere_identification.py genome.fa
```

## Hi-C analysis
```
# Calculate trans interactions strength.
# For Hi-C reads, please follow those steps:
# step1: 
    bash ./03.Trans_interactions_strength/01.Hi-C_alignment_work.sh
# step2: 
    bash ./03.Trans_interactions_strength/02.scaffolding.sh
# step3: 
    bash ./03.Trans_interactions_strength/03.Trans_interactions_strength_calculate.sh
```

## CpG analysis
```
# Identification and analysis of CpG islands based on genome.fa

# For genome.fa  file, please follow those steps:

# step1: 
    bash ./04.CpG_island_process_final/01.CpG_island.sh
# step2: 
    bash ./04.CpG_island_process_final/02.CpG_island_link.sh
# step3: 
    bash ./04.CpG_island_process_final/03.work.sh
# step4: 
    bash ./04.CpG_island_process_final/04.work.sh
# step5: 
    bash ./04.CpG_island_process_final/05.work.sh
```

